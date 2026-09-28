# dm-adapter-simpledb

**Tag**: data

## 简介

A DataMapper adapter for Amazon's SimpleDB service. 

Features:
 * Full set of CRUD operations
 * Supports all DataMapper query predicates.
 * Can translate many queries into efficient native SELECT operations.
 * Migrations
 * DataMapper identity map support for record caching
 * Lazy-loaded attributes
 * DataMapper Serial property support via UUIDs.
 * Array properties
 * Basic aggregation support (Model.count("..."))
 * String "chunking" permits attributes to exceed the 1024-byte limit

Note: as of version 1.0.0, this gem supports supports the DataMapper 0.10.*
series and breaks backwards compatibility with DataMapper 0.9.*.

## 官网

- 主页: http://github.com/devver/dm-adapter-simpledb
- RubyGems: https://rubygems.org/gems/dm-adapter-simpledb

## 历史版本号

- 1.5.0 (2010-01-26)
- 1.4.0 (2010-01-24)
- 1.3.0 (2010-01-19)
- 1.2.0 (2010-01-13)
- 1.1.0 (2009-11-25)
- 1.0.0 (2009-11-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/dm-adapter-simpledb
- gem 安装: `gem install dm-adapter-simpledb`
- Bundler: `gem "dm-adapter-simpledb"`
- 最新版本: 1.5.0
- 最新版归档: https://rubygems.org/downloads/dm-adapter-simpledb-1.5.0.gem
- 版本锁定: `gem "dm-adapter-simpledb", "~> 1.5.0"`
- 中央仓库: https://rubygems.org/
