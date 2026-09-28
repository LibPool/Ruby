# sidekiq-locking

**Tag**: web, database, data

## 简介

sidekiq-locking keeps only the first copy of a job in Redis while a
short-lived lock is active. A duplicate enqueue for the same lock context
(class, queue, args by default) is skipped until the original job succeeds
or the lock_for TTL expires — whichever comes first. It is deliberately
best-effort enqueue coalescing, not a correctness primitive or a runtime
mutex: jobs must still be idempotent and protect true uniqueness with
database constraints/locks where required. Opt a job in with
`sidekiq_options lock_for: 5.minutes`; customize the dedup scope with a
`lock_args` class method. No Rails or ActiveSupport required.

## 官网

- 主页: https://github.com/neetozone/sidekiq-locking
- RubyGems: https://rubygems.org/gems/sidekiq-locking

## 历史版本号

- 0.1.0 (2026-09-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq-locking
- gem 安装: `gem install sidekiq-locking`
- Bundler: `gem "sidekiq-locking"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/sidekiq-locking-0.1.0.gem
- 版本锁定: `gem "sidekiq-locking", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
