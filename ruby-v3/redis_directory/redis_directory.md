# redis_directory

**Tag**: cli, database, data

## 简介

Redis::Directory assumes a Redis installation running on a default
port and database 0 that will contain connection information for various
other Redis databases. For example, if you were using a Redis database to
store the content of cached pages, and this was running on a cluster of
two Redis instances, with multiple applications connecting partitioned by
database, then your connection might look like this:

  require "redis"
  require "redis/distributed"

  # The ACME Corp database is #27
  cache = Redis::Distributed.new "redis://redis.example:4400/27", "redis://redis.example:4401/27"

Redis::Directory uses a centralized Redis database to store the
connection information so you don't have to remember "magic numbers" for
each client/database mapping, and can easily update port-numbers/hostnames,
cluster-members as necessary. The same connection with
Redis::Directory would look like this:

  require "redis_directory"
  
  cache = Redis::Directory.new("redis.example").connect("cache", "acme")

## 官网

- 主页: https://github.com/wiecklabs/redis_directory
- RubyGems: https://rubygems.org/gems/redis_directory

## 历史版本号

- 1.0.4 (2012-03-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/redis_directory
- gem 安装: `gem install redis_directory`
- Bundler: `gem "redis_directory"`
- 最新版本: 1.0.4
- 最新版归档: https://rubygems.org/downloads/redis_directory-1.0.4.gem
- 版本锁定: `gem "redis_directory", "~> 1.0.4"`
- 中央仓库: https://rubygems.org/
