# cosmos-unpacking_interface

**Tag**: library

## 简介

A custom interface that unpacks aggregate packets (packets with many granules) into many  simple packets (packets with a single granule). This way we can use all the cosmos niceties  without having to send packets for individual measurements. Essentially we unpack an aggregate  packet into many packets that are stored in a queue that is read from. When the queue is empty  we look for new aggregate packets

## 官网

- 主页: https://github.com/nick-benoit14/cosmos-unpacking_interface
- 文档: https://www.rubydoc.info/gems/cosmos-unpacking_interface/1.0.0
- RubyGems: https://rubygems.org/gems/cosmos-unpacking_interface

## 历史版本号

- 1.0.0 (2019-04-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/cosmos-unpacking_interface
- gem 安装: `gem install cosmos-unpacking_interface`
- Bundler: `gem "cosmos-unpacking_interface"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/cosmos-unpacking_interface-1.0.0.gem
- 版本锁定: `gem "cosmos-unpacking_interface", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
