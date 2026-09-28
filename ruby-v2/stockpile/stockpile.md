# stockpile

**Tag**: web, database, networking

## 简介

Stockpile is a simple key-value store connection manager framework. Stockpile
itself does not implement a connection manager, but places expectations for
implemented connection managers. So far, only Redis has been implemented
(stockpile-redis).

Stockpile also provides an adapter so that its functionality can be accessed
from within a module.

Release 2.0 fixes an issue when Stockpile options are provided with an
OpenStruct, originally reported as
{stockpile-redis#1}[https://github.com/halostatue/stockpile-redis/issues/1].
Support for Ruby 1.9 has been dropped.

## 官网

- 主页: https://github.com/halostatue/stockpile/
- 文档: https://www.rubydoc.info/gems/stockpile/2.0
- RubyGems: https://rubygems.org/gems/stockpile

## 历史版本号

- 2.0 (2016-04-05)
- 1.1 (2015-02-10)
- 1.0 (2015-01-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/stockpile
- gem 安装: `gem install stockpile`
- Bundler: `gem "stockpile"`
- 最新版本: 2.0
- 最新版归档: https://rubygems.org/downloads/stockpile-2.0.gem
- 版本锁定: `gem "stockpile", "~> 2.0"`
- 中央仓库: https://rubygems.org/
