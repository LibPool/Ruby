# jashmenn-redis-lock

**Tag**: web, cli, database, testing

## 简介

Adds pessimistic locking capabilities to the redis gem.
  
  Since these capabilities are utilized client-side, all clients must use this gem and follow the order of lock => make changes => unlock in order to obtain maximum safety when modifying sensitive keys.
  
  Tested with redis-server 2.0.4 and should work with all versions > 0.091.

## 官网

- 主页: http://github.com/PatrickTulskie/redis-lock
- RubyGems: https://rubygems.org/gems/jashmenn-redis-lock

## 历史版本号

- 0.1.1 (2012-05-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/jashmenn-redis-lock
- gem 安装: `gem install jashmenn-redis-lock`
- Bundler: `gem "jashmenn-redis-lock"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/jashmenn-redis-lock-0.1.1.gem
- 版本锁定: `gem "jashmenn-redis-lock", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
