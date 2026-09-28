# redis_safe_queue

**Tag**: database

## 简介

RedisSafeQueue is a transactional queue for ruby/redis. It guarantees at least once semantics. The queue may be used with multiple producers and consumers, each job is removed in a open/commit transaction; even if a worker dies while processing a job, it is automatically requeued.

## 官网

- 主页: http://github.com/paulasmuth/redis_safe_queue
- RubyGems: https://rubygems.org/gems/redis_safe_queue

## 历史版本号

- 0.0.1 (2012-11-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/redis_safe_queue
- gem 安装: `gem install redis_safe_queue`
- Bundler: `gem "redis_safe_queue"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/redis_safe_queue-0.0.1.gem
- 版本锁定: `gem "redis_safe_queue", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
