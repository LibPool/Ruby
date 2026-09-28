# softwaregravy-net-http-persistent

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
- RubyGems: https://rubygems.org/gems/softwaregravy-net-http-persistent

## 历史版本号

- 2.6 (2012-05-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/softwaregravy-net-http-persistent
- gem 安装: `gem install softwaregravy-net-http-persistent`
- Bundler: `gem "softwaregravy-net-http-persistent"`
- 最新版本: 2.6
- 最新版归档: https://rubygems.org/downloads/softwaregravy-net-http-persistent-2.6.gem
- 版本锁定: `gem "softwaregravy-net-http-persistent", "~> 2.6"`
- 中央仓库: https://rubygems.org/
