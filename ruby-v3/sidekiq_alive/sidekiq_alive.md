# sidekiq_alive

**Tag**: web, database, networking

## 简介

SidekiqAlive offers a solution to add liveness probe of a Sidekiq instance.

How?

A http server is started and on each requests validates that a liveness key is stored in Redis. If it is there means is working.

A Sidekiq job is the responsable to storing this key. If Sidekiq stops processing jobs
this key gets expired by Redis an consequently the http server will return a 500 error.

This Job is responsible to requeue itself for the next liveness probe.

## 官网

- 主页: https://github.com/arturictus/sidekiq_alive
- 文档: https://github.com/arturictus/sidekiq_alive/blob/v2.5.0/README.md
- 更新日志: https://github.com/arturictus/sidekiq_alive/releases
- 问题追踪: https://github.com/arturictus/sidekiq_alive/issues
- RubyGems: https://rubygems.org/gems/sidekiq_alive

## 历史版本号

- 2.5.0 (2025-05-20)
- 2.4.0 (2024-02-15)
- 2.3.1 (2023-10-17)
- 2.3.0 (2023-09-07)
- 2.2.3 (2023-07-21)
- 2.2.2 (2023-05-25)
- 2.2.1 (2023-05-15)
- 2.2.0 (2023-03-01)
- 2.1.9 (2023-01-11)
- 2.1.8 (2022-12-29)
- 2.1.7 (2022-12-13)
- 2.1.6 (2022-12-07)
- 2.1.5 (2022-04-07)
- 2.1.4 (2021-09-27)
- 2.1.3 (2021-09-27)
- 2.1.2 (2021-07-26)
- 2.1.1 (2021-07-26)
- 2.1.0 (2021-07-09)
- 2.0.6 (2021-04-22)
- 2.0.5 (2021-03-29)
- 2.0.4 (2020-11-04)
- 2.0.3 (2020-08-18)
- 2.0.2 (2020-06-16)
- 2.0.1 (2020-01-03)
- 2.0.0 (2019-09-22)
- 1.2.0 (2019-09-21)
- 1.1.1 (2019-09-20)
- 1.1.0 (2019-01-11)
- 1.0.1 (2019-01-08)
- 1.0.0 (2018-10-08)
- 0.1.1 (2018-08-11)
- 0.1.0 (2018-05-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq_alive
- gem 安装: `gem install sidekiq_alive`
- Bundler: `gem "sidekiq_alive"`
- 最新版本: 2.5.0
- 最新版归档: https://rubygems.org/downloads/sidekiq_alive-2.5.0.gem
- 版本锁定: `gem "sidekiq_alive", "~> 2.5.0"`
- 中央仓库: https://rubygems.org/
