# cmoran92-paranoia

**Tag**: web

## 简介

Paranoia is a re-implementation of acts_as_paranoid for Rails 3, using much, much, much less code. You would use either plugin / gem if you wished that when you called destroy on an Active Record object that it didn't actually destroy it, but just "hid" the record. Paranoia does this by setting a deleted_at field to the current time when you destroy a record, and hides it by scoping all queries on your model to only include records which do not have a deleted_at field.

## 官网

- 主页: http://rubygems.org/gems/paranoia
- 文档: https://www.rubydoc.info/gems/cmoran92-paranoia/2.0.2a
- RubyGems: https://rubygems.org/gems/cmoran92-paranoia

## 历史版本号

- 2.0.2a (2014-09-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/cmoran92-paranoia
- gem 安装: `gem install cmoran92-paranoia`
- Bundler: `gem "cmoran92-paranoia"`
- 最新版本: 2.0.2a
- 最新版归档: https://rubygems.org/downloads/cmoran92-paranoia-2.0.2a.gem
- 版本锁定: `gem "cmoran92-paranoia", "~> 2.0.2a"`
- 中央仓库: https://rubygems.org/
