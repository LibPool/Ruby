# ractor-rails-shim

**Tag**: web, database

## 简介

ractor-rails-shim makes a Rails application Ractor-safe, so it can run in
Ractor mode — serving requests from worker Ractors that share one frozen
app graph, instead of forking N separate processes.

Rails keeps global state (Rails.application, Rails.cache, Rails.logger,
and every config value set via mattr_accessor / class_attribute) in
class-level instance variables, which Ruby forbids reading or writing from
a non-main Ractor. The shim reroutes those accessors through Ractor-safe
storage (ActiveSupport::IsolatedExecutionState, or Ractor.store_if_absent)
and patches the handful of raw class-ivar accessors Rails reads
per-request.

It is verified against a real Rails 8.1 app (Devise, Propshaft, Kaminari,
PostgreSQL) served by the kino web server in `kino -m ractor` mode.

This is a stopgap: once Rails supports Ractor mode upstream, this gem
becomes a no-op and can be removed.

## 官网

- 主页: https://github.com/DDKatch/ractor-rails-shim
- 更新日志: https://github.com/DDKatch/ractor-rails-shim/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/DDKatch/ractor-rails-shim/issues
- RubyGems: https://rubygems.org/gems/ractor-rails-shim

## 历史版本号

- 0.4.0 (2026-08-15)
- 0.3.1 (2026-08-06)
- 0.3.0 (2026-08-05)
- 0.2.6 (2026-08-04)
- 0.2.5 (2026-07-21)
- 0.2.4 (2026-07-16)
- 0.2.2 (2026-07-16)
- 0.2.1 (2026-07-14)
- 0.2.0 (2026-07-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/ractor-rails-shim
- gem 安装: `gem install ractor-rails-shim`
- Bundler: `gem "ractor-rails-shim"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/ractor-rails-shim-0.4.0.gem
- 版本锁定: `gem "ractor-rails-shim", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
