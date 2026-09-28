# chimera

**Tag**: web, database, testing, data

## 简介

Chimera is an object mapper for Riak and Redis. The idea is to mix the advantages of Riak
(scalability, massive data storage) with Redis (atomicity, performance, data structures).
You should store the bulk of your data in Riak, and then use Redis data structures where
appropriate (for example, a counter or set of keys).

Internally, Chimera uses Redis for any indexes you define as well as some default indexes
that are automatically created. There's no built in sharding for Redis, but since it's
only being used for key storage and basic data elements you should be able to go a long
way with one Redis server (especially if you use the new Redis VM).

!! Chimera is alpha. It's not production tested and needs a better test suite. !!
!! It's also only tested in Ruby 1.9. !!

## 官网

- 主页: http://github.com/benmyles/chimera
- 文档: http://wiki.github.com/benmyles/chimera/
- 问题追踪: http://github.com/benmyles/chimera/issues
- RubyGems: https://rubygems.org/gems/chimera

## 历史版本号

- 0.0.4 (2010-03-08)
- 0.0.3 (2010-03-06)
- 0.0.2 (2010-03-06)
- 0.0.1 (2010-03-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/chimera
- gem 安装: `gem install chimera`
- Bundler: `gem "chimera"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/chimera-0.0.4.gem
- 版本锁定: `gem "chimera", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
