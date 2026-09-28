# ephemeron

**Tag**: database, data

## 简介

Ephemeron improves the performance of your app.
It takes on itself the persistence of the ActiveRecord objects.
It protects you from saving the same object many times.
It checks whether a fetched from a database object was used.
It allows you to eliminate the controller's before_actions that are unnecessarily called.
Ephemeron works in the context of the thread and does the bulk of its job (i.a. persistence) at the end of the thread's lifecycle.
Although, you can trigger the finalization at any given moment.
You don't have to make a distinction in the code for the part that is responsible for the domain logic and the other responsible for the application layers.

## 官网

- 主页: https://artofcode.co
- 文档: https://www.rubydoc.info/gems/ephemeron/0.6.1
- RubyGems: https://rubygems.org/gems/ephemeron

## 历史版本号

- 0.6.1 (2023-03-28)
- 0.6.0 (2022-02-07)
- 0.5.0 (2020-08-28)
- 0.4.0 (2020-08-27)
- 0.3.0 (2020-08-27)
- 0.2.1 (2020-08-25)
- 0.2.0 (2020-08-25)
- 0.1.0 (2020-01-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/ephemeron
- gem 安装: `gem install ephemeron`
- Bundler: `gem "ephemeron"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/ephemeron-0.6.1.gem
- 版本锁定: `gem "ephemeron", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
