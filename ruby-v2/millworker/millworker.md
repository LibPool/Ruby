# millworker

**Tag**: web, cli, testing, networking, data

## 简介

A Ruby gem which takes the pain of continuously reading data from a serial port
away and lets you focus on dealing with the data received.

This was written specifically for reading in data from an ID-20
RFID card reader and running custom scripts to automatically perform
various tasks when patrons scanned their badge at the
[MN Mill](http://mnmill.org) (logging attendance, etc).


Custom scripts are loaded from `ENV["HOME"]/millworker/tasks` and are executed
in alphabetical order. Each script is executed with the ID of the badge passed
in as an argument. For example, a script called `tweet_id.rb` existed in the
afformentioned directory, it would be executed as if you had opened up a
command terminal and typed `tweet_id.rb RFID_TAG_ID_HERE`.

## 官网

- 主页: http://github.com/tomkersten/millworker
- RubyGems: https://rubygems.org/gems/millworker

## 历史版本号

- 0.2.0 (2012-10-19)
- 0.1.3 (2012-09-19)
- 0.1.2 (2012-09-19)
- 0.1.1 (2012-09-19)
- 0.1.0 (2012-09-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/millworker
- gem 安装: `gem install millworker`
- Bundler: `gem "millworker"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/millworker-0.2.0.gem
- 版本锁定: `gem "millworker", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
