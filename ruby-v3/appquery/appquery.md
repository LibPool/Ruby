# appquery

**Tag**: web, database, testing, serialization, tooling

## 简介

Improving introspection and testability of raw SQL queries in Rails
This gem improves introspection and testability of raw SQL queries in Rails by:
- ...providing a separate query-folder and easy instantiation  
  A query like `AppQuery[:some_query]` is read from app/queries/some_query.sql.

- ...providing options for rewriting a query:

  Query a CTE by replacing the select:
  query.select_all(select: "select * from some_cte").entries

  ...similarly, query the end result (i.e. CTE `_`):
  query.select_all(select: "select count(*) from _").entries

- ...providing (custom) casting:  
  AppQuery("select array[1,2]").select_value(cast: true)

  custom deserializers:
  AppQuery("select '1' id").select_all(cast: {"id" => ActiveRecord::Type::Integer.new}).entries

- ...providing spec-helpers and generators

## 官网

- 主页: https://github.com/eval/appquery
- 更新日志: https://github.com/eval/appquery/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/appquery

## 历史版本号

- 0.9.0.rc1 (2026-05-27)
- 0.8.0 (2026-01-14)
- 0.8.0.rc3 (2026-01-14)
- 0.8.0.rc2 (2026-01-14)
- 0.8.0.rc1 (2026-01-14)
- 0.7.0 (2026-01-08)
- 0.7.0.rc6 (2026-01-08)
- 0.7.0.rc5 (2026-01-08)
- 0.7.0.rc4 (2026-01-08)
- 0.7.0.rc3 (2026-01-08)
- 0.7.0.rc2 (2026-01-08)
- 0.7.0.rc1 (2026-01-08)
- 0.6.0 (2026-01-02)
- 0.6.0.rc9 (2026-01-02)
- 0.6.0.rc8 (2026-01-02)
- 0.6.0.rc7 (2026-01-02)
- 0.6.0.rc5 (2026-01-01)
- 0.6.0.rc4 (2026-01-01)
- 0.6.0.alpha (2026-01-01)
- 0.5.0 (2025-12-21)
- 0.4.0 (2025-12-15)
- 0.4.0.rc1 (2025-12-15)
- 0.3.0 (2025-06-02)
- 0.2.0 (2024-11-13)
- 0.1.0 (2024-10-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/appquery
- gem 安装: `gem install appquery`
- Bundler: `gem "appquery"`
- 最新版本: 0.8.0
- 最新版归档: https://rubygems.org/downloads/appquery-0.8.0.gem
- 版本锁定: `gem "appquery", "~> 0.8.0"`
- 中央仓库: https://rubygems.org/
