# fnf

**Tag**: web, cli

## 简介

Fire and Forget replaces the need to write resque tasks or delayed jobs to fire off web requests (usually notification webhooks or a anti-spam service, like defensio or akismet). A single worker reads and executes web requests from a blocking named pipe, while clients queue up them up in a non blocking manner. It uses typhoeus internally to execute the web requests for maximum speed.

## 官网

- 主页: http://www.github.com/capotej/fnf
- RubyGems: https://rubygems.org/gems/fnf

## 历史版本号

- 1.0.1 (2011-05-28)
- 1.0.0 (2011-05-28)
- 0.0.2 (2011-05-28)
- 0.0.1 (2011-05-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/fnf
- gem 安装: `gem install fnf`
- Bundler: `gem "fnf"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/fnf-1.0.1.gem
- 版本锁定: `gem "fnf", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
