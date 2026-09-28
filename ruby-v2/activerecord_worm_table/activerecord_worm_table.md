# activerecord_worm_table

**Tag**: library

## 简介

manage WriteOnceReadMany tables backing ActiveRecord models.
                         there will be a switch table and multiple backing tables for each 
                         ActiveRecord model, all created and managed automatically. a new
                         version of a table is created by writing to the working table, and
                         then Model.advance_version which makes the working table active,
                         and creates a new working table from the base model schmea

## 官网

- 主页: http://github.com/mccraigmccraig/activerecord_worm_table
- RubyGems: https://rubygems.org/gems/activerecord_worm_table

## 历史版本号

- 0.8.1 (2010-03-11)
- 0.8.0 (2010-02-17)
- 0.6.0 (2009-12-15)
- 0.5.0 (2009-11-13)
- 0.4.0 (2009-11-05)
- 0.3.0 (2009-11-05)
- 0.2.0 (2009-11-04)
- 0.1.0 (2009-11-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/activerecord_worm_table
- gem 安装: `gem install activerecord_worm_table`
- Bundler: `gem "activerecord_worm_table"`
- 最新版本: 0.8.1
- 最新版归档: https://rubygems.org/downloads/activerecord_worm_table-0.8.1.gem
- 版本锁定: `gem "activerecord_worm_table", "~> 0.8.1"`
- 中央仓库: https://rubygems.org/
