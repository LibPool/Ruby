# idempotency_check

**Tag**: database, data

## 简介

idempotency_check runs a block of code multiple times and compares the
side effects it produces (database rows, ActionMailer deliveries,
ActiveJob enqueue/perform activity, and optionally Sidekiq) to detect
jobs that aren't safe to retry or re-run. It works on any block of Ruby
code, not just jobs, and has no runtime dependencies of its own.

## 官网

- 主页: https://github.com/AFornio/idempotency_check
- 问题追踪: https://github.com/AFornio/idempotency_check/issues
- RubyGems: https://rubygems.org/gems/idempotency_check

## 历史版本号

- 0.1.0 (2026-07-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/idempotency_check
- gem 安装: `gem install idempotency_check`
- Bundler: `gem "idempotency_check"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/idempotency_check-0.1.0.gem
- 版本锁定: `gem "idempotency_check", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
