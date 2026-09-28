# scryer

**Tag**: web, database, security, serialization, template, tooling, filesystem, data

## 简介

Scryer is an all-in-one security auditing and static analysis tool for Ruby on Rails
applications — tells you what to fix first, across security, performance, dependencies, and
code quality. It scans a Ruby/Rails codebase for security vulnerabilities, performance
problems, dependency risk, and code-quality issues, then ranks everything it finds by severity
across all of those categories — so a scan ends with one answer to "what's most worth fixing,"
not four separate reports to reconcile by hand. (Style/lint is RuboCop's job — Scryer doesn't
touch that, except one narrow check.)

Detects SQL injection, mass assignment, SSRF, path traversal, IDOR, insecure JWT/CORS/session
config, hardcoded secrets, XSS, weak crypto, and more; N+1 queries, missing pagination, and
other performance heuristics; near-duplicate code; and known-vulnerable gems via a live
OSV.dev dependency audit — on by default, every run.

Every finding includes a human-reviewable suggested fix — never auto-applied, optionally
rewritten against your actual code by any LLM you configure. Reports in JSON, self-contained
HTML, CSV, or SARIF (for GitHub Code Scanning). Zero runtime dependencies beyond Ruby's own
stdlib.

## 官网

- 主页: https://ramlaxmanyadav.github.io/scryer/
- 源码仓库: https://github.com/ramlaxmanyadav/scryer
- 更新日志: https://github.com/ramlaxmanyadav/scryer/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/ramlaxmanyadav/scryer/issues
- RubyGems: https://rubygems.org/gems/scryer

## 历史版本号

- 1.3.0 (2026-09-21)
- 1.2.2 (2026-09-12)
- 1.2.1 (2026-09-04)
- 1.2.0 (2026-08-16)
- 1.1.1 (2026-08-14)
- 1.0.0 (2026-08-12)
- 0.3.0 (2026-08-11)
- 0.2.0 (2026-08-11)
- 0.1.0 (2026-08-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/scryer
- gem 安装: `gem install scryer`
- Bundler: `gem "scryer"`
- 最新版本: 1.3.0
- 最新版归档: https://rubygems.org/downloads/scryer-1.3.0.gem
- 版本锁定: `gem "scryer", "~> 1.3.0"`
- 中央仓库: https://rubygems.org/
