# prune_ar

**Tag**: database, data

## 简介

Given an initial set of records to delete prune_ar deletes all other records (accessible via ActiveRecord) that are now orphaned due to a belongs_to relation which is now non-existent. This allows you to safely delete records that you want to delete without creating orphaned records in another table (& without violating foreign key constraints if you use them). This can be used to prune a production database (given deletion criteria for top level parent-less independent entities) for use in a development environment without compromising customer data.

## 官网

- 主页: https://github.com/contently/prune_ar
- 文档: https://www.rubydoc.info/gems/prune_ar/0.1.0
- RubyGems: https://rubygems.org/gems/prune_ar

## 历史版本号

- 0.1.0 (2018-12-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/prune_ar
- gem 安装: `gem install prune_ar`
- Bundler: `gem "prune_ar"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/prune_ar-0.1.0.gem
- 版本锁定: `gem "prune_ar", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
