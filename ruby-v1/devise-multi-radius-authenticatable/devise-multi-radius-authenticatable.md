# devise-multi-radius-authenticatable

**Tag**: web, database, security, data

## 简介

A new authentication strategy named radius_authenticatable is added to the list of warden strategies when the model requests it.  The radius server information is configured through the devise initializer. One or more servers may be configured.  When a user attempts to authenticate via radius, the radiustar gem is used to perform the authentication with each server until a response is received.  This authentication strategy can be used in place of the database_authenticatable or alongside it depending on the needs of the application.

## 官网

- 主页: http://github.com/mzaccari/devise-radius-authenticatable
- 文档: https://www.rubydoc.info/gems/devise-multi-radius-authenticatable/0.3.0
- RubyGems: https://rubygems.org/gems/devise-multi-radius-authenticatable

## 历史版本号

- 0.3.0 (2020-04-15)
- 0.2.0 (2016-10-27)
- 0.1.2 (2015-12-03)
- 0.1.1 (2015-12-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/devise-multi-radius-authenticatable
- gem 安装: `gem install devise-multi-radius-authenticatable`
- Bundler: `gem "devise-multi-radius-authenticatable"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/devise-multi-radius-authenticatable-0.3.0.gem
- 版本锁定: `gem "devise-multi-radius-authenticatable", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
