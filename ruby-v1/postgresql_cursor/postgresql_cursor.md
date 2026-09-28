# postgresql_cursor

**Tag**: database, data

## 简介

PostgreSQL Cursor is an extension to the ActiveRecord PostgreSQLAdapter for
  very large result sets.  It provides a cursor open/fetch/close interface to
  access data without loading all rows into memory, and instead loads the result
  rows in 'chunks' (default of 1_000 rows), buffers them, and returns the rows
  one at a time.

## 官网

- 主页: http://github.com/afair/postgresql_cursor
- 文档: https://www.rubydoc.info/gems/postgresql_cursor/0.6.11
- RubyGems: https://rubygems.org/gems/postgresql_cursor

## 历史版本号

- 0.6.11 (2026-07-15)
- 0.6.10 (2026-04-08)
- 0.6.9 (2024-06-03)
- 0.6.8 (2023-01-18)
- 0.6.7 (2023-01-10)
- 0.6.6 (2022-10-31)
- 0.6.5 (2022-10-29)
- 0.6.4 (2019-10-03)
- 0.6.3 (2019-09-30)
- 0.6.2 (2018-09-08)
- 0.6.1 (2016-09-02)
- 0.6.0 (2016-02-22)
- 0.5.1 (2014-09-11)
- 0.5.0 (2014-06-26)
- 0.4.3 (2014-06-06)
- 0.4.2 (2013-02-20)
- 0.4.1 (2013-02-20)
- 0.4.0 (2012-07-21)
- 0.3.1 (2010-08-06)
- 0.3.0 (2010-07-29)
- 0.2.0 (2010-05-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/postgresql_cursor
- gem 安装: `gem install postgresql_cursor`
- Bundler: `gem "postgresql_cursor"`
- 最新版本: 0.6.11
- 最新版归档: https://rubygems.org/downloads/postgresql_cursor-0.6.11.gem
- 版本锁定: `gem "postgresql_cursor", "~> 0.6.11"`
- 中央仓库: https://rubygems.org/
