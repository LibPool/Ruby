# activerecord-trilogy-failover

**Tag**: web, database

## 简介

Handles MySQL ER_OPTION_PREVENTS_STATEMENT (1290) errors by translating them
into ActiveRecord::ConnectionFailed, enabling Rails' built-in retry mechanism
to transparently reconnect. Useful for Aurora failover, ProxySQL, RDS Multi-AZ,
or any MySQL read-only switchover scenario.

## 官网

- 主页: https://github.com/riseshia/activerecord-trilogy-failover
- RubyGems: https://rubygems.org/gems/activerecord-trilogy-failover

## 历史版本号

- 0.1.1 (2026-03-05)
- 0.1.0 (2026-02-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/activerecord-trilogy-failover
- gem 安装: `gem install activerecord-trilogy-failover`
- Bundler: `gem "activerecord-trilogy-failover"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/activerecord-trilogy-failover-0.1.1.gem
- 版本锁定: `gem "activerecord-trilogy-failover", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
