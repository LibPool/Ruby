# faye-publisher

**Tag**: web, cli, networking

## 简介

Allows to publish messages to a faye server, the main difference with the default faye client
    is that it does not need to run inside a EventMachine loop as it only opens a http connection
    with the server to send the event.
    Because of this is best to publish events from a separate thread using sidekiq for example.

## 官网

- 主页: https://github.com/adrian-gomez/faye-publisher
- 文档: https://www.rubydoc.info/gems/faye-publisher/0.0.3
- RubyGems: https://rubygems.org/gems/faye-publisher

## 历史版本号

- 0.0.3 (2014-04-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/faye-publisher
- gem 安装: `gem install faye-publisher`
- Bundler: `gem "faye-publisher"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/faye-publisher-0.0.3.gem
- 版本锁定: `gem "faye-publisher", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
