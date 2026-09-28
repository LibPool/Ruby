# mongoid_acl

**Tag**: library

## 简介

Mongoid::ACL allows you to easily add access control lists to your Mongoid::Document objects. This implementation assumes you need to check acl's when loading an object, it's not efficient if you want to retrieve all the objects an actor has rights on (though it could be if they are all in the same collection). This handles storing and reading permissions only, any actual checking of permissions needs to be done in your application using the methods provided (see usage in README)

## 官网

- 主页: https://bitbucket.org/nielsv/mongoid_acl
- RubyGems: https://rubygems.org/gems/mongoid_acl

## 历史版本号

- 0.1.1 (2012-03-05)
- 0.1.0 (2011-12-06)
- 0.0.3 (2011-12-06)
- 0.0.2 (2011-12-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/mongoid_acl
- gem 安装: `gem install mongoid_acl`
- Bundler: `gem "mongoid_acl"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/mongoid_acl-0.1.1.gem
- 版本锁定: `gem "mongoid_acl", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
