# ar_after_timestamps

**Tag**: web, database, data

## 简介

Gem that plugs into Ruby on Rails that gives you a way to add a callback to the ActiveRecord callback chain that will be executed right after the record's timestamp columns are set, but before the record is actually saved to the database. This is useful if you want to do something with the timestamps, such as defaulting another time column to created_at, or rolling back a timestamp by a certain amount.

## 官网

- 主页: http://github.com/mcmire/ar_after_timestamps
- RubyGems: https://rubygems.org/gems/ar_after_timestamps

## 历史版本号

- 0.2.0 (2010-01-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/ar_after_timestamps
- gem 安装: `gem install ar_after_timestamps`
- Bundler: `gem "ar_after_timestamps"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/ar_after_timestamps-0.2.0.gem
- 版本锁定: `gem "ar_after_timestamps", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
