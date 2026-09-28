# flamingo

**Tag**: web, database

## 简介

Flamingo makes it easy to wade through the Twitter Streaming API by 
    handling all connectivity and resource management for you. You just tell 
    it what to track and consume the information in a resque queue. 

    Flamingo isn't a traditional ruby gem. You don't require it into your code.
    Instead, it's designed to run as a daemon like redis or mysql. It provides 
    a REST interface to change the parameters sent to the Twitter Streaming 
    resource. All events from the streaming API are placed on a resque job 
    queue where your application can process them.
    
    CAVEAT EMPTOR: This gem is alpha code so act accordingly.

## 官网

- 主页: http://github.com/hayesdavis/flamingo
- RubyGems: https://rubygems.org/gems/flamingo

## 历史版本号

- 0.4.0 (2011-02-11)
- 0.3.1 (2010-11-27)
- 0.2.1 (2010-10-26)
- 0.2.0 (2010-08-02)
- 0.1 (2010-07-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/flamingo
- gem 安装: `gem install flamingo`
- Bundler: `gem "flamingo"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/flamingo-0.4.0.gem
- 版本锁定: `gem "flamingo", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
