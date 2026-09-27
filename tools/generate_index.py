#!/usr/bin/env python3
"""Generate a complete RubyGems index for LibPool."""

from __future__ import annotations

import argparse
import concurrent.futures
import gzip
import hashlib
import json
import re
import sqlite3
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Iterable


INDEX_BASE = "https://index.rubygems.org"
API_BASE = "https://rubygems.org/api/v1"
USER_AGENT = "LibPool-indexer/1.0 (+https://github.com/LibPool)"
DEFAULT_CACHE = Path("cache/rubygems_cache.sqlite3")
DEFAULT_WORKERS = 32
RETRIES = 6
MAJORS = (1, 2, 3, 4)
WINDOWS_RESERVED_NAMES = {
    "CON",
    "PRN",
    "AUX",
    "NUL",
    *(f"COM{index}" for index in range(1, 10)),
    *(f"LPT{index}" for index in range(1, 10)),
}


class FetchError(RuntimeError):
    pass


class NotFound(FetchError):
    pass


def http_text(url: str, retries: int = RETRIES) -> str:
    last_error: Exception | None = None
    for attempt in range(retries):
        request = urllib.request.Request(
            url,
            headers={
                "Accept": "text/plain, application/json",
                "Accept-Encoding": "gzip",
                "User-Agent": USER_AGENT,
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read()
                if response.headers.get("Content-Encoding") == "gzip":
                    body = gzip.decompress(body)
                return body.decode("utf-8")
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                raise NotFound(f"not found: {url}") from exc
            if 400 <= exc.code < 500 and exc.code != 429:
                raise FetchError(f"HTTP Error {exc.code}: {url}") from exc
            last_error = exc
        except Exception as exc:  # noqa: BLE001 - retry transient network errors
            last_error = exc
        if attempt + 1 < retries:
            time.sleep(min(30.0, 0.5 * (2**attempt)))
    raise FetchError(f"failed after {retries} attempts: {url}: {last_error}")


def http_json(url: str) -> dict[str, Any]:
    payload = json.loads(http_text(url))
    if not isinstance(payload, dict):
        raise FetchError(f"expected a JSON object: {url}")
    return payload


def init_cache(connection: sqlite3.Connection) -> None:
    connection.execute("PRAGMA journal_mode=WAL")
    connection.execute("PRAGMA synchronous=NORMAL")
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS gem_names (
            name TEXT PRIMARY KEY
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS gem_versions (
            name TEXT NOT NULL,
            version TEXT NOT NULL,
            ruby_requirement TEXT,
            created_at TEXT,
            checksum TEXT,
            PRIMARY KEY (name, version)
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS gem_info_state (
            name TEXT PRIMARY KEY,
            fetched_at INTEGER NOT NULL,
            version_count INTEGER NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS gem_details (
            name TEXT PRIMARY KEY,
            details_json TEXT NOT NULL,
            fetched_at INTEGER NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
        """
    )
    connection.execute(
        "CREATE INDEX IF NOT EXISTS idx_gem_versions_name ON gem_versions(name)"
    )


def get_metadata(connection: sqlite3.Connection, key: str) -> str | None:
    row = connection.execute(
        "SELECT value FROM metadata WHERE key = ?", (key,)
    ).fetchone()
    return row[0] if row else None


def set_metadata(
    connection: sqlite3.Connection, key: str, value: str
) -> None:
    connection.execute(
        "INSERT OR REPLACE INTO metadata(key, value) VALUES (?, ?)",
        (key, value),
    )


def fetch_names(
    connection: sqlite3.Connection, refresh: bool
) -> list[str]:
    if refresh:
        connection.execute("DELETE FROM gem_names")
        connection.execute("DELETE FROM metadata WHERE key = 'names_complete'")
        connection.commit()
    if get_metadata(connection, "names_complete") == "1":
        names = [
            row[0]
            for row in connection.execute(
                "SELECT name FROM gem_names ORDER BY name"
            )
        ]
        print(f"Using cached gem name list: {len(names)} gems")
        return names

    print("Fetching RubyGems names index...")
    text = http_text(f"{INDEX_BASE}/names")
    names: list[str] = []
    for line in text.splitlines():
        name = line.strip()
        if not name or name == "---" or name.startswith("created_at:"):
            continue
        names.append(name)
    names = sorted(set(names), key=str.casefold)
    connection.executemany(
        "INSERT OR IGNORE INTO gem_names(name) VALUES (?)",
        ((name,) for name in names),
    )
    set_metadata(connection, "names_complete", "1")
    connection.commit()
    print(f"Fetched {len(names)} gem names")
    return names


def fetch_info(name: str) -> str:
    encoded = urllib.parse.quote(name, safe="")
    return http_text(f"{INDEX_BASE}/info/{encoded}")


_RUBY_RE = re.compile(
    r"(?:^|,)ruby:(?P<value>.*?)(?=,rubygems:|,created_at:|,checksum:|$)"
)
_CREATED_AT_RE = re.compile(
    r"(?:^|,)created_at:(?P<value>[^,]+)"
)
_CHECKSUM_RE = re.compile(r"(?:^|,)checksum:(?P<value>[0-9a-fA-F]+)")


def parse_info(text: str) -> list[tuple[str, str | None, str | None, str | None]]:
    versions: list[tuple[str, str | None, str | None, str | None]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line == "---":
            continue
        parts = line.split(" ", 1)
        if not parts[0]:
            continue
        version = parts[0]
        metadata = parts[1] if len(parts) == 2 else ""
        ruby_match = _RUBY_RE.search(metadata)
        created_match = _CREATED_AT_RE.search(metadata)
        checksum_match = _CHECKSUM_RE.search(metadata)
        versions.append(
            (
                version,
                ruby_match.group("value").strip() if ruby_match else None,
                created_match.group("value").strip() if created_match else None,
                checksum_match.group("value").strip() if checksum_match else None,
            )
        )
    return versions


def fetch_info_worker(
    name: str,
) -> list[tuple[str, str | None, str | None, str | None]]:
    return parse_info(fetch_info(name))


def store_info(
    connection: sqlite3.Connection,
    name: str,
    versions: list[tuple[str, str | None, str | None, str | None]],
) -> int:
    connection.execute("DELETE FROM gem_versions WHERE name = ?", (name,))
    connection.executemany(
        """
        INSERT INTO gem_versions
            (name, version, ruby_requirement, created_at, checksum)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            (name, version, ruby_version, created_at, checksum)
            for version, ruby_version, created_at, checksum in versions
        ),
    )
    connection.execute(
        """
        INSERT OR REPLACE INTO gem_info_state(name, fetched_at, version_count)
        VALUES (?, ?, ?)
        """,
        (name, int(time.time()), len(versions)),
    )
    return len(versions)


def fetch_details(name: str) -> dict[str, Any] | None:
    encoded = urllib.parse.quote(name, safe="")
    try:
        return http_json(f"{API_BASE}/gems/{encoded}.json")
    except NotFound:
        return None


def cached_set(connection: sqlite3.Connection, query: str) -> set[str]:
    return {row[0] for row in connection.execute(query)}


def fetch_metadata_phase(
    connection: sqlite3.Connection,
    names: Iterable[str],
    workers: int,
    refresh: bool,
    use_processes: bool,
) -> None:
    names = list(names)
    if refresh:
        connection.execute("DELETE FROM gem_info_state")
        connection.execute("DELETE FROM gem_versions")
        connection.execute("DELETE FROM gem_details")
        connection.commit()

    cached_info = cached_set(connection, "SELECT name FROM gem_info_state")
    missing_info = [name for name in names if name not in cached_info]
    if missing_info:
        print(
            f"Fetching version metadata: {len(missing_info)} missing, "
            f"{len(cached_info)} cached, {workers} workers"
        )
        _run_parallel(
            connection,
            missing_info,
            workers,
            fetch_info_worker,
            "version metadata",
            lambda name, versions: store_info(connection, name, versions),
            use_processes,
        )
    else:
        print(f"Using cached version metadata: {len(cached_info)} gems")

    cached_details = cached_set(connection, "SELECT name FROM gem_details")
    missing_details = [name for name in names if name not in cached_details]
    if missing_details:
        print(
            f"Fetching gem metadata: {len(missing_details)} missing, "
            f"{len(cached_details)} cached, {workers} workers"
        )
        _run_parallel(
            connection,
            missing_details,
            workers,
            fetch_details,
            "gem metadata",
            lambda name, payload: store_details(connection, name, payload),
            use_processes,
        )
    else:
        print(f"Using cached gem metadata: {len(cached_details)} gems")


def store_details(
    connection: sqlite3.Connection,
    name: str,
    payload: dict[str, Any] | None,
) -> None:
    connection.execute(
        """
        INSERT OR REPLACE INTO gem_details(name, details_json, fetched_at)
        VALUES (?, ?, ?)
        """,
        (
            name,
            json.dumps(payload or {}, ensure_ascii=False),
            int(time.time()),
        ),
    )


def _run_parallel(
    connection: sqlite3.Connection,
    names: list[str],
    workers: int,
    fetch: Any,
    label: str,
    store: Any,
    use_processes: bool,
) -> None:
    """Fetch a large name list through a bounded sliding request window.

    Submitting one future for every gem can deadlock large runs behind a few
    slow responses and makes it impossible to durably commit completed work.
    Keep only a small multiple of the worker count in flight instead.
    """
    lock = threading.Lock()
    completed = 0
    failed: list[tuple[str, str]] = []
    in_flight = 0
    submitted = 0
    window_size = max(workers * 4, 64)
    executor_class: type[concurrent.futures.Executor]
    executor_class = (
        concurrent.futures.ProcessPoolExecutor
        if use_processes
        else concurrent.futures.ThreadPoolExecutor
    )
    with executor_class(max_workers=workers) as executor:
        futures: dict[concurrent.futures.Future[Any], str] = {}

        def submit_one() -> None:
            nonlocal in_flight, submitted
            if submitted >= len(names):
                return
            name = names[submitted]
            submitted += 1
            futures[executor.submit(fetch, name)] = name
            in_flight += 1

        for _ in range(min(window_size, len(names))):
            submit_one()

        while futures:
            done, _ = concurrent.futures.wait(
                futures,
                return_when=concurrent.futures.FIRST_COMPLETED,
                timeout=30,
            )
            if not done:
                print(
                    f"  {completed}/{len(names)} {label} fetched, "
                    f"{len(failed)} failed, {in_flight} in flight",
                    flush=True,
                )
                continue
            for future in done:
                name = futures.pop(future)
                in_flight -= 1
                try:
                    payload = future.result()
                except Exception as exc:  # noqa: BLE001 - continue and report failures
                    failed.append((name, str(exc)))
                else:
                    with lock:
                        store(name, payload)
                        completed += 1
                        if completed % 250 == 0:
                            connection.commit()
                            print(
                                f"  {completed}/{len(names)} {label} fetched, "
                                f"{len(failed)} failed",
                                flush=True,
                            )
                submit_one()

            if (completed + len(failed)) % 1000 == 0:
                connection.commit()
    connection.commit()
    if failed:
        print(f"Failed {label}: {len(failed)}", file=sys.stderr)
        for name, error in failed[:50]:
            print(f"  {name}: {error}", file=sys.stderr)
        if len(failed) > 50:
            print(f"  ... {len(failed) - 50} more", file=sys.stderr)
        raise RuntimeError(f"{len(failed)} {label} requests failed")


def _parse_version(value: str) -> tuple[int, int, int, int]:
    numbers = [int(part) for part in re.findall(r"\d+", value)[:4]]
    numbers.extend([0] * (4 - len(numbers)))
    return tuple(numbers[:4])  # type: ignore[return-value]


def _next_safe_version(
    value: tuple[int, int, int, int], component_count: int
) -> tuple[int, int, int, int]:
    # RubyGems treats ~> 2.7 as <3.0, but ~> 2.7.0 as <2.8.0.
    # The number of written components therefore carries meaning.
    major, minor, patch, build = value
    if component_count <= 1:
        return major + 1, 0, 0, 0
    if component_count == 2:
        return major, minor + 1, 0, 0
    if component_count == 3:
        return major, minor, patch + 1, 0
    return major, minor, patch, build + 1


_CONSTRAINT_RE = re.compile(
    r"(?P<op>~>|>=|<=|!=|>|<|=)?\s*"
    r"(?P<version>\d+(?:\.\d+){0,3})"
)


def _branch_bounds(
    branch: str,
) -> tuple[tuple[int, int, int, int], bool, tuple[int, int, int, int], bool]:
    lower = (0, 0, 0, 0)
    lower_inclusive = True
    upper = (1_000_000, 0, 0, 0)
    upper_inclusive = False
    for match in _CONSTRAINT_RE.finditer(branch):
        operator = match.group("op") or "="
        version_text = match.group("version")
        version = _parse_version(version_text)
        component_count = len(version_text.split("."))
        if operator == ">=":
            if version > lower:
                lower, lower_inclusive = version, True
        elif operator == ">":
            if version >= lower:
                lower, lower_inclusive = version, False
        elif operator == "<=":
            if version < upper:
                upper, upper_inclusive = version, True
        elif operator == "<":
            if version <= upper:
                upper, upper_inclusive = version, False
        elif operator == "~>":
            if version > lower:
                lower, lower_inclusive = version, True
            safe_upper = _next_safe_version(version, component_count)
            if safe_upper < upper:
                upper, upper_inclusive = safe_upper, False
        elif operator == "!=":
            continue
        elif operator == "=":
            if version > lower:
                lower, lower_inclusive = version, True
            if version < upper:
                upper, upper_inclusive = version, True
    return lower, lower_inclusive, upper, upper_inclusive


def constraint_intersects_major(
    constraint: str | None, major: int
) -> bool:
    if constraint is None or not constraint.strip():
        return True
    major_start = (major, 0, 0, 0)
    major_end = (major + 1, 0, 0, 0)
    for branch in constraint.split("||"):
        lower, lower_inclusive, upper, upper_inclusive = _branch_bounds(branch)
        if lower > upper or (
            lower == upper and not (lower_inclusive and upper_inclusive)
        ):
            continue
        if upper <= major_start or lower >= major_end:
            continue
        return True
    return False


def supported_majors(
    connection: sqlite3.Connection, name: str
) -> list[int]:
    rows = connection.execute(
        """
        SELECT ruby_requirement
        FROM gem_versions
        WHERE name = ?
        """,
        (name,),
    ).fetchall()
    found = {
        major
        for major in MAJORS
        if any(constraint_intersects_major(row[0], major) for row in rows)
    }
    if not found:
        found.add(3)
    return [major for major in MAJORS if major in found]


def safe_component(value: str) -> str:
    value = value.strip().replace("/", "_").replace("\\", "_")
    value = re.sub(r"[\x00-\x1f<>:\"|?*]", "_", value)
    value = value.rstrip(". ") or "_"
    if value.split(".", 1)[0].upper() in WINDOWS_RESERVED_NAMES:
        value = f"_{value}"
    if len(value) > 100:
        digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:10]
        value = f"{value[:80].rstrip('. ')}~{digest}"
    return value


def build_component_map(names: Iterable[str]) -> dict[str, str]:
    groups: dict[str, list[str]] = {}
    for name in names:
        component = safe_component(name)
        groups.setdefault(component.casefold(), []).append(name)

    result: dict[str, str] = {}
    for group in groups.values():
        if len(group) == 1:
            result[group[0]] = safe_component(group[0])
            continue
        for name in group:
            digest = hashlib.sha1(name.encode("utf-8")).hexdigest()[:10]
            result[name] = f"{safe_component(name)}~{digest}"
    return result


def unique_links(items: Iterable[tuple[str, Any]]) -> list[tuple[str, str]]:
    seen: set[str] = set()
    links: list[tuple[str, str]] = []
    for label, raw_url in items:
        url = str(raw_url or "").strip()
        if not url or url in seen:
            continue
        seen.add(url)
        links.append((label, url))
    return links


def derive_tags(
    name: str,
    details: dict[str, Any],
) -> list[str]:
    info = str(details.get("info") or "")
    text = " ".join(
        [
            name,
            str(details.get("name") or ""),
            info,
            " ".join(str(item) for item in details.get("licenses") or []),
        ]
    ).lower()
    tags: list[str] = []
    rules = [
        ("web", ("web", "rails", "rack", "sinatra", "http", "server", "api")),
        ("cli", ("cli", "console", "command line", "terminal")),
        ("database", ("database", "sql", "postgres", "mysql", "sqlite", "redis")),
        ("testing", ("test", "spec", "mock", "fixture", "assert")),
        ("security", ("auth", "crypto", "encrypt", "jwt", "oauth", "security")),
        ("serialization", ("json", "yaml", "xml", "marshal", "serializ")),
        ("networking", ("network", "socket", "http", "ftp", "smtp", "graphql")),
        ("template", ("template", "render", "view", "html")),
        ("tooling", ("build", "generator", "lint", "parser", "compiler", "codegen")),
        ("devops", ("deploy", "docker", "kubernetes", "cloud", "aws", "azure")),
        ("filesystem", ("file", "filesystem", "path", "archive", "zip")),
        ("data", ("data", "csv", "excel", "statistics", "analytics")),
    ]
    for tag, needles in rules:
        if any(needle in text for needle in needles):
            tags.append(tag)
    return tags[:12] or ["library"]


def version_sort_key(row: tuple[str, str | None]) -> tuple[str, tuple[int, ...]]:
    version, created_at = row
    numbers = tuple(int(part) for part in re.findall(r"\d+", version)[:8])
    return created_at or "", numbers


def render_gem(
    connection: sqlite3.Connection,
    name: str,
) -> str:
    details_row = connection.execute(
        "SELECT details_json FROM gem_details WHERE name = ?", (name,)
    ).fetchone()
    details = json.loads(details_row[0]) if details_row else {}
    versions = connection.execute(
        """
        SELECT version, created_at
        FROM gem_versions
        WHERE name = ?
        """,
        (name,),
    ).fetchall()
    versions.sort(key=version_sort_key, reverse=True)
    latest_version = str(details.get("version") or "").strip()
    if not latest_version and versions:
        latest_version = versions[0][0]

    description = str(
        details.get("info") or details.get("description") or ""
    ).strip()
    tags = derive_tags(name, details)
    encoded = urllib.parse.quote(name, safe="")
    links = unique_links(
        [
            ("主页", details.get("homepage_uri")),
            ("源码仓库", details.get("source_code_uri")),
            ("文档", details.get("documentation_uri")),
            ("更新日志", details.get("changelog_uri")),
            ("问题追踪", details.get("bug_tracker_uri")),
            ("RubyGems", f"https://rubygems.org/gems/{encoded}"),
        ]
    )

    lines = [
        f"# {name}",
        "",
        f"**Tag**: {', '.join(tags)}",
        "",
        "## 简介",
        "",
        description or f"RubyGems 中央仓库中的 Ruby gem {name}。",
        "",
        "## 官网",
        "",
    ]
    lines.extend(f"- {label}: {url}" for label, url in links)
    lines.extend(["", "## 历史版本号", ""])
    if versions:
        for version, created_at in versions:
            suffix = f" ({created_at[:10]})" if created_at else ""
            lines.append(f"- {version}{suffix}")
    else:
        lines.append("(无版本信息)")

    lines.extend(
        [
            "",
            "## 获取地址",
            "",
            f"- RubyGems: https://rubygems.org/gems/{encoded}",
            f"- gem 安装: `gem install {name}`",
            f"- Bundler: `gem \"{name}\"`",
        ]
    )
    if latest_version:
        lines.append(f"- 最新版本: {latest_version}")
        archive_name = f"{name}-{latest_version}.gem"
        lines.append(
            "- 最新版归档: "
            f"https://rubygems.org/downloads/{urllib.parse.quote(archive_name)}"
        )
        if re.match(r"^\d", latest_version):
            lines.append(f"- 版本锁定: `gem \"{name}\", \"~> {latest_version}\"`")
    lines.append("- 中央仓库: https://rubygems.org/")
    lines.append("")
    return "\n".join(lines)


def write_index(
    connection: sqlite3.Connection,
    names: Iterable[str],
) -> dict[int, int]:
    names = list(names)
    components = build_component_map(names)
    counts = {major: 0 for major in MAJORS}
    for index, name in enumerate(names, 1):
        component = components[name]
        markdown = render_gem(connection, name)
        for major in supported_majors(connection, name):
            path = Path(f"ruby-v{major}") / component / f"{component}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(markdown, encoding="utf-8")
            counts[major] += 1
        if index % 1000 == 0:
            print(f"  generated {index}/{len(names)}")
    return counts


def write_readme(counts: dict[int, int], total: int) -> None:
    major_lines = "\n".join(
        f"- `ruby-v{major}`：{counts[major]} 个 gem" for major in MAJORS
    )
    content = f"""# Ruby 库索引

本仓库收录 RubyGems 中央仓库中的 Ruby gem，按 Ruby 大版本与 gem 名称组织。

- 大版本目录：`ruby-v1`、`ruby-v2`、`ruby-v3`、`ruby-v4`
- gem 路径：`<gem>/<gem>.md`
- gem 会根据所有历史版本声明的 `required_ruby_version` 约束，同时出现在兼容的大版本目录中
- 当前共枚举 {total} 个 RubyGems gem

## 收录的中央仓库

| 中央仓库 | 地址 | 说明 |
| --- | --- | --- |
| RubyGems.org | https://rubygems.org/ | Ruby 官方社区 gem 仓库 |
| RubyGems compact index | https://index.rubygems.org/ | 全量 gem 名称、版本和依赖索引 |
| RubyGems API | https://rubygems.org/api/v1/ | gem 详情、项目主页和仓库元数据 |
| Ruby 官网 | https://www.ruby-lang.org/ | Ruby 语言与运行时 |

## 大版本统计

{major_lines}

## 生成方式

```bash
python tools/generate_index.py
```

生成器使用 SQLite 保存名称、版本元数据和 gem 详情缓存，网络中断后可直接续跑。
"""
    Path("README.md").write_text(content, encoding="utf-8")
    for major in MAJORS:
        version_readme = f"""# Ruby v{major} 库索引

- 收录来源：RubyGems compact index 与官方 API
- gem 路径：`<gem>/<gem>.md`
- 当前共收录 {counts[major]} 个 gem
- 版本兼容性根据历史版本的 `required_ruby_version` 约束判定
"""
        Path(f"ruby-v{major}").mkdir(parents=True, exist_ok=True)
        Path(f"ruby-v{major}/README.md").write_text(
            version_readme, encoding="utf-8"
        )


def count_existing(version: str) -> int:
    root = Path(version)
    if not root.exists():
        return 0
    return sum(1 for _ in root.rglob("*.md")) - int((root / "README.md").exists())


def verify(counts: dict[int, int]) -> None:
    for major in MAJORS:
        actual = count_existing(f"ruby-v{major}")
        if actual != counts[major]:
            raise RuntimeError(
                f"ruby-v{major}: generated {counts[major]}, found {actual} files"
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS)
    parser.add_argument(
        "--limit",
        type=int,
        help="only process the first N gem names, useful for a smoke test",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="discard all cached RubyGems metadata and refetch it",
    )
    parser.add_argument(
        "--refresh-names",
        action="store_true",
        help="refresh the gem name list without discarding metadata caches",
    )
    parser.add_argument(
        "--metadata-only",
        action="store_true",
        help="fetch metadata but do not rewrite the markdown index",
    )
    parser.add_argument(
        "--process-pool",
        action="store_true",
        help="use processes for network requests and parsing",
    )
    args = parser.parse_args()

    args.cache.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(args.cache)
    try:
        init_cache(connection)
        names = fetch_names(
            connection, args.refresh or args.refresh_names
        )
        if args.limit is not None:
            names = names[: args.limit]
        fetch_metadata_phase(
            connection,
            names,
            args.workers,
            args.refresh,
            args.process_pool,
        )
        if args.metadata_only:
            print("Metadata cache is complete.")
            return 0
        counts = write_index(connection, names)
        write_readme(counts, len(names))
        verify(counts)
        print(
            "Generated "
            + ", ".join(f"ruby-v{major}={counts[major]}" for major in MAJORS)
        )
        return 0
    finally:
        connection.close()


if __name__ == "__main__":
    raise SystemExit(main())
