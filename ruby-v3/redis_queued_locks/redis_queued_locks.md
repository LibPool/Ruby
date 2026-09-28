# redis_queued_locks

**Tag**: database, data

## 简介

|> Distributed locks with "prioritized lock acquisition queue" capabilities based on the Redis Database.
|> Each lock request is put into the request queue (each lock is hosted by its own queue separately from other queues) and processed in order of their priority (FIFO).
|> Each lock request lives some period of time (RTTL) (with requeue capabilities) which guarantees the request queue will never be stacked.
|> In addition to the classic `queued` (FIFO) strategy RQL supports `random` (RANDOM) lock obtaining strategy when any acquirer from the lock queue can obtain the lock regardless the position in the queue.
|> Provides flexible invocation flow, parametrized limits (lock request ttl, lock ttl, queue ttl, lock attempts limit, fast failing, etc), logging and instrumentation.

## 官网

- 主页: https://github.com/0exp/redis_queued_locks
- 源码仓库: https://github.com/0exp/redis_queued_locks/blob/master
- 更新日志: https://github.com/0exp/redis_queued_locks/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/redis_queued_locks

## 历史版本号

- 1.16.2 (2026-02-05)
- 1.16.1 (2026-01-28)
- 1.16.0 (2026-01-27)
- 1.15.1 (2025-10-22)
- 1.15.0 (2025-10-17)
- 1.14.0 (2025-10-17)
- 1.13.0 (2025-06-07)
- 1.12.1 (2024-09-25)
- 1.12.0 (2024-08-11)
- 1.11.0 (2024-08-11)
- 1.10.0 (2024-08-11)
- 1.9.0 (2024-07-15)
- 1.8.0 (2024-06-13)
- 1.7.0 (2024-06-12)
- 1.6.0 (2024-05-25)
- 1.5.0 (2024-05-23)
- 1.4.0 (2024-05-13)
- 1.3.1 (2024-05-10)
- 1.3.0 (2024-05-08)
- 1.2.0 (2024-04-27)
- 1.1.0 (2024-04-02)
- 1.0.0 (2024-04-01)
- 0.0.40 (2024-03-31)
- 0.0.39 (2024-03-31)
- 0.0.38 (2024-03-28)
- 0.0.37 (2024-03-28)
- 0.0.36 (2024-03-28)
- 0.0.35 (2024-03-26)
- 0.0.34 (2024-03-26)
- 0.0.33 (2024-03-25)
- 0.0.32 (2024-03-25)
- 0.0.30 (2024-03-23)
- 0.0.29 (2024-03-23)
- 0.0.28 (2024-03-21)
- 0.0.27 (2024-03-21)
- 0.0.26 (2024-03-21)
- 0.0.25 (2024-03-21)
- 0.0.24 (2024-03-21)
- 0.0.23 (2024-03-21)
- 0.0.22 (2024-03-21)
- 0.0.21 (2024-03-19)
- 0.0.20 (2024-03-14)
- 0.0.19 (2024-03-12)
- 0.0.18 (2024-03-04)
- 0.0.17 (2024-02-29)
- 0.0.16 (2024-02-29)
- 0.0.15 (2024-02-28)
- 0.0.14 (2024-02-27)
- 0.0.13 (2024-02-27)
- 0.0.12 (2024-02-27)
- 0.0.11 (2024-02-27)
- 0.0.10 (2024-02-27)
- 0.0.9 (2024-02-27)
- 0.0.8 (2024-02-27)
- 0.0.7 (2024-02-26)
- 0.0.6 (2024-02-26)
- 0.0.5 (2024-02-26)
- 0.0.4 (2024-02-26)
- 0.0.3 (2024-02-26)
- 0.0.2 (2024-02-26)
- 0.0.1 (2024-02-26)
- 0.0.0 (2024-02-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/redis_queued_locks
- gem 安装: `gem install redis_queued_locks`
- Bundler: `gem "redis_queued_locks"`
- 最新版本: 1.16.2
- 最新版归档: https://rubygems.org/downloads/redis_queued_locks-1.16.2.gem
- 版本锁定: `gem "redis_queued_locks", "~> 1.16.2"`
- 中央仓库: https://rubygems.org/
