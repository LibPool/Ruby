# google-auth-token_validator

**Tag**: web, cli, testing, security, serialization, networking, data

## 简介

The Google Sign-In API gives OAuth2 JSON Web Tokens (JWT) as response data upon user sign-in.
    A necessary step for a service provider to trust such a token is validatation. Accepting the
    token without validation would allow a malicious client to simply assert itself in your system.
    



    Google provides libraries in several languages (https://goo.gl/jkzS18) to accomplish this,
    as well as an API endpoint that can outsource the task to Google's own servers (thereby
    introducing an additional network round trip into every authentication step), but a Ruby
    implementation is missing. This gem fills that gap.

## 官网

- 主页: https://github.com/hamza/google-signin-token-validator
- 文档: https://www.rubydoc.info/gems/google-auth-token_validator/0.1.2
- RubyGems: https://rubygems.org/gems/google-auth-token_validator

## 历史版本号

- 0.1.2 (2017-09-17)
- 0.1.0 (2017-09-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/google-auth-token_validator
- gem 安装: `gem install google-auth-token_validator`
- Bundler: `gem "google-auth-token_validator"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/google-auth-token_validator-0.1.2.gem
- 版本锁定: `gem "google-auth-token_validator", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
