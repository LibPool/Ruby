# activerecord-duplicator

**Tag**: web

## 简介

activerecord-duplicator copies an ActiveRecord record and its associated rows
(has_many, has_one, belongs_to, has_many :through) in one call. It rewires
foreign keys through an internal id map, bypasses callbacks by using
insert_all!, and lets you plug in per-model handlers for records that need
custom logic. Composite primary keys (Rails 7.1+) are supported.

## 官网

- 主页: https://github.com/kufu/activerecord-duplicator
- 更新日志: https://github.com/kufu/activerecord-duplicator/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/activerecord-duplicator

## 历史版本号

- 0.6.0 (2026-07-08)
- 0.5.0 (2026-07-07)
- 0.4.0 (2026-07-06)
- 0.3.0 (2026-07-06)
- 0.2.0 (2026-07-06)
- 0.1.0 (2026-07-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/activerecord-duplicator
- gem 安装: `gem install activerecord-duplicator`
- Bundler: `gem "activerecord-duplicator"`
- 最新版本: 0.6.0
- 最新版归档: https://rubygems.org/downloads/activerecord-duplicator-0.6.0.gem
- 版本锁定: `gem "activerecord-duplicator", "~> 0.6.0"`
- 中央仓库: https://rubygems.org/
