# activerecord-wait_for_lsn

**Tag**: database, data

## 简介

A DatabaseSelector resolver that stores the primary WAL LSN after each write and runs
WAIT FOR LSN on the replica before reading, falling back to the primary on timeout.

## 官网

- 主页: https://github.com/izhanov/activerecord-wait_for_lsn
- RubyGems: https://rubygems.org/gems/activerecord-wait_for_lsn

## 历史版本号

- 0.2.0 (2026-09-04)
- 0.1.0 (2026-09-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/activerecord-wait_for_lsn
- gem 安装: `gem install activerecord-wait_for_lsn`
- Bundler: `gem "activerecord-wait_for_lsn"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/activerecord-wait_for_lsn-0.2.0.gem
- 版本锁定: `gem "activerecord-wait_for_lsn", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
