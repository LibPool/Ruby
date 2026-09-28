# pg_pipeline

**Tag**: database

## 简介

A driver-adjacent Ruby control-plane over ruby-pg/libpq. It multiplexes
independent, session-neutral extended-protocol operations from many fibers
onto a small number of PostgreSQL connections while keeping explicit
transactions and session-changing work on exclusive pinned connections.
Requires any Fiber::Scheduler host (Async::Scheduler, Itsi::Scheduler, …);
the gem does not depend on a particular reactor. Control-plane only: all
wire work stays in libpq.

## 官网

- 主页: https://github.com/roman-haidarov/pg_pipeline
- 源码仓库: https://github.com/roman-haidarov/pg_pipeline/tree/main
- 更新日志: https://github.com/roman-haidarov/pg_pipeline/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/roman-haidarov/pg_pipeline/issues
- RubyGems: https://rubygems.org/gems/pg_pipeline

## 历史版本号

- 0.3.3 (2026-08-19)
- 0.3.2 (2026-08-17)
- 0.3.1 (2026-08-09)
- 0.3.0 (2026-08-08)
- 0.2.5 (2026-08-03)
- 0.2.4 (2026-07-31)
- 0.2.3 (2026-07-30)
- 0.2.2 (2026-07-30)
- 0.2.1 (2026-07-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/pg_pipeline
- gem 安装: `gem install pg_pipeline`
- Bundler: `gem "pg_pipeline"`
- 最新版本: 0.3.3
- 最新版归档: https://rubygems.org/downloads/pg_pipeline-0.3.3.gem
- 版本锁定: `gem "pg_pipeline", "~> 0.3.3"`
- 中央仓库: https://rubygems.org/
