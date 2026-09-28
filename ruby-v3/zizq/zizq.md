# zizq

**Tag**: web, cli, database, testing, networking

## 简介

This is the official Ruby client for the Zizq job queue server.

Zizq is a simple, single binary, zero dependency, language agnostic job queue.

Features:

- Enqueue and process jobs across programming languages
- Persistent/journalled
- Multi-thread and/or multi-fiber
- Scheduled jobs
- Prioritized queues
- Optional ActiveJob integration
- Unique jobs
- Cron scheduling (recurring jobs)
- Job introspection and management, including `jq` filters


This client supports multi-threaded and/or multi-fiber concurrency and is very fast. The Zizq server provides everything needed. There are no separate external storage dependencies to configure such as Redis or a RDBMS.

See https://zizq.io for full details and documentation.

## 官网

- 主页: https://zizq.io
- 源码仓库: https://github.com/zizq-labs/zizq-ruby
- 文档: https://zizq.io/docs/clients/ruby/
- RubyGems: https://rubygems.org/gems/zizq

## 历史版本号

- 0.7.0 (2026-09-10)
- 0.6.0 (2026-08-01)
- 0.5.0 (2026-06-30)
- 0.4.0 (2026-05-31)
- 0.3.7 (2026-05-28)
- 0.3.6 (2026-05-27)
- 0.3.5 (2026-05-27)
- 0.3.4 (2026-05-25)
- 0.3.3 (2026-05-25)
- 0.3.2 (2026-05-24)
- 0.3.1 (2026-05-21)
- 0.3.0 (2026-05-06)
- 0.2.1 (2026-05-02)
- 0.2.0 (2026-04-27)
- 0.1.0 (2026-04-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/zizq
- gem 安装: `gem install zizq`
- Bundler: `gem "zizq"`
- 最新版本: 0.7.0
- 最新版归档: https://rubygems.org/downloads/zizq-0.7.0.gem
- 版本锁定: `gem "zizq", "~> 0.7.0"`
- 中央仓库: https://rubygems.org/
