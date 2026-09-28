# hash-auth

**Tag**: web, cli, security, networking

## 简介

HashAuth allows your Rails application to support incoming and outgoing two-factor authentication via hashing some component of an HTTPS request. Both sides of the request (your Rails app and your client or provider) must have some unique shared secret. This secret is used to create a hash of some portion of the request, ensuring that (if neither side has been compromised) only the other party could have created the request.

## 官网

- 主页: http://maxwells.github.com
- 文档: https://www.rubydoc.info/gems/hash-auth/1.0.3
- RubyGems: https://rubygems.org/gems/hash-auth

## 历史版本号

- 1.0.3 (2013-12-12)
- 1.0.2 (2013-06-24)
- 1.0.1 (2013-05-27)
- 1.0.0 (2013-05-27)
- 0.1.1 (2013-04-05)
- 0.1.0 (2013-04-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/hash-auth
- gem 安装: `gem install hash-auth`
- Bundler: `gem "hash-auth"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/hash-auth-1.0.3.gem
- 版本锁定: `gem "hash-auth", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
