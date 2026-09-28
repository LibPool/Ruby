# mongoid-bigbang

**Tag**: testing

## 简介

When you have a project in which you are not using Mongoid::Timestamps and you want to mock an object's creation time, you have to do some cumbersome operations in order to get those first 4 bytes of the ObjectId to represent the seconds since the Unix epoch that you want for that object.

    Particularly, if you want to have two objects with the same creation time, it would not suffice to generate the IDs via the BSON::ObjectId.from_time method, since it would yield the same ID for both objects, and you probably do not want them to be seen as the same object.

    This gem solves this little annoying issue by generating a unique ID for the given timestamp by using the other 8 bytes in ObjectId to generate the needed additional entropy.

## 官网

- 主页: https://github.com/dnlserrano/mongoid-bigbang
- 文档: https://www.rubydoc.info/gems/mongoid-bigbang/0.0.3
- RubyGems: https://rubygems.org/gems/mongoid-bigbang

## 历史版本号

- 0.0.3 (2015-01-22)
- 0.0.2 (2015-01-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/mongoid-bigbang
- gem 安装: `gem install mongoid-bigbang`
- Bundler: `gem "mongoid-bigbang"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/mongoid-bigbang-0.0.3.gem
- 版本锁定: `gem "mongoid-bigbang", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
