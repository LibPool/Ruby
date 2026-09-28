# sidekiq-fusebox

**Tag**: web

## 简介

A Sidekiq server middleware that trips an independent circuit breaker per target (extracted from job args, e.g. an integration or hostname), so one flaky downstream service fails fast without starving jobs bound for unrelated targets.

## 官网

- 主页: https://github.com/bhawsartanmay/sidekiq-fusebox
- 源码仓库: https://github.com/bhawsartanmay/sidekiq-fusebox.git
- 更新日志: https://github.com/bhawsartanmay/sidekiq-fusebox/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/bhawsartanmay/sidekiq-fusebox/issues
- RubyGems: https://rubygems.org/gems/sidekiq-fusebox

## 历史版本号

- 0.1.0 (2026-09-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq-fusebox
- gem 安装: `gem install sidekiq-fusebox`
- Bundler: `gem "sidekiq-fusebox"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/sidekiq-fusebox-0.1.0.gem
- 版本锁定: `gem "sidekiq-fusebox", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
