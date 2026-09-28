# thrift_amqp_transport

**Tag**: cli

## 简介

Transports thrift messages over a the advanced message queue protocol. (AMQP) Because of the unconnected broadcasting nature of the message queue, this  transport supports only one-way communication.   The usage scenario is that you would use this to broadcast information about  services (1 producer, n consumers) and then create point to point connections  from client to service using normal (TCP) thrift. You gain the advantage of using only one interface definition language (IDL).

## 官网

- 文档: https://www.rubydoc.info/gems/thrift_amqp_transport/0.1.0
- RubyGems: https://rubygems.org/gems/thrift_amqp_transport

## 历史版本号

- 0.1.0 (2009-08-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/thrift_amqp_transport
- gem 安装: `gem install thrift_amqp_transport`
- Bundler: `gem "thrift_amqp_transport"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/thrift_amqp_transport-0.1.0.gem
- 版本锁定: `gem "thrift_amqp_transport", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
