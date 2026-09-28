# eager_record

**Tag**: database, data

## 简介

EagerRecord extends ActiveRecord to automate association preloading. Each time a collection of more than one record is loaded from the database, each record remembers the collection that it is part of; then when one of those records has an association accessed, EagerRecord triggers a preload_associations for all the records in the originating collection. Never worry about that :include option again!

## 官网

- 主页: http://github.com/outoftime/eager_record
- 文档: https://www.rubydoc.info/gems/eager_record/0.2.0
- RubyGems: https://rubygems.org/gems/eager_record

## 历史版本号

- 0.2.0 (2013-06-12)
- 0.1.3 (2011-01-04)
- 0.1.2 (2010-06-21)
- 0.1.1 (2010-06-04)
- 0.1.0 (2010-05-28)
- 0.0.3 (2010-05-04)
- 0.0.2 (2010-05-03)
- 0.0.1 (2010-05-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/eager_record
- gem 安装: `gem install eager_record`
- Bundler: `gem "eager_record"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/eager_record-0.2.0.gem
- 版本锁定: `gem "eager_record", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
