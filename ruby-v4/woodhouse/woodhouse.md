# woodhouse

**Tag**: web, cli, testing

## 简介

An AMQP-based background worker system for Ruby designed to make managing heterogenous tasks relatively easy.
  
  The use case for Woodhouse is for reliable and sane performance in situations where jobs on a single queue may vary significantly in length. The goal is to permit large numbers of quick jobs to be serviced even when many slow jobs are in the queue. A secondary goal is to provide a sane way for jobs on a given queue to be given special priority or dispatched to a server more suited to them.
  
  Clients (i.e., your application) may be using either Ruby 1.9 in any VM.

## 官网

- 主页: http://github.com/mboeh/woodhouse
- 文档: https://www.rubydoc.info/gems/woodhouse/1.0.0
- RubyGems: https://rubygems.org/gems/woodhouse

## 历史版本号

- 1.0.0 (2014-08-26)
- 0.1.5 (2013-04-13)
- 0.1.2 (2013-03-05)
- 0.1.1 (2013-03-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/woodhouse
- gem 安装: `gem install woodhouse`
- Bundler: `gem "woodhouse"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/woodhouse-1.0.0.gem
- 版本锁定: `gem "woodhouse", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
