# ocean-dynamo

**Tag**: web, database, networking, devops, data

## 简介

== OceanDynamo

As one important use case for OceanDynamo is to facilitate the conversion of SQL
databases to no-SQL DynamoDB databases, it is important that the syntax and semantics
of OceanDynamo are as close as possible to those of ActiveRecord. This includes
callbacks, exceptions and method chaining semantics. OceanDynamo follows this pattern
closely and is of course based on ActiveModel.


The attribute and persistence layer of OceanDynamo is modeled on that of ActiveRecord:
there's +save+, +save!+, +create+, +update+, +update!+, +update_attributes+, +find_each+,
+destroy_all+, +delete_all+, +read_attribute+, +write_attribute+ and all the other
methods you're used to. The design goal is always to implement as much of the ActiveRecord
interface as possible, without compromising scalability. This makes the task of switching
from SQL to no-SQL much easier.


OceanDynamo uses only primary indices to retrieve related table items and collections,
which means it will scale without limits.


OceanDynamo is fully usable as an ActiveModel and can be used by Rails
controllers. Thanks to its structural similarity to ActiveRecord, OceanDynamo works
with FactoryBot.


See also Ocean, a Rails framework for creating highly scalable SOAs in the cloud, in which
ocean-dynamo is used as a central component: http://wiki.oceanframework.net

## 官网

- 主页: https://gitlab.com/ocean-dev/ocean-dynamo
- 文档: https://www.rubydoc.info/gems/ocean-dynamo/1.9.1
- RubyGems: https://rubygems.org/gems/ocean-dynamo

## 历史版本号

- 1.9.1 (2018-10-12)
- 1.9.0 (2018-10-12)
- 1.8.2 (2018-10-09)
- 1.8.1 (2018-09-02)
- 1.8.0 (2018-09-02)
- 1.7.0 (2018-09-02)
- 1.6.1 (2018-06-28)
- 1.6.0 (2018-06-28)
- 1.5.1 (2018-06-10)
- 1.4.0 (2017-03-12)
- 1.3.1 (2017-03-12)
- 1.3.0 (2015-12-09)
- 1.2.4 (2015-09-19)
- 1.2.3 (2015-09-19)
- 1.2.2 (2015-09-19)
- 1.2.1 (2015-09-18)
- 1.2.0 (2015-09-18)
- 1.1.0 (2015-09-18)
- 1.0.8 (2015-09-17)
- 1.0.7 (2015-09-17)
- 1.0.6 (2015-09-17)
- 1.0.5 (2015-09-17)
- 1.0.4 (2015-09-17)
- 1.0.3 (2015-09-17)
- 1.0.2 (2015-09-16)
- 1.0.1 (2015-09-16)
- 1.0.0 (2015-09-16)
- 0.7.5 (2015-09-10)
- 0.7.4 (2015-05-06)
- 0.7.3 (2015-02-10)
- 0.7.2 (2015-01-07)
- 0.7.1 (2015-01-07)
- 0.7.0 (2015-01-07)
- 0.6.5 (2014-09-16)
- 0.6.4 (2014-09-16)
- 0.6.2 (2014-08-20)
- 0.6.1 (2014-04-16)
- 0.6.0 (2014-04-16)
- 0.5.8 (2014-04-09)
- 0.5.7 (2014-01-10)
- 0.5.6 (2013-12-29)
- 0.5.5 (2013-11-09)
- 0.5.4 (2013-11-09)
- 0.5.3 (2013-10-07)
- 0.5.2 (2013-10-06)
- 0.5.1 (2013-10-03)
- 0.5.0 (2013-10-01)
- 0.4.4 (2013-09-30)
- 0.4.3 (2013-09-30)
- 0.4.2 (2013-09-27)
- 0.4.1 (2013-09-25)
- 0.4.0 (2013-09-16)
- 0.3.13 (2013-09-16)
- 0.3.12 (2013-09-16)
- 0.3.11 (2013-09-16)
- 0.3.10 (2013-09-15)
- 0.3.9 (2013-09-15)
- 0.3.8 (2013-09-15)
- 0.3.7 (2013-09-15)
- 0.3.6 (2013-09-15)
- 0.3.5 (2013-09-15)
- 0.3.4 (2013-09-14)
- 0.3.3 (2013-09-13)
- 0.3.2 (2013-09-13)
- 0.3.1 (2013-09-12)
- 0.3.0 (2013-09-12)
- 0.2.8 (2013-09-12)
- 0.2.7 (2013-09-12)
- 0.2.6 (2013-09-12)
- 0.2.5 (2013-09-12)
- 0.2.4 (2013-09-11)
- 0.2.3 (2013-09-11)
- 0.2.2 (2013-09-11)
- 0.2.1 (2013-09-11)
- 0.2.0 (2013-09-10)
- 0.1.14 (2013-09-10)
- 0.1.13 (2013-09-10)
- 0.1.12 (2013-09-10)
- 0.1.11 (2013-09-10)
- 0.1.10 (2013-09-09)
- 0.1.9 (2013-09-09)
- 0.1.8 (2013-09-07)
- 0.1.7 (2013-09-07)
- 0.1.6 (2013-09-07)
- 0.1.5 (2013-09-07)
- 0.1.4 (2013-09-07)
- 0.1.3 (2013-09-07)
- 0.1.2 (2013-09-07)
- 0.1.1 (2013-09-07)
- 0.1.0 (2013-09-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/ocean-dynamo
- gem 安装: `gem install ocean-dynamo`
- Bundler: `gem "ocean-dynamo"`
- 最新版本: 1.9.1
- 最新版归档: https://rubygems.org/downloads/ocean-dynamo-1.9.1.gem
- 版本锁定: `gem "ocean-dynamo", "~> 1.9.1"`
- 中央仓库: https://rubygems.org/
