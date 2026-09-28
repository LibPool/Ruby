# multirow_counter

**Tag**: database

## 简介

Typically SQL is not a great place to store a counter that is incremented often. For instance if you're counting the number of visits to a page by incrementing a SQL column and that page gets popular then there's a good chance that the SQL counter will become a benchmark. This is because doing an UPDATE on the row in question locks the row during the course of the UPDATE. So for many concurrent UPDATES there will be lots of lock contention. This gem helps with that.

## 官网

- 主页: http://github.com/Shopify/multirow_counter
- 文档: https://www.rubydoc.info/gems/multirow_counter/0.0.3
- RubyGems: https://rubygems.org/gems/multirow_counter

## 历史版本号

- 0.0.3 (2014-06-23)
- 0.0.2 (2012-07-17)
- 0.0.1 (2012-07-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/multirow_counter
- gem 安装: `gem install multirow_counter`
- Bundler: `gem "multirow_counter"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/multirow_counter-0.0.3.gem
- 版本锁定: `gem "multirow_counter", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
