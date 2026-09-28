# websocket_messaging

**Tag**: web, database, networking, data

## 简介

This gem has been extracted from chat application based on websockets.
    It consists of basically two components: channels and notifiers. Channels are meant to handle
    external communication through provided socket in a bidirectional manner while
    using notifiers for internal communication. Notifiers are using a messaging bus,
    which might be anything supporting publish/subscribe pattern across multiple threads / processes,
    i.e. common Redis cluster. It lets you define your own handlers for receiving and sending data.

## 官网

- 主页: https://github.com/growthrepublic/websocket_messaging
- 文档: https://www.rubydoc.info/gems/websocket_messaging/0.0.1
- RubyGems: https://rubygems.org/gems/websocket_messaging

## 历史版本号

- 0.0.1 (2014-05-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/websocket_messaging
- gem 安装: `gem install websocket_messaging`
- Bundler: `gem "websocket_messaging"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/websocket_messaging-0.0.1.gem
- 版本锁定: `gem "websocket_messaging", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
