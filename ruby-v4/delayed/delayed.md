# delayed

**Tag**: database

## 简介

Delayed is a multi-threaded, SQL-driven ActiveJob backend used at Betterment to process millions
of background jobs per day. It supports postgres, mysql, and sqlite, and is designed to be
Reliable (with co-transactional job enqueues and guaranteed, at-least-once execution), Scalable
(with an optimized pickup query and concurrent job execution), Resilient (with built-in retry
mechanisms, exponential backoff, and failed job preservation), and Maintainable (with robust
instrumentation, continuous monitoring, and priority-based alerting).

## 官网

- 主页: http://github.com/betterment/delayed
- 源码仓库: https://github.com/betterment/delayed
- 更新日志: https://github.com/betterment/delayed/releases
- 问题追踪: https://github.com/betterment/delayed/issues
- RubyGems: https://rubygems.org/gems/delayed

## 历史版本号

- 4.1.0 (2026-08-19)
- 4.0.1 (2026-08-13)
- 4.0.0 (2026-08-12)
- 3.1.0 (2026-07-13)
- 3.0.1 (2026-06-15)
- 3.0.0 (2026-06-08)
- 2.2.0 (2026-02-12)
- 2.1.0 (2026-02-05)
- 2.0.3 (2026-02-02)
- 2.0.2 (2026-01-05)
- 2.0.1 (2026-01-05)
- 2.0.0 (2025-12-19)
- 1.2.1 (2025-10-06)
- 1.2.0 (2025-10-03)
- 1.1.0 (2025-09-12)
- 1.0.0 (2025-05-08)
- 0.8.0 (2025-04-03)
- 0.7.2 (2025-04-02)
- 0.7.1 (2025-01-24)
- 0.7.0 (2025-01-15)
- 0.6.0 (2024-12-18)
- 0.5.5 (2024-08-13)
- 0.5.4 (2024-05-01)
- 0.5.3 (2024-01-31)
- 0.5.2 (2023-10-19)
- 0.5.1 (2023-10-11)
- 0.5.0 (2023-01-20)
- 0.4.0 (2021-11-30)
- 0.3.0 (2021-10-26)
- 0.2.0 (2021-09-02)
- 0.1.1 (2021-08-19)
- 0.1.0 (2021-08-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/delayed
- gem 安装: `gem install delayed`
- Bundler: `gem "delayed"`
- 最新版本: 4.1.0
- 最新版归档: https://rubygems.org/downloads/delayed-4.1.0.gem
- 版本锁定: `gem "delayed", "~> 4.1.0"`
- 中央仓库: https://rubygems.org/
