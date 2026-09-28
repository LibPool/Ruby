# pg_any_where

**Tag**: database

## 简介

pg_any_where patches Arel so that `where(column: array)` emits
`column = ANY($1::type[])` instead of `column IN ($1, $2, …)`.

This yields a stable prepared-statement shape (one bind parameter regardless
of array size), better PostgreSQL plan cache utilisation, and cleaner
pg_stat_statements output.  Empty arrays are handled correctly without the
`1=0` / `1=1` footguns.

## 官网

- 主页: https://github.com/aimanabutalaah/pg_any_where
- 更新日志: https://github.com/aimanabutalaah/pg_any_where/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/aimanabutalaah/pg_any_where/issues
- RubyGems: https://rubygems.org/gems/pg_any_where

## 历史版本号

- 0.1.0 (2026-06-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/pg_any_where
- gem 安装: `gem install pg_any_where`
- Bundler: `gem "pg_any_where"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pg_any_where-0.1.0.gem
- 版本锁定: `gem "pg_any_where", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
