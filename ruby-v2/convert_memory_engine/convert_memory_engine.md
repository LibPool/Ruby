# convert_memory_engine

**Tag**: database, testing, filesystem, data

## 简介

When i use rspec to do a lot of test, each time database is inserted data and truncate table, when tables grows the speed grow down too much. At first i convert the db engine from innodb to memory in db/seed.rb file. After that i write this gem to do the job for more app.
Notice: Tables those contain text col can not convert to memory engine, so i convert those colums to string first. So if there are test case use too long string to insert, there would be trouble.

## 官网

- 主页: http://wangfan.bj.cn
- 文档: https://www.rubydoc.info/gems/convert_memory_engine/1.0.0
- RubyGems: https://rubygems.org/gems/convert_memory_engine

## 历史版本号

- 1.0.0 (2014-08-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/convert_memory_engine
- gem 安装: `gem install convert_memory_engine`
- Bundler: `gem "convert_memory_engine"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/convert_memory_engine-1.0.0.gem
- 版本锁定: `gem "convert_memory_engine", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
