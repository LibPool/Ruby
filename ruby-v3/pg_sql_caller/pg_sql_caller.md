# pg_sql_caller

**Tag**: web, database, testing, serialization, tooling

## 简介

PgSqlCaller is a small, focused wrapper for running raw SQL against PostgreSQL through ActiveRecord. It exposes a stable, documented API on an ActiveRecord-backed class you name, covering the queries the query builder makes awkward: single-scalar and single-column SELECTs, raw rows, ActiveRecord::Result reads, and type-cast (serialized) variants that decode PostgreSQL arrays and custom column types into Ruby objects. Every ? placeholder is bound and escaped through the ActiveRecord sanitizer, so statements stay injection-safe with no manual quoting. On top of that it adds PostgreSQL-specific helpers — non-consuming sequence peeking, table and relation sizes, EXPLAIN ANALYZE, NOTICE capture, and quoting/sanitizing utilities — plus a fast, injection-safe bulk update that partially updates many existing rows in a single UPDATE ... FROM unnest(...) statement and round-trip. The reader API is extensible via define_sql_method, and the gem runs on Ruby 3.2+ with Rails 7.1 through 8.1.

## 官网

- 主页: https://github.com/didww/pg_sql_caller
- RubyGems: https://rubygems.org/gems/pg_sql_caller

## 历史版本号

- 1.2.0 (2026-07-23)
- 1.1.1 (2026-06-23)
- 1.1.0 (2026-06-18)
- 1.0.0 (2026-06-08)
- 0.2.3 (2025-02-07)
- 0.2.2 (2023-02-08)
- 0.2.1 (2023-02-08)
- 0.2.0 (2020-12-23)
- 0.1.0 (2020-03-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/pg_sql_caller
- gem 安装: `gem install pg_sql_caller`
- Bundler: `gem "pg_sql_caller"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/pg_sql_caller-1.2.0.gem
- 版本锁定: `gem "pg_sql_caller", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
