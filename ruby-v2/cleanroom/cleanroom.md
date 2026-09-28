# cleanroom

**Tag**: data

## 简介

Ruby is an excellent programming language for creating and managing custom DSLs, but how can you securely evaluate a DSL while explicitly controlling the methods exposed to the user? Our good friends instance_eval and instance_exec are great, but they expose all methods - public, protected, and private - to the user. Even worse, they expose the ability to accidentally or intentionally alter the behavior of the system! The cleanroom pattern is a safer, more convenient, Ruby-like approach for limiting the information exposed by a DSL while giving users the ability to write awesome code!

## 官网

- 主页: https://github.com/sethvargo/cleanroom
- 文档: http://rubydoc.info/github/sethvargo/cleanroom/master/frames
- 问题追踪: https://github.com/sethvargo/cleanroom/issues
- RubyGems: https://rubygems.org/gems/cleanroom

## 历史版本号

- 1.0.0 (2014-08-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/cleanroom
- gem 安装: `gem install cleanroom`
- Bundler: `gem "cleanroom"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/cleanroom-1.0.0.gem
- 版本锁定: `gem "cleanroom", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
