# stellr

**Tag**: web, cli, tooling, data

## 简介

== FEATURES:  * DRb frontend * easy to use client library (see below) * multi index search * Index rotation Stellr always keeps two versions of your index around - one is used in a multi threaded, read only way to handle incoming search requests, while the other one is written to when you index something. Using the switch function you may decide when to switch over searching from  the old index to the new one. Then, changes will be synced, and searches will see the new or updated data from before the switch call. * Index synchronization Two kinds of synchronization methods are supported for now: rsync, using rsync two copy over the changes from one index to the other, and static, which will completely replace the old index with the new one. While the latter is suitable for indexes which you rebuild completely from time to time, the former is good for large indexes that are updated frequently or that are too large for frequent rebuilds.  == SYNOPSIS:  * start the server:

## 官网

- 文档: https://www.rubydoc.info/gems/stellr/0.1.2
- RubyGems: https://rubygems.org/gems/stellr

## 历史版本号

- 0.1.1 (2009-07-25)
- 0.1.0 (2009-07-25)
- 0.1.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/stellr
- gem 安装: `gem install stellr`
- Bundler: `gem "stellr"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/stellr-0.1.2.gem
- 版本锁定: `gem "stellr", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
