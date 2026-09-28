# net-http-persistent

**Tag**: web, networking

## 简介

Manages persistent connections using Net::HTTP including a thread pool for
connecting to multiple hosts.

Using persistent HTTP connections can dramatically increase the speed of HTTP.
Creating a new HTTP connection for every request involves an extra TCP
round-trip and causes TCP congestion avoidance negotiation to start over.

Net::HTTP supports persistent connections with some API methods but does not
make setting up a single persistent connection or managing multiple
connections easy.  Net::HTTP::Persistent wraps Net::HTTP and allows you to
focus on how to make HTTP requests.

## 官网

- 主页: https://github.com/drbrain/net-http-persistent
- RubyGems: https://rubygems.org/gems/net-http-persistent

## 历史版本号

- 4.0.8 (2025-12-30)
- 4.0.7 (2025-12-30)
- 4.0.6 (2025-05-29)
- 4.0.5 (2024-12-04)
- 4.0.4 (2024-09-09)
- 4.0.3 (2024-09-09)
- 4.0.2 (2023-03-29)
- 4.0.1 (2021-01-12)
- 4.0.0 (2020-05-01)
- 3.1.0 (2019-07-25)
- 3.0.1 (2019-04-29)
- 3.0.0 (2016-10-06)
- 2.9.4 (2014-02-10)
- 2.9.3 (2014-02-07)
- 2.9.2 (2014-02-06)
- 2.9.1 (2014-01-22)
- 2.9 (2013-07-24)
- 2.8 (2012-10-18)
- 2.7 (2012-06-06)
- 2.6 (2012-03-26)
- 2.5.2 (2012-02-13)
- 2.5.1 (2012-02-10)
- 2.5 (2012-02-07)
- 2.4.1 (2012-02-04)
- 2.4 (2012-01-31)
- 2.3.3 (2011-12-21)
- 2.3.2 (2011-11-09)
- 2.3.1 (2011-10-27)
- 2.3 (2011-10-25)
- 2.2 (2011-10-25)
- 2.1 (2011-09-20)
- 2.0 (2011-08-27)
- 1.9 (2011-08-27)
- 1.8.1 (2011-08-09)
- 1.8 (2011-06-27)
- 1.7 (2011-04-17)
- 1.6.1 (2011-03-08)
- 1.6 (2011-03-02)
- 1.5.2 (2011-02-25)
- 1.5.1 (2011-02-10)
- 1.5 (2011-01-26)
- 1.4.1 (2010-10-13)
- 1.4 (2010-09-30)
- 1.3.1 (2010-09-13)
- 1.3 (2010-09-09)
- 1.2.5 (2010-07-27)
- 1.2.4 (2010-07-26)
- 1.2.3 (2010-06-29)
- 1.2.2 (2010-06-22)
- 1.2.1 (2010-05-25)
- 1.2 (2010-05-21)
- 1.1 (2010-05-19)
- 1.0.1 (2010-05-06)
- 1.0 (2010-05-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/net-http-persistent
- gem 安装: `gem install net-http-persistent`
- Bundler: `gem "net-http-persistent"`
- 最新版本: 4.0.8
- 最新版归档: https://rubygems.org/downloads/net-http-persistent-4.0.8.gem
- 版本锁定: `gem "net-http-persistent", "~> 4.0.8"`
- 中央仓库: https://rubygems.org/
