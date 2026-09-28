# associate_jsonb

**Tag**: web, database, serialization, data

## 简介

This gem extends ActiveRecord to add additional functionality to JSONB

- use PostgreSQL JSONB data for associations
- thread-safe single-key updates to JSONB columns using `jsonb_set`
- extended `table#references` for easy migrations and indexes
- virtual JSONB foreign keys using check constraints
  (NOTE: real foreign key constraints are not possible with PostgreSQL JSONB)

Inspired by activerecord-jsonb-associations, but for use in Rails 6+ and
ruby 2.7+ and with some unnecessary options and features (HABTM) removed
and some additional features added

## 官网

- 主页: https://github.com/SampsonCrowley/associate_jsonb
- 文档: https://www.rubydoc.info/gems/associate_jsonb/6.1.4.1.1
- RubyGems: https://rubygems.org/gems/associate_jsonb

## 历史版本号

- 6.1.4.1.1 (2021-09-19)
- 0.0.10 (2020-09-24)
- 0.0.9 (2020-08-13)
- 0.0.8 (2020-08-12)
- 0.0.7 (2020-08-04)
- 0.0.5 (2020-07-21)
- 0.0.4 (2020-07-16)
- 0.0.3 (2020-07-14)
- 0.0.2 (2020-07-14)
- 0.0.1 (2020-07-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/associate_jsonb
- gem 安装: `gem install associate_jsonb`
- Bundler: `gem "associate_jsonb"`
- 最新版本: 6.1.4.1.1
- 最新版归档: https://rubygems.org/downloads/associate_jsonb-6.1.4.1.1.gem
- 版本锁定: `gem "associate_jsonb", "~> 6.1.4.1.1"`
- 中央仓库: https://rubygems.org/
