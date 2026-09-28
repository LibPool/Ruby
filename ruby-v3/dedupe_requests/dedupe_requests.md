# dedupe_requests

**Tag**: web, cli, database

## 简介

Detects and rejects duplicate inbound POST/PUT/PATCH requests with a 409/conflict, with no client-side idempotency key required. The server auto-computes a fingerprint of each mutating request, claims it atomically in Redis, and short-circuits duplicates seen within a configurable time window, so they don't overwhelm your server or cause 5xx errors.

## 官网

- 主页: https://github.com/tilo/dedupe_requests
- 更新日志: https://github.com/tilo/dedupe_requests/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/dedupe_requests

## 历史版本号

- 1.0.0 (2026-06-24)
- 1.0.0.pre1 (2026-06-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/dedupe_requests
- gem 安装: `gem install dedupe_requests`
- Bundler: `gem "dedupe_requests"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/dedupe_requests-1.0.0.gem
- 版本锁定: `gem "dedupe_requests", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
