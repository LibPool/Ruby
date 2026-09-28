# resque-rate_limited_queue

**Tag**: web

## 简介

A Resque plugin which allows you to create dedicated queues for jobs that use rate limited apis.
These queues will pause when one of the jobs hits a rate limit, and unpause after a suitable time period.
The rate_limited_queue can be used directly, and just requires catching the rate limit exception and pausing the
queue. There are also additional queues provided that already include the pause/rety logic for twitter, angelist
and evernote; these allow you to support rate limited apis with minimal changes.

## 官网

- 主页: http://github.com/pavoni/resque-rate-limited-queue
- 文档: https://www.rubydoc.info/gems/resque-rate_limited_queue/1.2.0
- RubyGems: https://rubygems.org/gems/resque-rate_limited_queue

## 历史版本号

- 1.2.0 (2016-10-07)
- 1.1.0 (2016-10-03)
- 1.0.4 (2016-01-16)
- 1.0.3 (2015-11-06)
- 1.0.2 (2015-01-26)
- 1.0.0 (2014-12-30)
- 0.0.34 (2014-12-28)
- 0.0.33 (2014-12-28)
- 0.0.32 (2014-12-28)
- 0.0.31 (2014-12-28)
- 0.0.30 (2014-12-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-rate_limited_queue
- gem 安装: `gem install resque-rate_limited_queue`
- Bundler: `gem "resque-rate_limited_queue"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/resque-rate_limited_queue-1.2.0.gem
- 版本锁定: `gem "resque-rate_limited_queue", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
