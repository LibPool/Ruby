# always_verify_ssl_certificates

**Tag**: web, networking

## 简介

Ruby’s net/http is setup to never verify SSL certificates by default. Most ruby libraries do the same. That means that you’re not verifying the identity of the server you’re communicating with and are therefore exposed to man in the middle attacks. This gem monkey-patches net/http to force certificate verification and make turning it off impossible.

## 官网

- 主页: http://github.com/jamesgolick/always_verify_ssl_certificates
- RubyGems: https://rubygems.org/gems/always_verify_ssl_certificates

## 历史版本号

- 0.3.0 (2011-03-18)
- 0.2.0 (2010-12-09)
- 0.1.0 (2010-12-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/always_verify_ssl_certificates
- gem 安装: `gem install always_verify_ssl_certificates`
- Bundler: `gem "always_verify_ssl_certificates"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/always_verify_ssl_certificates-0.3.0.gem
- 版本锁定: `gem "always_verify_ssl_certificates", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
