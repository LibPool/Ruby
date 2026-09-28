# zbatery

**Tag**: web, networking

## 简介

Zbatery is an HTTP server for Rack applications on systems that either
do not support fork(), or have no memory (nor need) to run the
master/worker model.  It is based on Rainbows! (which is based on
Unicorn (which is based on Mongrel)) and inherits parts of each.
Zbatery supports your choice of all the thread/fiber/event/actor-based
concurrency models and Rack middleware that Rainbows! supports (or will
ever support) in a single process.

## 官网

- 主页: http://zbatery.bogomip.org/
- 源码仓库: http://git.bogomips.org/cgit/zbatery.git
- RubyGems: https://rubygems.org/gems/zbatery

## 历史版本号

- 4.0.0 (2011-06-27)
- 3.4.0 (2011-05-21)
- 3.3.0 (2011-05-16)
- 3.1.0 (2011-02-11)
- 3.0.0 (2011-01-12)
- 0.6.0 (2010-12-29)
- 0.5.0 (2010-11-20)
- 0.4.0 (2010-10-28)
- 0.3.1 (2010-07-11)
- 0.3.0 (2010-07-10)
- 0.2.1 (2010-04-19)
- 0.2.0 (2010-03-01)
- 0.1.1 (2010-02-13)
- 0.1.0 (2009-12-22)
- 0.0.0 (2009-12-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/zbatery
- gem 安装: `gem install zbatery`
- Bundler: `gem "zbatery"`
- 最新版本: 4.0.0
- 最新版归档: https://rubygems.org/downloads/zbatery-4.0.0.gem
- 版本锁定: `gem "zbatery", "~> 4.0.0"`
- 中央仓库: https://rubygems.org/
