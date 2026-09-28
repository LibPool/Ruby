# redisrpc

**Tag**: web, database, testing, serialization, tooling, data

## 简介

RedisRPC is the easiest to use RPC library in the world. (No small claim!) It
has implementations in Ruby, PHP, and Python.

Redis is a powerful in-memory data structure server that is useful for building
fast distributed systems. Redis implements message queue functionality with its
use of list data structures and the `LPOP`, `BLPOP`, and `RPUSH` commands.
RedisRPC implements a lightweight RPC mechanism using Redis message queues to
temporarily hold RPC request and response messages. These messages are encoded
as JSON strings for portability.

Many other RPC mechanisms are either programming language specific (e.g.
Java RMI) or require boiler-plate code for explicit typing (e.g. Thrift).
RedisRPC was designed to be extremely easy to use by eliminating boiler-plate
code while also being programming language neutral.  High performance was not
an initial goal of RedisRPC and other RPC libraries are likely to have better
performance. Instead, RedisRPC has better programmer performance; it lets you
get something working immediately.

## 官网

- 主页: http://github.com/nfarring/redisrpc
- RubyGems: https://rubygems.org/gems/redisrpc

## 历史版本号

- 0.3.5 (2012-04-20)
- 0.3.4 (2012-04-04)
- 0.3.3 (2012-03-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/redisrpc
- gem 安装: `gem install redisrpc`
- Bundler: `gem "redisrpc"`
- 最新版本: 0.3.5
- 最新版归档: https://rubygems.org/downloads/redisrpc-0.3.5.gem
- 版本锁定: `gem "redisrpc", "~> 0.3.5"`
- 中央仓库: https://rubygems.org/
