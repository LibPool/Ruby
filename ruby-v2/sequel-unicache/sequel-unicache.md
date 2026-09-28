# sequel-unicache

**Tag**: database, testing, data

## 简介

Read through caching library inspired by Cache Money, support Sequel 4

Read-Through: Queries by ID or any specified unique key, like `User[params[:id]]` or `User[username: 'bachue@gmail.com']`, will first look in memcache store and then look in the database for the results of that query. If there is a cache miss, it will populate the cache. As objects are created, updated, and deleted, all of the caches are automatically expired.

## 官网

- 主页: https://github.com/bachue/sequel-unicache
- 文档: https://www.rubydoc.info/gems/sequel-unicache/0.9.0
- RubyGems: https://rubygems.org/gems/sequel-unicache

## 历史版本号

- 0.9.0 (2015-02-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/sequel-unicache
- gem 安装: `gem install sequel-unicache`
- Bundler: `gem "sequel-unicache"`
- 最新版本: 0.9.0
- 最新版归档: https://rubygems.org/downloads/sequel-unicache-0.9.0.gem
- 版本锁定: `gem "sequel-unicache", "~> 0.9.0"`
- 中央仓库: https://rubygems.org/
