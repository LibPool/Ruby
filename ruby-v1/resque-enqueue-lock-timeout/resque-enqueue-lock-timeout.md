# resque-enqueue-lock-timeout

**Tag**: web

## 简介

A Resque plugin. Adds locking, with optional timeout/deadlock handling to
  resque jobs.

  Using a `lock_timeout` allows you to re-aquire the lock should your worker
  fail, crash, or is otherwise unable to relase the lock.

  i.e. Your server unexpectedly looses power. Very handy for jobs that are
  recurring or may be retried.

## 官网

- 主页: http://github.com/saroka/resque-lock-timeout
- RubyGems: https://rubygems.org/gems/resque-enqueue-lock-timeout

## 历史版本号

- 0.4.0 (2012-10-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-enqueue-lock-timeout
- gem 安装: `gem install resque-enqueue-lock-timeout`
- Bundler: `gem "resque-enqueue-lock-timeout"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/resque-enqueue-lock-timeout-0.4.0.gem
- 版本锁定: `gem "resque-enqueue-lock-timeout", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
