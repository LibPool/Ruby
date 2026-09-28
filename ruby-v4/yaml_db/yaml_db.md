# yaml_db

**Tag**: web, database, serialization, data

## 简介

YamlDb is a database-independent format for dumping and restoring data.  It complements the database-independent schema format found in db/schema.rb.  The data is saved into db/data.yml.
This can be used as a replacement for mysqldump or pg_dump, but only for the databases typically used by Rails apps.  Users, permissions, schemas, triggers, and other advanced database features are not supported - by design.
Any database that has an ActiveRecord adapter should work.

## 官网

- 主页: https://github.com/yamldb/yaml_db
- 文档: https://www.rubydoc.info/gems/yaml_db/0.7.0
- RubyGems: https://rubygems.org/gems/yaml_db

## 历史版本号

- 0.7.0 (2018-06-12)
- 0.6.0 (2017-05-21)
- 0.5.0 (2017-03-25)
- 0.4.2 (2016-10-02)
- 0.4.0 (2016-07-10)
- 0.3.0 (2014-11-02)
- 0.2.3 (2012-04-30)
- 0.2.2 (2011-10-12)
- 0.2.1 (2011-04-19)
- 0.2.0 (2010-09-27)
- 0.1.0 (2009-12-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/yaml_db
- gem 安装: `gem install yaml_db`
- Bundler: `gem "yaml_db"`
- 最新版本: 0.7.0
- 最新版归档: https://rubygems.org/downloads/yaml_db-0.7.0.gem
- 版本锁定: `gem "yaml_db", "~> 0.7.0"`
- 中央仓库: https://rubygems.org/
