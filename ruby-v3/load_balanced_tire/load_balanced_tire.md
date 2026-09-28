# load_balanced_tire

**Tag**: web, cli, database, networking, data

## 简介

Tire is a Ruby client for the ElasticSearch search engine/database.

   It provides Ruby-like API for fluent communication with the ElasticSearch server
   and blends with ActiveModel class for convenient usage in Rails applications.

   It allows to delete and create indices, define mapping for them, supports
   the bulk API, and presents an easy-to-use DSL for constructing your queries.

   It has full ActiveRecord/ActiveModel compatibility, allowing you to index
   your models (incrementally upon saving, or in bulk), searching and
   paginating the results.

   Please check the documentation at <http://karmi.github.com/tire/>.

   It has been modified to use the load_balance_client gem instead of the
   rest-client to support multiple elasticsearch servers with failover.

## 官网

- 主页: http://github.com/themattray/tire
- RubyGems: https://rubygems.org/gems/load_balanced_tire

## 历史版本号

- 0.11 (2012-08-08)
- 0.1 (2012-08-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/load_balanced_tire
- gem 安装: `gem install load_balanced_tire`
- Bundler: `gem "load_balanced_tire"`
- 最新版本: 0.11
- 最新版归档: https://rubygems.org/downloads/load_balanced_tire-0.11.gem
- 版本锁定: `gem "load_balanced_tire", "~> 0.11"`
- 中央仓库: https://rubygems.org/
