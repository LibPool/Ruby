# schema_ferry

**Tag**: web, cli, database

## 简介

schema_ferry keeps a PostgreSQL schema in sync with a MySQL source during a gradual migration. It reads the MySQL schema through ActiveRecord, converts it to PostgreSQL equivalents — with a declarative DSL for type mappings, enum handling, and per-table overrides — and applies only the diff, idempotently, via ridgepole. Ships a Ruby API and a cron-friendly CLI.

## 官网

- 主页: https://github.com/kyuuri1791/schema_ferry
- 更新日志: https://github.com/kyuuri1791/schema_ferry/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/schema_ferry

## 历史版本号

- 0.3.0 (2026-07-11)
- 0.2.0 (2026-07-06)
- 0.1.3 (2026-07-06)
- 0.1.2 (2026-07-06)
- 0.1.1 (2026-07-06)
- 0.1.0 (2026-07-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/schema_ferry
- gem 安装: `gem install schema_ferry`
- Bundler: `gem "schema_ferry"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/schema_ferry-0.3.0.gem
- 版本锁定: `gem "schema_ferry", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
