# capacitor

**Tag**: database

## 简介

Instead of making ActiveRecord calls to change a counter field, write them to capacitor.  They'll get summarized in a redis hash, with a separate process batch-retrieving and writing to ActiveRecord.  Being single-threaded, the writing process avoids row lock collisions, and absorbs traffic spikes by coalescing changes to the same row into one DB write.

## 官网

- 文档: https://www.rubydoc.info/gems/capacitor/1.0.0
- RubyGems: https://rubygems.org/gems/capacitor

## 历史版本号

- 1.0.0 (2013-09-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/capacitor
- gem 安装: `gem install capacitor`
- Bundler: `gem "capacitor"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/capacitor-1.0.0.gem
- 版本锁定: `gem "capacitor", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
