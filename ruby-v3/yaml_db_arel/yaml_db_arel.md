# yaml_db_arel

**Tag**: web, database, serialization, data

## 简介

YamlDb is a database-independent format for dumping and restoring data.  It complements the the database-independent schema format found in db/schema.rb.  The data is saved into db/data.yml.
This can be used as a replacement for mysqldump or pg_dump, but only for the databases typically used by Rails apps.  Users, permissions, schemas, triggers, and other advanced database features are not supported - by design.
Any database that has an ActiveRecord adapter should work

## 官网

- 主页: http://github.com/ludicast/yaml_db
- RubyGems: https://rubygems.org/gems/yaml_db_arel

## 历史版本号

- 0.2.2 (2012-02-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/yaml_db_arel
- gem 安装: `gem install yaml_db_arel`
- Bundler: `gem "yaml_db_arel"`
- 最新版本: 0.2.2
- 最新版归档: https://rubygems.org/downloads/yaml_db_arel-0.2.2.gem
- 版本锁定: `gem "yaml_db_arel", "~> 0.2.2"`
- 中央仓库: https://rubygems.org/
