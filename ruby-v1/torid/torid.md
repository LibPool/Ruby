# torid

**Tag**: web, database, data

## 简介

Temporally Ordered IDs. Generate universally unique identifiers (UUID) that sort lexically in time order. Torid exists to solve the problem of generating UUIDs that when ordered lexically, they are also ordered temporally. I needed a way to generate ids for events that are entering a system with the following criteria: 1. Fast ID generation 2. No central coordinating server/system 3. No local storage 4. Library code, that is multiple apps on the same machine can use the same code    and they will not generate duplicate ids 5. Eventually stored in a UUID field in a database. So 128bit ids are totally    fine. The IDs that Torid generates are 128bit IDs made up of 2, 64bit parts. * 64bit microsecond level UNIX timestamp * 64bit hash of the system hostname, process id and a random value.

## 官网

- 主页: http://github.com/copiousfreetime/torid
- 文档: https://www.rubydoc.info/gems/torid/1.3.0
- RubyGems: https://rubygems.org/gems/torid

## 历史版本号

- 1.3.0 (2017-02-17)
- 1.2.5 (2016-12-01)
- 1.2.4 (2015-02-18)
- 1.2.3 (2014-09-21)
- 1.2.2 (2014-09-15)
- 1.2.1 (2014-09-13)
- 1.2.0 (2014-09-04)
- 1.1.0 (2014-07-17)
- 1.0.0 (2014-07-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/torid
- gem 安装: `gem install torid`
- Bundler: `gem "torid"`
- 最新版本: 1.3.0
- 最新版归档: https://rubygems.org/downloads/torid-1.3.0.gem
- 版本锁定: `gem "torid", "~> 1.3.0"`
- 中央仓库: https://rubygems.org/
