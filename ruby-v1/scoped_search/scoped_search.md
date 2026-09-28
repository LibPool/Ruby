# scoped_search

**Tag**: database, testing, tooling, data

## 简介

Scoped search makes it easy to search your ActiveRecord-based models.

    It will create a named scope :search_for that can be called with a query string. It will build an SQL query using
    the provided query string and a definition that specifies on what fields to search. Because the functionality is
    built on named_scope, the result of the search_for call can be used like any other named_scope, so it can be
    chained with another scope or combined with will_paginate.

    Because it uses standard SQL, it does not require any setup, indexers or daemons. This makes scoped_search
    suitable to quickly add basic search functionality to your application with little hassle. On the other hand,
    it may not be the best choice if it is going to be used on very large datasets or by a large user base.

## 官网

- 主页: https://github.com/wvanbergen/scoped_search/wiki
- 源码仓库: http://github.com/wvanbergen/scoped_search
- 文档: http://rdoc.info/projects/wvanbergen/scoped_search
- 问题追踪: http://github.com/wvanbergen/scoped_search/issues
- RubyGems: https://rubygems.org/gems/scoped_search

## 历史版本号

- 5.0.0 (2026-08-05)
- 4.3.1 (2025-09-30)
- 4.3.0 (2025-09-25)
- 4.2.0 (2025-02-18)
- 4.1.13 (2024-12-03)
- 4.1.12 (2023-10-26)
- 4.1.11 (2023-06-05)
- 4.1.10 (2021-11-29)
- 4.1.9 (2020-08-24)
- 4.1.8 (2020-04-15)
- 4.1.7 (2019-05-07)
- 4.1.6 (2018-11-21)
- 4.1.5 (2018-09-19)
- 4.1.4 (2018-09-06)
- 4.1.3 (2018-03-08)
- 4.1.2 (2017-09-07)
- 4.1.1 (2017-09-05)
- 4.1.0 (2017-03-29)
- 4.0.0 (2016-12-05)
- 3.3.0 (2016-08-09)
- 3.2.2 (2015-07-28)
- 3.2.1 (2015-06-23)
- 3.2.0 (2015-02-23)
- 3.1.0 (2015-01-15)
- 3.0.1 (2014-12-24)
- 3.0.0 (2014-11-21)
- 2.7.1 (2014-03-23)
- 2.7.0 (2014-03-22)
- 2.6.5 (2014-03-10)
- 2.6.4 (2014-03-02)
- 2.6.3 (2014-02-12)
- 2.6.2 (2014-02-10)
- 2.6.1 (2013-12-17)
- 2.6.0 (2013-06-17)
- 2.5.1 (2013-04-02)
- 2.5.0 (2013-03-29)
- 2.4.1 (2013-03-06)
- 2.4.0 (2012-09-11)
- 2.3.7 (2012-04-30)
- 2.3.6 (2011-11-13)
- 2.3.5 (2011-10-18)
- 2.3.4 (2011-10-03)
- 2.3.3 (2011-09-06)
- 2.3.1 (2011-06-22)
- 2.3.0 (2011-05-16)
- 2.2.1 (2010-11-09)
- 2.2.0 (2010-05-26)
- 2.0.1 (2009-10-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/scoped_search
- gem 安装: `gem install scoped_search`
- Bundler: `gem "scoped_search"`
- 最新版本: 5.0.0
- 最新版归档: https://rubygems.org/downloads/scoped_search-5.0.0.gem
- 版本锁定: `gem "scoped_search", "~> 5.0.0"`
- 中央仓库: https://rubygems.org/
