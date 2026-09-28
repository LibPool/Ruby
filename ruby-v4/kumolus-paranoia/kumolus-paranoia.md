# kumolus-paranoia

**Tag**: library

## 简介

You would use this Paranoia gem if you
    wished that when you called destroy on an Active Record object that it
    didn't actually destroy it, but just "hide" the record. Paranoia does this
    by setting a deleted_at field to the current time when you destroy a record,
    and hides it by scoping all queries on your model to only include records
    which do not have a deleted_at field.

## 官网

- 主页: https://github.com/kumoas/kumolus-paranoia
- 文档: https://www.rubydoc.info/gems/kumolus-paranoia/0.1.0
- RubyGems: https://rubygems.org/gems/kumolus-paranoia

## 历史版本号

- 0.1.0 (2018-11-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/kumolus-paranoia
- gem 安装: `gem install kumolus-paranoia`
- Bundler: `gem "kumolus-paranoia"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/kumolus-paranoia-0.1.0.gem
- 版本锁定: `gem "kumolus-paranoia", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
