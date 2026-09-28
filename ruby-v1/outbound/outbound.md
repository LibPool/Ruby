# outbound

**Tag**: web, testing, data

## 简介

Outbound sends automated email, SMS, phone calls and push notifications based on the actions users take or do not take in your app. The Outbound API has two components:

Identify each of your users and their attributes using an identify API call.
Track the actions that each user takes in your app using a track API call.
Because every message is associated with a user (identify call) and a specific trigger action that a user took or should take (track call), Outbound is able to keep track of how each message affects user actions in your app. These calls also allow you to target campaigns and customize each message based on user data.

Example: When a user in San Francisco(user attribute) does signup(event) but does not upload a picture(event) within 2 weeks, send them an email about how they'll benefit from uploading a picture.

## 官网

- 主页: https://outbound.io
- 文档: https://www.rubydoc.info/gems/outbound/1.2.0
- RubyGems: https://rubygems.org/gems/outbound

## 历史版本号

- 1.2.0 (2016-01-29)
- 1.1.1 (2016-01-26)
- 1.1.0 (2016-01-26)
- 1.0.1 (2015-10-05)
- 1.0.0 (2015-05-12)
- 0.3.2 (2014-11-17)
- 0.3.1 (2014-11-07)
- 0.3 (2014-09-26)
- 0.2.1 (2014-08-19)
- 0.2 (2014-07-23)
- 0.1.0 (2014-07-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/outbound
- gem 安装: `gem install outbound`
- Bundler: `gem "outbound"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/outbound-1.2.0.gem
- 版本锁定: `gem "outbound", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
