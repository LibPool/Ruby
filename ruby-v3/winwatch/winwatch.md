# winwatch

**Tag**: web, cli, networking, filesystem

## 简介

winwatch watches a directory (optionally a whole subtree) with a single
overlapped ReadDirectoryChangesW operation and delivers :added/:modified/
:removed/:renamed events with absolute UTF-8 paths. Kernel buffer overflow is
surfaced as an explicit :rescan event (never silently dropped) and a dying
watch (root deleted, network loss) as a terminal :gone event. Blocking pulls
release the GVL and are interrupt-safe; under the winloop fiber scheduler the
watcher parks fibers on the loop's completion port with zero extra threads.

Public API: Winwatch.watch(path, recursive:, filter:, buffer_size:,
normalize_names:) with a block form, Watcher#take/#each/#close, and a frozen
Winwatch::Event struct. Windows MSVC (mswin) Ruby only.

## 官网

- 主页: https://github.com/main-path/winwatch
- 更新日志: https://github.com/main-path/winwatch/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/winwatch/issues
- RubyGems: https://rubygems.org/gems/winwatch

## 历史版本号

- 0.1.0 (2026-06-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/winwatch
- gem 安装: `gem install winwatch`
- Bundler: `gem "winwatch"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/winwatch-0.1.0.gem
- 版本锁定: `gem "winwatch", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
