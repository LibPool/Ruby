# resque-rate_limited

**Tag**: web

## 简介

A Resque plugin which allows you to create dedicated queues for jobs that use rate-limited APIs. These queues will pause when one of the jobs hits a rate limit, and unpause after a suitable time period. The rate-limited queue can be used directly, and just requires catching the rate limit exception and pausing the queue. There are also additional queues provided that already include the pause/retry logic for Twitter, AngelList and Evernote; these allow you to support rate-limited APIs with minimal changes.

## 官网

- 主页: http://github.com/Xenapto/resque-rate_limited
- 文档: https://www.rubydoc.info/gems/resque-rate_limited/1.2.4
- RubyGems: https://rubygems.org/gems/resque-rate_limited

## 历史版本号

- 1.2.4 (2017-04-26)
- 1.2.3 (2017-04-26)
- 1.2.2 (2017-04-26)
- 1.2.0 (2016-10-07)
- 1.1.0 (2016-10-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-rate_limited
- gem 安装: `gem install resque-rate_limited`
- Bundler: `gem "resque-rate_limited"`
- 最新版本: 1.2.4
- 最新版归档: https://rubygems.org/downloads/resque-rate_limited-1.2.4.gem
- 版本锁定: `gem "resque-rate_limited", "~> 1.2.4"`
- 中央仓库: https://rubygems.org/
