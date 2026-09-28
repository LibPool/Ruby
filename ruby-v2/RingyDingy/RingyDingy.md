# RingyDingy

**Tag**: web, networking

## 简介

RingyDingy is a little boat that keeps your DRb service afloat!
RingyDingy automatically registers a service with a RingServer. If
communication between the RingServer and the RingyDingy is lost,
RingyDingy will re-register its service with the RingServer when it
reappears.

Similarly, the RingServer will automatically drop registrations by a
RingyDingy that it can't communicate with after a short timeout.

RingyDingy also includes a RingServer wrapper that adds verbose mode
to see what services as they register and expire and an option to list
all available services on the network.

## 官网

- 主页: https://github.com/drbrain/RingyDingy
- 源码仓库: https://githu.com/drbrain/RingyDingy
- 文档: http://docs.seattlerb.org/RingyDingy
- 问题追踪: https://githu.com/drbrain/RingyDingy/issues
- RubyGems: https://rubygems.org/gems/RingyDingy

## 历史版本号

- 1.6 (2013-06-05)
- 1.5 (2013-05-03)
- 1.4 (2013-03-16)
- 1.3 (2013-02-15)
- 1.2.1 (2009-07-25)
- 1.2.0 (2009-07-25)
- 1.1.0 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/RingyDingy
- gem 安装: `gem install RingyDingy`
- Bundler: `gem "RingyDingy"`
- 最新版本: 1.6
- 最新版归档: https://rubygems.org/downloads/RingyDingy-1.6.gem
- 版本锁定: `gem "RingyDingy", "~> 1.6"`
- 中央仓库: https://rubygems.org/
