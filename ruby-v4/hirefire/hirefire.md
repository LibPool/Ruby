# hirefire

**Tag**: library

## 简介

HireFire automatically "hires" and "fires" (aka "scales") Delayed Job and Resque workers on Heroku. When there are no queue jobs, HireFire will fire (shut down) all workers. If there are queued jobs, then it'll hire (spin up) workers. The amount of workers that get hired depends on the amount of queued jobs (the ratio can be configured by you). HireFire is great for both high, mid and low traffic applications. It can save you a lot of money by only hiring workers when there are pending jobs, and then firing them again once all the jobs have been processed. It's also capable to dramatically reducing processing time by automatically hiring more workers when the queue size increases.

## 官网

- 主页: http://rubygems.org/gems/hirefire
- RubyGems: https://rubygems.org/gems/hirefire

## 历史版本号

- 0.1.4 (2011-06-28)
- 0.1.3 (2011-05-01)
- 0.1.2 (2011-05-01)
- 0.1.1 (2011-04-15)
- 0.1.0 (2011-04-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/hirefire
- gem 安装: `gem install hirefire`
- Bundler: `gem "hirefire"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/hirefire-0.1.4.gem
- 版本锁定: `gem "hirefire", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
