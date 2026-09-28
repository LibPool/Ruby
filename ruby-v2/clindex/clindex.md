# clindex

**Tag**: web, cli

## 简介

A generic index DRb server. The core index is a hash, each key is an individual term, each value is an array of references for that term. Searches the index with a simple regexp grep against the hash keys to return a single array of all references on matching terms. Multi-user ready via a simple locking mechanism that probably doesn't scale too well. BSD License.

## 官网

- 主页: https://github.com/chrismo/clindex
- 文档: https://www.rubydoc.info/gems/clindex/2.0.1
- RubyGems: https://rubygems.org/gems/clindex

## 历史版本号

- 2.0.1 (2023-11-22)
- 2.0.0 (2019-01-03)
- 1.2.1 (2012-12-20)
- 1.2.0 (2011-05-22)
- 1.1.0 (2011-05-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/clindex
- gem 安装: `gem install clindex`
- Bundler: `gem "clindex"`
- 最新版本: 2.0.1
- 最新版归档: https://rubygems.org/downloads/clindex-2.0.1.gem
- 版本锁定: `gem "clindex", "~> 2.0.1"`
- 中央仓库: https://rubygems.org/
