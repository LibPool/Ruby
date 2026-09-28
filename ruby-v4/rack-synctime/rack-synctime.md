# rack-synctime

**Tag**: web, networking

## 简介

Rack::Synctime is a simple Rack middleware that returns sync time (time when request started) in HTTP headers (#{Rack::Synctime::DEFAULT_HEADER_NAME} by default). Header name can be changed also sync time can be modified using time offset i.e. -5 seconds (server time in seconds decreased by 5) etc. This can be useful if you develop mobile applications (Android, iOS, ...) and you need information when request started in response header.

## 官网

- 主页: https://github.com/b-wojtowicz/rack-synctime
- RubyGems: https://rubygems.org/gems/rack-synctime

## 历史版本号

- 0.0.2 (2013-03-17)
- 0.0.1 (2013-03-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-synctime
- gem 安装: `gem install rack-synctime`
- Bundler: `gem "rack-synctime"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/rack-synctime-0.0.2.gem
- 版本锁定: `gem "rack-synctime", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
