# easy_jwt_auth

**Tag**: web, security, tooling, data

## 简介

A typical usecase of JWT tokens is when building an API. JWT tokens can be sent as authorization tokens in headers. The advantage of using JWT tokens is that they are signed with a secret, so the information inside them cannot be tampered. This makes them ideal for embeding both authentication and authorization information in one step (e.g. by "decoding" the token, one can get information about the user and the roles a user has in case of a role-based authorization). Also, the fact that expiration timestamps can be embedded in the data of the token and be handled automatically, can be used to easily build short-lived tokens, making an API more secure.

## 官网

- 主页: https://github.com/m1lt0n/easy_jwt_auth
- 文档: https://www.rubydoc.info/gems/easy_jwt_auth/0.1.1
- RubyGems: https://rubygems.org/gems/easy_jwt_auth

## 历史版本号

- 0.1.1 (2017-04-19)
- 0.1.0 (2017-04-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/easy_jwt_auth
- gem 安装: `gem install easy_jwt_auth`
- Bundler: `gem "easy_jwt_auth"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/easy_jwt_auth-0.1.1.gem
- 版本锁定: `gem "easy_jwt_auth", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
