# yaml_db_improved

**Tag**: web, database, serialization, data

## 简介

YamlDb is a database-independent format for dumping and restoring data.  It complements the the database-independent schema format found in db/schema.rb.  The data is saved into db/data.yml.
This can be used as a replacement for mysqldump or pg_dump, but only for the databases typically used by Rails apps.  Users, permissions, schemas, triggers, and other advanced database features are not supported - by design.
Any database that has an ActiveRecord adapter should work

## 官网

- 主页: http://github.com/zoltankiss/yaml_db
- 文档: https://www.rubydoc.info/gems/yaml_db_improved/1.0.1
- RubyGems: https://rubygems.org/gems/yaml_db_improved

## 历史版本号

- 1.0.1 (2014-10-06)
- 1.0.0 (2014-09-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/yaml_db_improved
- gem 安装: `gem install yaml_db_improved`
- Bundler: `gem "yaml_db_improved"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/yaml_db_improved-1.0.1.gem
- 版本锁定: `gem "yaml_db_improved", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
