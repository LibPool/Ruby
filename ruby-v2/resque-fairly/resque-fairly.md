# resque-fairly

**Tag**: library

## 简介

Normally resque processes queues in a fixed order.  This can lead to jobs in queues at the end of the list not getting process for very long periods.  resque-fairly provides a mechanism where by workers are distributed across the set of queues with pending jobs fairly.  This results in a much more predictable mean time to handling for jobs in queues that are not the first in the list.

## 官网

- 主页: http://github.com/openlogic/resque-fairly
- 文档: https://www.rubydoc.info/gems/resque-fairly/1.4.1
- RubyGems: https://rubygems.org/gems/resque-fairly

## 历史版本号

- 1.4.1 (2015-01-19)
- 1.1.0 (2011-03-04)
- 1.0.1 (2010-08-23)
- 1.0.0 (2010-08-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-fairly
- gem 安装: `gem install resque-fairly`
- Bundler: `gem "resque-fairly"`
- 最新版本: 1.4.1
- 最新版归档: https://rubygems.org/downloads/resque-fairly-1.4.1.gem
- 版本锁定: `gem "resque-fairly", "~> 1.4.1"`
- 中央仓库: https://rubygems.org/
