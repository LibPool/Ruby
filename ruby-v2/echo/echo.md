# echo

**Tag**: web, testing, networking

## 简介

Echo is a test double for API interactions that learns from the real API. In its simplest use case, it extends Net::HTTP and tracks every HTTP call to a registered domain. If it hasn't seen that call, it stores both the request and the response. On subsequent calls it returns the stored response. Explicit scenario start/end markers are also supported for more complex multiple-step interactions.

## 官网

- 主页: http://github.com/SFEley/echo
- RubyGems: https://rubygems.org/gems/echo

## 历史版本号

- 0.0.0 (2009-10-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/echo
- gem 安装: `gem install echo`
- Bundler: `gem "echo"`
- 最新版本: 0.0.0
- 最新版归档: https://rubygems.org/downloads/echo-0.0.0.gem
- 版本锁定: `gem "echo", "~> 0.0.0"`
- 中央仓库: https://rubygems.org/
