# rabbit-slide-pmq20-tracing-a-memory-leak-in-a-long-running-eventmachine-application

**Tag**: web

## 简介

In Huanteng Smart we manufacture smart household gadgets which all connect to a single long running eventmachine application to receive and send instructions with the server. This eventmachine application is a single Linux process holding all TCP connections never closes them. One day, we found that this process was leaking memory, and here is how we managed to trace its cause.

## 官网

- 主页: http://slide.rabbit-shocker.org/authors/pmq20/tracing-a-memory-leak-in-a-long-running-eventmachine-application/
- 文档: https://www.rubydoc.info/gems/rabbit-slide-pmq20-tracing-a-memory-leak-in-a-long-running-eventmachine-application/1.0.0
- RubyGems: https://rubygems.org/gems/rabbit-slide-pmq20-tracing-a-memory-leak-in-a-long-running-eventmachine-application

## 历史版本号

- 1.0.0 (2014-12-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/rabbit-slide-pmq20-tracing-a-memory-leak-in-a-long-running-eventmachine-application
- gem 安装: `gem install rabbit-slide-pmq20-tracing-a-memory-leak-in-a-long-running-eventmachine-application`
- Bundler: `gem "rabbit-slide-pmq20-tracing-a-memory-leak-in-a-long-running-eventmachine-application"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/rabbit-slide-pmq20-tracing-a-memory-leak-in-a-long-running-eventmachine-application-1.0.0.gem
- 版本锁定: `gem "rabbit-slide-pmq20-tracing-a-memory-leak-in-a-long-running-eventmachine-application", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
