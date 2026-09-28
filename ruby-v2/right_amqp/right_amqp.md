# right_amqp

**Tag**: cli

## 简介

RightAMQP provides a high availability client for interfacing with the
RightScale RabbitMQ broker using the AMQP protocol. The AMQP version on which
this gem is based is 0.6.7 but beyond that it contains a number of bug fixes and
enhancements including reconnect, message return, heartbeat, and UTF-8 support.
The high availability is achieved by maintaining multiple broker connections
such that failed connections automatically reconnect and only connected
brokers are used when routing a message. Although the HABrokerClient class
is the intended primary means for accessing RabbitMQ services with this gem,
alternatively the underlying AMQP services may be used directly.

## 官网

- 主页: https://github.com/rightscale/right_amqp
- 文档: https://www.rubydoc.info/gems/right_amqp/0.8.7
- RubyGems: https://rubygems.org/gems/right_amqp

## 历史版本号

- 0.8.7 (2015-06-26)
- 0.8.6 (2014-11-17)
- 0.8.5 (2014-10-02)
- 0.8.4 (2014-07-09)
- 0.8.3 (2014-05-27)
- 0.7.0 (2013-08-07)
- 0.6.1 (2013-07-23)
- 0.6.0 (2012-12-11)
- 0.3.3 (2012-10-31)
- 0.3.2 (2012-10-04)
- 0.5.2 (2012-10-04)
- 0.3.1 (2012-08-21)
- 0.3.0 (2012-05-01)
- 0.2.1 (2012-03-22)
- 0.2.0 (2012-03-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/right_amqp
- gem 安装: `gem install right_amqp`
- Bundler: `gem "right_amqp"`
- 最新版本: 0.8.7
- 最新版归档: https://rubygems.org/downloads/right_amqp-0.8.7.gem
- 版本锁定: `gem "right_amqp", "~> 0.8.7"`
- 中央仓库: https://rubygems.org/
