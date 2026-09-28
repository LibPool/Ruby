# mongoid-sadstory

**Tag**: web, testing

## 简介

This is a sad story - mongoid maintainers decided to drop support for multi paramter fields in mongoid 4.x, leaving it to ActiveSupport/ActiveModel and rails. Sadly there was no extraction ready after ror 4.x was released and since mongoid 4.x was the only version working with ror 4.x series this meant you could not update your application from ror 3.x to 4.x if you were using mongoid and you had date/time/datetime fields somewhere in your application. That's just sad. What I did is just extracted our hacks to make multiparams working again. Make sure your specs are passing before using this in prod systems...

## 官网

- 文档: https://www.rubydoc.info/gems/mongoid-sadstory/0.0.2
- RubyGems: https://rubygems.org/gems/mongoid-sadstory

## 历史版本号

- 0.0.2 (2014-03-06)
- 0.0.1 (2013-11-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/mongoid-sadstory
- gem 安装: `gem install mongoid-sadstory`
- Bundler: `gem "mongoid-sadstory"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/mongoid-sadstory-0.0.2.gem
- 版本锁定: `gem "mongoid-sadstory", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
