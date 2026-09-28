# redis_dedupe

**Tag**: database, security

## 简介

This is a weak deduper to make things like bulk email run safer. It is not a lock safe for financial/security needs because it uses a weak redis locking pattern that can have race conditions. However, imagine a bulk email job that loops over 100 users, and enqueues a background email for each user. If the job fails at iteration 50, a retry would enqueue all the users again and many will receive dupes. This would continue multiple times as the parent job continued to rerun. By marking that a subjob has been enqueued, we can let that isolated job handle its own failures, and the batch enqueue job can run multiple times without re-enqueueing the same subjobs.

## 官网

- 文档: https://www.rubydoc.info/gems/redis_dedupe/1.0.0
- RubyGems: https://rubygems.org/gems/redis_dedupe

## 历史版本号

- 1.0.0 (2025-06-30)
- 0.0.6 (2024-10-22)
- 0.0.5 (2023-09-28)
- 0.0.4 (2022-01-21)
- 0.0.3 (2016-08-10)
- 0.0.2 (2015-03-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/redis_dedupe
- gem 安装: `gem install redis_dedupe`
- Bundler: `gem "redis_dedupe"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/redis_dedupe-1.0.0.gem
- 版本锁定: `gem "redis_dedupe", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
