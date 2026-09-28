# chef-cleanroom

**Tag**: data

## 简介

Ruby is an excellent programming language for creating and managing custom DSLs, but how can you securely evaluate a DSL while explicitly controlling the methods exposed to the user? Our good friends instance_eval and instance_exec are great, but they expose all methods - public, protected, and private - to the user. Even worse, they expose the ability to accidentally or intentionally alter the behavior of the system! The cleanroom pattern is a safer, more convenient, Ruby-like approach for limiting the information exposed by a DSL while giving users the ability to write awesome code!

## 官网

- 主页: https://github.com/chef/cleanroom
- 文档: https://www.rubydoc.info/gems/chef-cleanroom/1.0.5
- RubyGems: https://rubygems.org/gems/chef-cleanroom

## 历史版本号

- 1.0.5 (2022-05-26)
- 1.0.4 (2021-10-01)
- 1.0.3 (2021-10-01)
- 1.0.2 (2019-09-19)
- 1.0.1 (2019-09-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/chef-cleanroom
- gem 安装: `gem install chef-cleanroom`
- Bundler: `gem "chef-cleanroom"`
- 最新版本: 1.0.5
- 最新版归档: https://rubygems.org/downloads/chef-cleanroom-1.0.5.gem
- 版本锁定: `gem "chef-cleanroom", "~> 1.0.5"`
- 中央仓库: https://rubygems.org/
