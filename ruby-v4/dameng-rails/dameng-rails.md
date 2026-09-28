# dameng-rails

**Tag**: web, database, testing, template

## 简介

DM8 has no Ruby driver or ActiveRecord adapter. dm-rails keeps the stock mysql2 adapter and routes it through ShardingSphere-Proxy to DM8, patching ActiveRecord schema introspection (SHOW FULL FIELDS / information_schema) with a DM-side helper view. Battle-tested on a production Rails 7.1 system.

## 官网

- 主页: https://github.com/qinyuanmao/dm-rails
- RubyGems: https://rubygems.org/gems/dameng-rails

## 历史版本号

- 0.1.2 (2026-07-31)
- 0.1.1 (2026-07-31)
- 0.1.0 (2026-07-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/dameng-rails
- gem 安装: `gem install dameng-rails`
- Bundler: `gem "dameng-rails"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/dameng-rails-0.1.2.gem
- 版本锁定: `gem "dameng-rails", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
