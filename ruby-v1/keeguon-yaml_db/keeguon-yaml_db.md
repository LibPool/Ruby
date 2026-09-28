# keeguon-yaml_db

**Tag**: web, database, serialization, data

## 简介

YamlDb is a database-independent format for dumping and restoring data.  It complements the the database-independent schema format found in db/schema.rb.  The data is saved into db/data.yml.
This can be used as a replacement for mysqldump or pg_dump, but only for the databases typically used by Rails apps.  Users, permissions, schemas, triggers, and other advanced database features are not supported - by design.
Any database that has an ActiveRecord adapter should work

## 官网

- 主页: http://github.com/blanchma/yaml_db
- RubyGems: https://rubygems.org/gems/keeguon-yaml_db

## 历史版本号

- 0.2.4 (2013-03-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/keeguon-yaml_db
- gem 安装: `gem install keeguon-yaml_db`
- Bundler: `gem "keeguon-yaml_db"`
- 最新版本: 0.2.4
- 最新版归档: https://rubygems.org/downloads/keeguon-yaml_db-0.2.4.gem
- 版本锁定: `gem "keeguon-yaml_db", "~> 0.2.4"`
- 中央仓库: https://rubygems.org/
