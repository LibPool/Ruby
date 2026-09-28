# couchproxy

**Tag**: web, cli, database, template, data

## 简介

CouchProxy is a simple proxy server that distributes reads and writes to a
cluster of Apache CouchDB servers so they appear to be a single huge database.
Documents are stored and retrieved from a particular CouchDB instance, using
consistent hashing of the document id. Map/reduce views are processed
concurrently on each CouchDB instance and merged together by the proxy before
returning the results to the client.

## 官网

- 主页: http://github.com/dgraham/couchproxy
- 源码仓库: https://github.com/dgraham/couchproxy
- 问题追踪: https://github.com/dgraham/couchproxy/issues
- RubyGems: https://rubygems.org/gems/couchproxy

## 历史版本号

- 0.2.0 (2011-01-03)
- 0.1.0 (2010-09-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/couchproxy
- gem 安装: `gem install couchproxy`
- Bundler: `gem "couchproxy"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/couchproxy-0.2.0.gem
- 版本锁定: `gem "couchproxy", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
