# xaop-exception_notification

**Tag**: web, testing

## 简介

This gem differs from the exception_notifier gem in 3 ways:
a) It actually works, because the latest commits on from the github rails/exception_notification repository are incorporated
b) The name of the gem is closer to the name of the github repository (hopefully causing less confusion)
c) The options to the middleware are stored in the Rack env, meaning you can send exception notifications from your own code after catching an exception, while still sending back a response to the user (probably mainly useful with Ajax requests)

## 官网

- 文档: https://www.rubydoc.info/gems/xaop-exception_notification/1.0.2
- RubyGems: https://rubygems.org/gems/xaop-exception_notification

## 历史版本号

- 1.0.2 (2011-01-27)
- 1.0.1 (2011-01-27)
- 1.0.0 (2010-10-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/xaop-exception_notification
- gem 安装: `gem install xaop-exception_notification`
- Bundler: `gem "xaop-exception_notification"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/xaop-exception_notification-1.0.2.gem
- 版本锁定: `gem "xaop-exception_notification", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
