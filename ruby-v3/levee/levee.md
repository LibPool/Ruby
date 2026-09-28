# levee

**Tag**: web, database, tooling, data

## 简介

The purpose of the builder object is to create a layer of abstraction between the controller and models in a Rails application. The builder is particularly useful for receiving complex post and put requests with multiple parameters, but is lightweight enough to use for simple writes when some filtering or parameter combination validation might be useful before writing to the database. Since it wraps the entire write action to mulitple models in a single transaction, any failure in the builder will result in the entire request being rolled back.

## 官网

- 主页: https://github.com/mmartinson/levee
- 文档: https://www.rubydoc.info/gems/levee/0.0.4
- RubyGems: https://rubygems.org/gems/levee

## 历史版本号

- 0.0.4 (2015-07-29)
- 0.0.3 (2015-03-18)
- 0.0.2 (2015-03-18)
- 0.0.1 (2015-03-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/levee
- gem 安装: `gem install levee`
- Bundler: `gem "levee"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/levee-0.0.4.gem
- 版本锁定: `gem "levee", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
