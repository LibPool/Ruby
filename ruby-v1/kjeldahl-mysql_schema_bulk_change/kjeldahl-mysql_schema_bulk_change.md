# kjeldahl-mysql_schema_bulk_change

**Tag**: web, database, testing, networking, template

## 简介

This extension to the MysqlAdapter in ActiveRecord enables bulk updates to schema definitions.  Pr. default when calling connection#add_column the change will be executed a once, but Mysql allows for multiple changes to be executed in one SQL statement (http://dev.mysql.com/doc/refman/5.1/en/alter-table.html). The advantage of this is that it takes a lot less time, especially if the table is large.

## 官网

- 主页: http://github.com/jacob_kjeldahl/mysql_schema_bulk_change
- 文档: https://www.rubydoc.info/gems/kjeldahl-mysql_schema_bulk_change/0.2.0
- RubyGems: https://rubygems.org/gems/kjeldahl-mysql_schema_bulk_change

## 历史版本号

- 0.2.0 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/kjeldahl-mysql_schema_bulk_change
- gem 安装: `gem install kjeldahl-mysql_schema_bulk_change`
- Bundler: `gem "kjeldahl-mysql_schema_bulk_change"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/kjeldahl-mysql_schema_bulk_change-0.2.0.gem
- 版本锁定: `gem "kjeldahl-mysql_schema_bulk_change", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
