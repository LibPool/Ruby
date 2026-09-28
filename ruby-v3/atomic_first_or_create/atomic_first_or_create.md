# atomic_first_or_create

**Tag**: database, data

## 简介

first_or_create does not guarantee uniqueness by itself, and if there is a uniqueness constraint on the database, it may fail with a RecordNotUnique exception. This gem adds atomic_first_or_create, which, in conjunction with a uniqueness constraint, provides the correct behaviour.

## 官网

- 主页: https://edgepetrol.com
- 文档: https://www.rubydoc.info/gems/atomic_first_or_create/1.0
- RubyGems: https://rubygems.org/gems/atomic_first_or_create

## 历史版本号

- 1.0 (2020-11-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/atomic_first_or_create
- gem 安装: `gem install atomic_first_or_create`
- Bundler: `gem "atomic_first_or_create"`
- 最新版本: 1.0
- 最新版归档: https://rubygems.org/downloads/atomic_first_or_create-1.0.gem
- 版本锁定: `gem "atomic_first_or_create", "~> 1.0"`
- 中央仓库: https://rubygems.org/
