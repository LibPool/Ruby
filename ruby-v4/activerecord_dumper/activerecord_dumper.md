# activerecord_dumper

**Tag**: web, database, serialization, data

## 简介

ActiveRecordDumper is a fork of YamlDb gem without any explicit Rails dependencies.
This way it can be used by any AR-enabled app (e.g. Sinatra) without pulling whole Rails in.
YamlDB/ActiveRecordDumper is a database-independent format for dumping and restoring data.
It complements the database-independent schema format found in db/schema.rb.
The data is saved into db/data.yml. This can be used as a replacement for mysqldump or pg_dump,
but it only supports features found in ActiveRecord-based (Rails, etc.) apps.
Users, permissions, schemas, triggers, and other advanced database features are not supported by design.
Any database that has an ActiveRecord adapter should work.

## 官网

- 主页: https://github.com/spijet/activerecord_dumper
- 文档: https://www.rubydoc.info/gems/activerecord_dumper/0.9.1
- RubyGems: https://rubygems.org/gems/activerecord_dumper

## 历史版本号

- 0.9.1 (2026-02-09)
- 0.9.0 (2026-02-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/activerecord_dumper
- gem 安装: `gem install activerecord_dumper`
- Bundler: `gem "activerecord_dumper"`
- 最新版本: 0.9.1
- 最新版归档: https://rubygems.org/downloads/activerecord_dumper-0.9.1.gem
- 版本锁定: `gem "activerecord_dumper", "~> 0.9.1"`
- 中央仓库: https://rubygems.org/
