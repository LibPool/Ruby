# goran

**Tag**: testing, networking, tooling

## 简介

Named after Goran Invanisevic, the tennis legend who won the Wimbledon after losing the final 3 times, 
    Goran provides a simple syntax to run a block of code multiple times. E.g.
    
    * run block 'x' number of times
    * run until the block returns a non-nil value
    * run until the block does not raise an exception
    * run until the block returns a non-zero value, to a maximum of 3 times, and return nil if all runs return a 0
    
    Goran is especially useful for running network calls which have unexpected outputs like 404, timeouts. It is an
    easy way to build in retry logic into these calls and handle cases where these calls do not succeed at all.

## 官网

- 主页: http://github.com/wallwisher/goran
- RubyGems: https://rubygems.org/gems/goran

## 历史版本号

- 0.6 (2012-05-01)
- 0.5 (2012-05-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/goran
- gem 安装: `gem install goran`
- Bundler: `gem "goran"`
- 最新版本: 0.6
- 最新版归档: https://rubygems.org/downloads/goran-0.6.gem
- 版本锁定: `gem "goran", "~> 0.6"`
- 中央仓库: https://rubygems.org/
