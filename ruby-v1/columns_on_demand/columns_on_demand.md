# columns_on_demand

**Tag**: web, database, testing, data

## 简介

Lazily loads large columns on demand.

By default, does this for all TEXT (:text) and BLOB (:binary) columns, but a list
of specific columns to load on demand can be given.

This is useful to reduce the memory taken by Rails when loading a number of records
that have large columns if those particular columns are actually not required most
of the time.  In this situation it can also greatly reduce the database query time
because loading large BLOB/TEXT columns generally means seeking to other database
pages since they are not stored wholly in the record's page itself.

Although this plugin is mainly used for BLOB and TEXT columns, it will actually
work on all types - and is just as useful for large string fields etc.

## 官网

- 主页: http://github.com/willbryant/columns_on_demand
- 文档: https://www.rubydoc.info/gems/columns_on_demand/6.1.0
- RubyGems: https://rubygems.org/gems/columns_on_demand

## 历史版本号

- 6.1.0 (2024-07-10)
- 6.0.0 (2020-11-12)
- 5.2.0 (2018-01-02)
- 5.1.2 (2018-01-02)
- 5.1.1 (2017-05-09)
- 5.1.0 (2017-04-13)
- 4.3.0 (2016-06-07)
- 4.2.3 (2016-04-04)
- 4.2.2 (2015-07-17)
- 4.2.1.1 (2015-05-17)
- 4.2.1 (2015-05-17)
- 4.2.0 (2014-09-08)
- 4.1.1 (2014-07-16)
- 4.1.0 (2014-07-15)
- 3.0.2 (2013-04-21)
- 3.0.1 (2013-04-20)
- 3.0.0 (2013-04-20)
- 2.0.1 (2012-08-18)
- 2.0.0 (2012-08-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/columns_on_demand
- gem 安装: `gem install columns_on_demand`
- Bundler: `gem "columns_on_demand"`
- 最新版本: 6.1.0
- 最新版归档: https://rubygems.org/downloads/columns_on_demand-6.1.0.gem
- 版本锁定: `gem "columns_on_demand", "~> 6.1.0"`
- 中央仓库: https://rubygems.org/
