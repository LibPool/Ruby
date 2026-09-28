# flagpole_sitta

**Tag**: web, database, template, data

## 简介

Flagpole Sitta is a gem that main purpose is to make it easier to effectively fragment cache in dynamic fashions in Rails. 
When ever a cache is created it is associated with any model and/or record you tell it to be from the view helper method. When that model and/or record is updated all it's associated caches are cleared. 
Flagpole also expects you to put all your database calls into Procs/Lamdbas. This makes it so that your database calls wont have to happen unless your cache hasn't been created. Thus speeding up response time and reducing database traffic.

## 官网

- 主页: https://github.com/rovermicrover/FlagpoleSitta
- RubyGems: https://rubygems.org/gems/flagpole_sitta

## 历史版本号

- 0.9.7.1 (2012-10-01)
- 0.9.7 (2012-10-01)
- 0.9.6 (2012-09-19)
- 0.9.5 (2012-09-19)
- 0.9.4 (2012-08-28)
- 0.9.2 (2012-08-21)
- 0.9.0 (2012-08-08)
- 0.8.0 (2012-07-30)
- 0.7.3 (2012-07-24)
- 0.7.2 (2012-07-22)
- 0.7.1 (2012-07-22)
- 0.7.0 (2012-07-21)
- 0.6.0 (2012-07-19)
- 0.5.9 (2012-07-18)
- 0.5.1 (2012-07-18)
- 0.5.0 (2012-07-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/flagpole_sitta
- gem 安装: `gem install flagpole_sitta`
- Bundler: `gem "flagpole_sitta"`
- 最新版本: 0.9.7.1
- 最新版归档: https://rubygems.org/downloads/flagpole_sitta-0.9.7.1.gem
- 版本锁定: `gem "flagpole_sitta", "~> 0.9.7.1"`
- 中央仓库: https://rubygems.org/
