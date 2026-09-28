# net-http-persistent-retry

**Tag**: web, networking

## 简介

Manages persistent connections using Net::HTTP. It's thread-safe too! Using persistent HTTP connections can dramatically increase the speed of HTTP. Creating a new HTTP connection for every request involves an extra TCP round-trip and causes TCP congestion avoidance negotiation to start over. Net::HTTP supports persistent connections with some API methods but does not handle reconnection gracefully. Net::HTTP::Persistent supports reconnection and retry according to RFC 2616.

## 官网

- 主页: https://github.com/grosser/net-http-persistent
- 文档: https://www.rubydoc.info/gems/net-http-persistent-retry/3.0.1
- RubyGems: https://rubygems.org/gems/net-http-persistent-retry

## 历史版本号

- 3.0.1 (2019-05-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/net-http-persistent-retry
- gem 安装: `gem install net-http-persistent-retry`
- Bundler: `gem "net-http-persistent-retry"`
- 最新版本: 3.0.1
- 最新版归档: https://rubygems.org/downloads/net-http-persistent-retry-3.0.1.gem
- 版本锁定: `gem "net-http-persistent-retry", "~> 3.0.1"`
- 中央仓库: https://rubygems.org/
