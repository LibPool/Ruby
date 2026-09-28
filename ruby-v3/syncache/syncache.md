# syncache

**Tag**: data

## 简介

SynCache stores cached objects in a Hash that is protected by an advanced
two-level locking mechanism which ensures that:

 * Multiple threads can add and fetch objects in parallel.
 * While one thread is working on a cache entry, other threads can access
   the rest of the cache with no waiting on the global lock, no race
   conditions nor deadlock or livelock situations.
 * While one thread is performing a long and resource-intensive
   operation, other threads that request the same data will be put on hold,
   and as soon as the first thread completes the operation, the result will be
   returned to all threads.

## 官网

- 主页: https://github.com/angdraug/syncache
- 文档: https://www.rubydoc.info/gems/syncache/1.4
- RubyGems: https://rubygems.org/gems/syncache

## 历史版本号

- 1.4 (2016-04-16)
- 1.3 (2016-02-15)
- 1.2 (2012-10-13)
- 1.0.0 (2010-05-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/syncache
- gem 安装: `gem install syncache`
- Bundler: `gem "syncache"`
- 最新版本: 1.4
- 最新版归档: https://rubygems.org/downloads/syncache-1.4.gem
- 版本锁定: `gem "syncache", "~> 1.4"`
- 中央仓库: https://rubygems.org/
