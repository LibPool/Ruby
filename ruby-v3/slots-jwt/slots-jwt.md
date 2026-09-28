# slots-jwt

**Tag**: web, database, security, data

## 简介

Token Authentication for Rails using JWT. Slots is designed to keep JWT stateless and minimize database calls. This is done by storing (none sensitive) data in the JWT and populating current_user with the JWT data. This allows for things like `current_user.teams` or other assocations to be called on the user. Unless explicitly told slots will only load the user from the database when creating (or updating an expired) token.

## 官网

- 主页: https://github.com/jonathongardner/slots-jwt
- 文档: https://www.rubydoc.info/gems/slots-jwt/0.1.1
- RubyGems: https://rubygems.org/gems/slots-jwt

## 历史版本号

- 0.1.1 (2020-04-18)
- 0.1.0 (2019-11-01)
- 0.0.4 (2019-08-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/slots-jwt
- gem 安装: `gem install slots-jwt`
- Bundler: `gem "slots-jwt"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/slots-jwt-0.1.1.gem
- 版本锁定: `gem "slots-jwt", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
