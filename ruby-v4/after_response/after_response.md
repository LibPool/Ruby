# after_response

**Tag**: cli, data

## 简介

AfterResponse provides callbacks into the Passenger2.2, Passenger3 and Unicorn
request cycle. The main goal is to delay as much non-critical processing until later, delivering
the response to the client application sooner. This would mainly include logging data into a Observatory-like
event logging service, sending email and other tasks that do not affect the response body in any way.

## 官网

- 主页: https://github.com/kevn/after_response
- RubyGems: https://rubygems.org/gems/after_response

## 历史版本号

- 0.9.3 (2011-05-03)
- 0.9.2 (2010-12-27)
- 0.9.1 (2010-12-16)
- 0.9 (2010-12-16)
- 0.8 (2010-12-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/after_response
- gem 安装: `gem install after_response`
- Bundler: `gem "after_response"`
- 最新版本: 0.9.3
- 最新版归档: https://rubygems.org/downloads/after_response-0.9.3.gem
- 版本锁定: `gem "after_response", "~> 0.9.3"`
- 中央仓库: https://rubygems.org/
