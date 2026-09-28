# balsamique

**Tag**: database, serialization

## 简介

Balsamique (pronounced "Balsami-QUEUE") is a Redis-backed Ruby library
which implements a job queue system.  Balsamique jobs consist of
JSON-encoded args hashes, along with lists of tasks and their
successful outputs.  Jobs can be enqueued to run at some time in the
future, and workers can also delay the running of subsequent tasks.
Retries are automatically scheduled at the time a worker checks out a
job, and cancelled only when the worker reports success.  In contrast
to Resque, Balsamique uses Lua scripting in Redis extensively to make
job state transitions as atomic as possible.

## 官网

- 主页: https://github.com/dwnld/balsamique
- 文档: https://www.rubydoc.info/gems/balsamique/0.1.7
- RubyGems: https://rubygems.org/gems/balsamique

## 历史版本号

- 0.1.7 (2016-02-12)
- 0.1.6 (2016-02-02)
- 0.1.5 (2016-01-20)
- 0.1.4 (2016-01-19)
- 0.1.3 (2016-01-17)
- 0.1.2 (2016-01-15)
- 0.1.1 (2016-01-04)
- 0.1.0 (2015-12-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/balsamique
- gem 安装: `gem install balsamique`
- Bundler: `gem "balsamique"`
- 最新版本: 0.1.7
- 最新版归档: https://rubygems.org/downloads/balsamique-0.1.7.gem
- 版本锁定: `gem "balsamique", "~> 0.1.7"`
- 中央仓库: https://rubygems.org/
