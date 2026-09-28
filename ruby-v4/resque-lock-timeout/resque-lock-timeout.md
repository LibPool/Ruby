# resque-lock-timeout

**Tag**: web

## 简介

A Resque plugin. Adds locking, with optional timeout/deadlock handling to
  resque jobs.

  Using a `lock_timeout` allows you to re-acquire the lock should your worker
  fail, crash, or is otherwise unable to relase the lock.
  
  i.e. Your server unexpectedly looses power. Very handy for jobs that are
  recurring or may be retried.

## 官网

- 主页: http://github.com/lantins/resque-lock-timeout
- 文档: http://rdoc.info/projects/lantins/resque-lock-timeout/blob/5823725625bd987569671bae0b177fefabb568dc
- RubyGems: https://rubygems.org/gems/resque-lock-timeout

## 历史版本号

- 0.4.5 (2015-08-04)
- 0.4.4 (2014-02-21)
- 0.4.1 (2012-11-19)
- 0.4.0 (2012-11-09)
- 0.3.3 (2012-03-09)
- 0.3.1 (2011-07-16)
- 0.3.0 (2011-07-16)
- 0.2.1 (2010-06-27)
- 0.2.0 (2010-05-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-lock-timeout
- gem 安装: `gem install resque-lock-timeout`
- Bundler: `gem "resque-lock-timeout"`
- 最新版本: 0.4.5
- 最新版归档: https://rubygems.org/downloads/resque-lock-timeout-0.4.5.gem
- 版本锁定: `gem "resque-lock-timeout", "~> 0.4.5"`
- 中央仓库: https://rubygems.org/
