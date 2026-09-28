# mockingbird

**Tag**: web, testing, networking, data

## 简介

Mockingbird emulates the Twitter Streaming API using a simple script-like 
    configuration that makes it easy to test code that connects to the Streaming 
    API. Mockingbird can be used to simulate bad data, unexpected status codes, 
    hard disconnects, etc.
    
    Mockingbird uses eventmachine to run as an actual streaming http server so
    it's a drop-in replacement for code that reads from the streaming api. 
    Simply change the host and port your code is connecting to from Twitter to 
    a running Mockingbird.

## 官网

- 主页: http://github.com/hayesdavis/mockingbird
- RubyGems: https://rubygems.org/gems/mockingbird

## 历史版本号

- 0.2.0 (2012-02-21)
- 0.1.1 (2012-02-18)
- 0.1.0 (2010-07-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/mockingbird
- gem 安装: `gem install mockingbird`
- Bundler: `gem "mockingbird"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/mockingbird-0.2.0.gem
- 版本锁定: `gem "mockingbird", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
