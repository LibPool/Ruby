# activerecord-beagle-turso

**Tag**: database, testing, data

## 简介

An ActiveRecord connection adapter for Turso's libsql engine. It subclasses
the stock SQLite3Adapter and reroutes only the raw-execution seam onto the
beagle-turso native driver, so schema migrations and model CRUD run against
a local, in-memory, or synced remote Turso database while inheriting
SQLite3Adapter's SQL generation, quoting, and schema introspection.

## 官网

- 主页: https://github.com/BeagleSoftwareUK/beagle-turso
- RubyGems: https://rubygems.org/gems/activerecord-beagle-turso

## 历史版本号

- 0.1.4 (2026-08-09)
- 0.1.3 (2026-08-09)
- 0.1.2 (2026-08-08)
- 0.1.1 (2026-08-08)
- 0.1.0 (2026-08-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/activerecord-beagle-turso
- gem 安装: `gem install activerecord-beagle-turso`
- Bundler: `gem "activerecord-beagle-turso"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/activerecord-beagle-turso-0.1.4.gem
- 版本锁定: `gem "activerecord-beagle-turso", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
