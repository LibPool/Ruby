# net-http-persistent-pool

**Tag**: web, networking

## 简介

Manages persistent connections using Net::HTTP plus a speed fix for Ruby 1.8.
It's thread-safe too!

Using persistent HTTP connections can dramatically increase the speed of HTTP.
Creating a new HTTP connection for every request involves an extra TCP
round-trip and causes TCP congestion avoidance negotiation to start over.

Net::HTTP supports persistent connections with some API methods but does not
handle reconnection gracefully.  Net::HTTP::Persistent supports reconnection
and retry according to RFC 2616.

## 官网

- 主页: http://docs.seattlerb.org/net-http-persistent
- 文档: https://www.rubydoc.info/gems/net-http-persistent-pool/2.10.0
- RubyGems: https://rubygems.org/gems/net-http-persistent-pool

## 历史版本号

- 2.10.0 (2016-05-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/net-http-persistent-pool
- gem 安装: `gem install net-http-persistent-pool`
- Bundler: `gem "net-http-persistent-pool"`
- 最新版本: 2.10.0
- 最新版归档: https://rubygems.org/downloads/net-http-persistent-pool-2.10.0.gem
- 版本锁定: `gem "net-http-persistent-pool", "~> 2.10.0"`
- 中央仓库: https://rubygems.org/
