# active_job_lock

**Tag**: web

## 简介

An ActiveJob plugin. Adds locking, with optional timeout/deadlock handling.

  Using a `lock_timeout` allows you to re-acquire the lock should your job
  fail, crash, or is otherwise unable to relase the lock.

  i.e. Your server unexpectedly looses power. Very handy for jobs that are
  recurring or may be retried.

## 官网

- 主页: http://github.com/dferrazm/active_job_lock
- 文档: https://www.rubydoc.info/gems/active_job_lock/0.1.0
- RubyGems: https://rubygems.org/gems/active_job_lock

## 历史版本号

- 0.1.0 (2016-07-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/active_job_lock
- gem 安装: `gem install active_job_lock`
- Bundler: `gem "active_job_lock"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/active_job_lock-0.1.0.gem
- 版本锁定: `gem "active_job_lock", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
