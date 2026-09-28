# xap_ruby

**Tag**: testing, networking, tooling

## 简介

This gem provides basic xAP Automation protocol support for EventMachine
applications.  It was developed for use in Nitrogen Logic controller software.
There are no automated tests and the code could be improved in many ways, but it
may still be useful to someone.

This is a Ruby library written from scratch for communicating with a home
automation network using the xAP protocol.  Supports sending and receiving
arbitrary xAP messages, triggering callbacks on certain received messages, etc.
Also includes an implementation of an xAP Basic Status and Control device.
Incoming xAP messages are parsed using an ad-hoc parser based on Ruby's
String#split() and Array#map() (a validating Treetop parser is also available).
Network events are handled using EventMachine.

## 官网

- 主页: https://github.com/nitrogenlogic/xap_ruby/
- 文档: https://www.rubydoc.info/gems/xap_ruby/0.1.1
- RubyGems: https://rubygems.org/gems/xap_ruby

## 历史版本号

- 0.1.1 (2021-03-05)
- 0.1.0 (2017-01-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/xap_ruby
- gem 安装: `gem install xap_ruby`
- Bundler: `gem "xap_ruby"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/xap_ruby-0.1.1.gem
- 版本锁定: `gem "xap_ruby", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
