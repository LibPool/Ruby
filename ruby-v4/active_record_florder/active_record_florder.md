# active_record_florder

**Tag**: web, cli, database, data

## 简介

Floating point ActiveRecord Models ordering for rich client apps heavily inspirated by Trello's ordering alorithm. ActiveRecordFlorder let client decide model's position in collection, normalize given value and resolve conflicts to keep your data clean. It's highly optimalized and generate as small SQL queries. The whole philosophy is to load and update as little records as possible so in 99% it runs just one SELECT and one UPDATE. In edge cases sanitization of all records happens and bring records back to the Garden of Eden state. It's implemented with both Rails and non-Rails apps in mind and highly configurable.

## 官网

- 文档: https://www.rubydoc.info/gems/active_record_florder/0.1.0
- RubyGems: https://rubygems.org/gems/active_record_florder

## 历史版本号

- 0.1.0 (2016-02-01)
- 0.0.1 (2016-01-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/active_record_florder
- gem 安装: `gem install active_record_florder`
- Bundler: `gem "active_record_florder"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/active_record_florder-0.1.0.gem
- 版本锁定: `gem "active_record_florder", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
