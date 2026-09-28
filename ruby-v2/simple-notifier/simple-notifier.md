# simple-notifier

**Tag**: library

## 简介

Inspired by ActionMailer, Notifier offers Notifier::Base, a base class for creating notification handlers on any class or instance of a class.  Simply define a method in your handler named after the type of object you would like to create notification events for, substituting any namespace "::" delineation with "_", along with a signature that allows for the object as the first parameter and an optional params hash.  Then notify on that object or class by simply calling MyHandler.notify!(myclass, params).

## 官网

- 主页: http://github.com/alexagranov/simple-notifier
- 源码仓库: https://github.com/alexagranov/simple-notifier
- RubyGems: https://rubygems.org/gems/simple-notifier

## 历史版本号

- 0.1.1 (2011-02-11)
- 0.1.0 (2011-02-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/simple-notifier
- gem 安装: `gem install simple-notifier`
- Bundler: `gem "simple-notifier"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/simple-notifier-0.1.1.gem
- 版本锁定: `gem "simple-notifier", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
