# active_record_openid_store

**Tag**: web, security, filesystem, data

## 简介

A store is required by an OpenID server and optionally by the consumer to store associations, nonces, and auth key information across requests and processes. If rails is distributed across several machines, they must must all have access to the same OpenID store data, so the FilesystemStore won't do. The code here is copied from the openid-ruby library examples. All I did was move some things around, add a namespace and package it all up as a rails engine/plugin, with some conveniences, for use with Rails 3.

## 官网

- 主页: https://github.com/skorks/active_record_openid_store
- RubyGems: https://rubygems.org/gems/active_record_openid_store

## 历史版本号

- 0.1.5 (2013-02-10)
- 0.1.4 (2012-07-29)
- 0.1.3 (2011-08-08)
- 0.1.2 (2011-07-21)
- 0.1.1 (2011-07-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/active_record_openid_store
- gem 安装: `gem install active_record_openid_store`
- Bundler: `gem "active_record_openid_store"`
- 最新版本: 0.1.5
- 最新版归档: https://rubygems.org/downloads/active_record_openid_store-0.1.5.gem
- 版本锁定: `gem "active_record_openid_store", "~> 0.1.5"`
- 中央仓库: https://rubygems.org/
