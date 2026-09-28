# sidekiq-alive-next

**Tag**: web, database, networking

## 简介

SidekiqAlive offers a solution to add liveness probe of a Sidekiq instance.

How?

A http server is started and on each requests validates that a liveness key is stored in Redis. If it is there means is working.

A Sidekiq job is the responsable to storing this key. If Sidekiq stops processing jobs
this key gets expired by Redis an consequently the http server will return a 500 error.

This Job is responsible to requeue itself for the next liveness probe.

## 官网

- 主页: https://github.com/andrcuns/sidekiq-alive
- 文档: https://github.com/andrcuns/sidekiq-alive/blob/v3.2.0/README.md
- 更新日志: https://github.com/andrcuns/sidekiq-alive/releases
- 问题追踪: https://github.com/andrcuns/sidekiq-alive/issues
- RubyGems: https://rubygems.org/gems/sidekiq-alive-next

## 历史版本号

- 3.2.0 (2025-04-25)
- 3.1.1 (2022-12-02)
- 3.1.0 (2022-11-02)
- 3.0.0 (2022-10-29)
- 2.2.1 (2022-10-15)
- 2.2.0 (2022-10-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq-alive-next
- gem 安装: `gem install sidekiq-alive-next`
- Bundler: `gem "sidekiq-alive-next"`
- 最新版本: 3.2.0
- 最新版归档: https://rubygems.org/downloads/sidekiq-alive-next-3.2.0.gem
- 版本锁定: `gem "sidekiq-alive-next", "~> 3.2.0"`
- 中央仓库: https://rubygems.org/
