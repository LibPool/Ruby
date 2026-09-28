# elbping

**Tag**: web, networking

## 简介

elbping is a tool to ping all of the nodes behind an Amazon Elastic Load Balancer. It only works for ELBs in HTTP mode and works by triggering an HTTP 405 (METHOD NOT ALLOWED) error caused when the ELB receives a HTTP verb that is too long.

## 官网

- 主页: https://github.com/heroku/elbping
- 文档: https://www.rubydoc.info/gems/elbping/0.3
- 问题追踪: https://github.com/heroku/elbping/issues
- RubyGems: https://rubygems.org/gems/elbping

## 历史版本号

- 0.3 (2014-12-01)
- 0.2 (2014-09-05)
- 0.1 (2014-02-08)
- 0.0.16 (2013-12-07)
- 0.0.15 (2013-12-07)
- 0.0.14 (2013-09-14)
- 0.0.13 (2013-09-07)
- 0.0.12 (2013-08-30)
- 0.0.11 (2013-08-17)
- 0.0.10 (2013-08-16)
- 0.0.9 (2013-08-15)
- 0.0.8 (2013-08-14)
- 0.0.7 (2013-08-14)
- 0.0.6 (2013-08-13)
- 0.0.5 (2013-08-13)
- 0.0.4 (2013-08-13)
- 0.0.3 (2013-08-13)
- 0.0.2 (2013-08-13)
- 0.0.1 (2013-08-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/elbping
- gem 安装: `gem install elbping`
- Bundler: `gem "elbping"`
- 最新版本: 0.3
- 最新版归档: https://rubygems.org/downloads/elbping-0.3.gem
- 版本锁定: `gem "elbping", "~> 0.3"`
- 中央仓库: https://rubygems.org/
