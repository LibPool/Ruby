# ia-redis-rpc

**Tag**: web, database, testing, serialization, tooling, data

## 简介

RedisRpc is the easiest to use RPC library in the world. (No small claim!).
    This version is a repackage that only has Ruby implementation.

    Redis is a powerful in-memory data structure server that is useful for building
    fast distributed systems. Redis implements message queue functionality with its
    use of list data structures and the `LPOP`, `BLPOP`, and `RPUSH` commands.
    RedisRpc implements a lightweight RPC mechanism using Redis message queues to
    temporarily hold RPC request and response messages. These messages are encoded
    as JSON strings for portability.

    Many other RPC mechanisms are either programming language specific (e.g.
    Java RMI) or require boiler-plate code for explicit typing (e.g. Thrift).
    RedisRpc was designed to be extremely easy to use by eliminating boiler-plate
    code while also being programming language neutral.  High performance was not
    an initial goal of RedisRpc and other RPC libraries are likely to have better
    performance. Instead, RedisRpc has better programmer performance; it lets you
    get something working immediately.

## 官网

- 主页: http://github.com/phuongnd08/redis-rpc-ruby
- 文档: https://www.rubydoc.info/gems/ia-redis-rpc/2.1.0
- RubyGems: https://rubygems.org/gems/ia-redis-rpc

## 历史版本号

- 2.1.0 (2024-02-01)
- 2.0.1.pre.dev (2023-03-30)
- 2.0.0.pre.dev (2023-03-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/ia-redis-rpc
- gem 安装: `gem install ia-redis-rpc`
- Bundler: `gem "ia-redis-rpc"`
- 最新版本: 2.1.0
- 最新版归档: https://rubygems.org/downloads/ia-redis-rpc-2.1.0.gem
- 版本锁定: `gem "ia-redis-rpc", "~> 2.1.0"`
- 中央仓库: https://rubygems.org/
