# authist

**Tag**: web, database, security, data

## 简介

Authist is a Ruby on Rails plugin that provides a simple way to add role-based authorization to your application.
It can easily be plugged into any user or group models in your application, and allows you to define a set of access types that roles can provide.
Roles and users' participation in them can be changed at runtime, providing a highly customizable access control system to your
website administrators.

Authist is designed with a minimal impact on your own code architecture in mind. It creates a few database tables for itself, but does not change anything
whatsoever to the data of your own models, and only adds a minimal mixin to the model itself.
This allows it to peacefully integrate with most authentication libraries. Authist can also be used in combination with more
advanced authorization gems like Pundit to add runtime-editable access roles to their policies.

## 官网

- 主页: http://github.com/angryzor
- 文档: https://www.rubydoc.info/gems/authist/0.0.1
- RubyGems: https://rubygems.org/gems/authist

## 历史版本号

- 0.0.1 (2014-10-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/authist
- gem 安装: `gem install authist`
- Bundler: `gem "authist"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/authist-0.0.1.gem
- 版本锁定: `gem "authist", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
