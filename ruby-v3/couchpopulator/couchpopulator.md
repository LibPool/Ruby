# couchpopulator

**Tag**: web, tooling

## 简介

The idea behind this tool is to provide a framework for populating your CouchDB instances with generated documents. It provides a plug-able system for easy writing own generators. Also the the process, which invokes the generator and manages the insertion to CouchDB, what I call execution engines, are easily exchangeable. The default execution engine uses CouchDB's bulk-docs-API with configurable chunk-size, concurrent inserts and total chunks to insert.

## 官网

- 主页: http://github.com/tisba/couchpopulator
- 问题追踪: http://github.com/tisba/couchpopulator/issues
- RubyGems: https://rubygems.org/gems/couchpopulator

## 历史版本号

- 0.2.0 (2009-11-17)
- 0.1.0 (2009-11-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/couchpopulator
- gem 安装: `gem install couchpopulator`
- Bundler: `gem "couchpopulator"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/couchpopulator-0.2.0.gem
- 版本锁定: `gem "couchpopulator", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
