# rubarb

**Tag**: web, cli, networking

## 简介

This library uses two socket connections between a client and a server. One is used for request / replies from the
client to the server.  The other is used for remote calls made from the server to the client.

Each end publishes a single object on which
methods can be called by the remote end.  All calls to the remote objects are asyncronous.  Do not make any blocking
calls in the published object.  Responses are return by calling the "reply method on the responder object.

## 官网

- 主页: http://github.com/dougbradbury/rubarb
- RubyGems: https://rubygems.org/gems/rubarb

## 历史版本号

- 0.12.10 (2012-08-29)
- 1.0.0 (2012-08-29)
- 0.2.11 (2011-02-09)
- 0.2.0 (2010-11-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/rubarb
- gem 安装: `gem install rubarb`
- Bundler: `gem "rubarb"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/rubarb-1.0.0.gem
- 版本锁定: `gem "rubarb", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
