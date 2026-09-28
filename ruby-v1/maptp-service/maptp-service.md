# maptp-service

**Tag**: web, cli, networking

## 简介

This gem provides access to the MapTP web services.

In order to use them, you need your MapTP credentials aka your Map24 id.

For more information head over to http://www.nn4d.com

You should consider that this client solely works with WGS´84 coordinates in the Decimal Degrees format.
Usually MapTP services work with the Decimal Minutes format, but because Decimal Degrees are much more
established we use it for this lib. To work with MapTP the parameters as well as the responses are
converted internally.

*Note*: This is *not* an official client of MapTP or NAVTEQ, but a private project. :)

## 官网

- 源码仓库: http://github.com/fabrik42/maptp-service
- 问题追踪: http://github.com/fabrik42/maptp-service/issues
- RubyGems: https://rubygems.org/gems/maptp-service

## 历史版本号

- 0.0.3 (2010-10-21)
- 0.0.2 (2010-05-23)
- 0.0.1 (2010-05-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/maptp-service
- gem 安装: `gem install maptp-service`
- Bundler: `gem "maptp-service"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/maptp-service-0.0.3.gem
- 版本锁定: `gem "maptp-service", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
