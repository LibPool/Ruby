# edouard-clarity

**Tag**: web, filesystem

## 简介

Clarity - a log search tool
By John Tajima & Tobi Lütke

Clarity is a Splunk like web interface for your server log files. It supports 
searching (using grep) as well as trailing log files in realtime. It has been written 
using the event based architecture based on EventMachine and so allows real-time search
of very large log files. If you hit the browser Stop button it will also kill 
the grep / tail utility. 

We wrote Clarity to allow our support staff to use a simple interface to look
through the various log files in our server farm. The application was such a 
big success internally that we decided to release it as open source.

## 官网

- 主页: http://github.com/tobi/clarity
- RubyGems: https://rubygems.org/gems/edouard-clarity

## 历史版本号

- 0.9.9 (2010-03-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/edouard-clarity
- gem 安装: `gem install edouard-clarity`
- Bundler: `gem "edouard-clarity"`
- 最新版本: 0.9.9
- 最新版归档: https://rubygems.org/downloads/edouard-clarity-0.9.9.gem
- 版本锁定: `gem "edouard-clarity", "~> 0.9.9"`
- 中央仓库: https://rubygems.org/
