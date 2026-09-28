# ironmin_yaml_db

**Tag**: web, database, serialization, data

## 简介

IronmineYamlDb is a database-independent format for dumping and restoring data.  It complements the the database-independent schema format found in db/schema.rb.  The data is saved into db/data.yml.
This can be used as a replacement for mysqldump or pg_dump, but only for the databases typically used by Rails apps.  Users, permissions, schemas, triggers, and other advanced database features are not supported - by design.
Any database that has an ActiveRecord adapter should work

## 官网

- 主页: http://github.com/uudui/ironmine_yaml_db
- 文档: https://www.rubydoc.info/gems/ironmin_yaml_db/0.0.3
- RubyGems: https://rubygems.org/gems/ironmin_yaml_db

## 历史版本号

- 0.0.3 (2013-07-17)
- 0.0.2 (2013-07-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/ironmin_yaml_db
- gem 安装: `gem install ironmin_yaml_db`
- Bundler: `gem "ironmin_yaml_db"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/ironmin_yaml_db-0.0.3.gem
- 版本锁定: `gem "ironmin_yaml_db", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
