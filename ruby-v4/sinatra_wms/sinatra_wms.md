# sinatra_wms

**Tag**: web, testing, networking, template, tooling, data

## 简介

A WMS (Web Map Service) is a great way to show lots of geolocated data on a map. Instead of generating static images (which will either be huge or don't have enough resolution), a WMS allows you to dynamically zoom in and out of your dataset.

This gem allows you to very easily represent your data via a WMS. On one hand it extends Sinatra to give it a method called "wms" to process WMS-requests; on the other hand it extends RMagick to allow the developer to use coordinates in the methods used for drawing.

Convenient methods to easily generate HTML code to show your WMS data on top of OpenStreetMaps or Google Maps are also included.

Current test status: [![Build Status](https://secure.travis-ci.org/fabianonline/sinatra_wms.png?branch=master)](http://travis-ci.org/fabianonline/sinatra_wms)

## 官网

- 主页: http://github.com/fabianonline/sinatra_wms
- 源码仓库: https://github.com/fabianonline/sinatra_wms/
- 文档: https://github.com/fabianonline/sinatra_wms/blob/master/README.rdoc
- RubyGems: https://rubygems.org/gems/sinatra_wms

## 历史版本号

- 0.1.1 (2012-04-28)
- 0.1.0 (2012-04-24)
- 0.0.2 (2012-04-23)
- 0.0.1 (2012-04-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/sinatra_wms
- gem 安装: `gem install sinatra_wms`
- Bundler: `gem "sinatra_wms"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/sinatra_wms-0.1.1.gem
- 版本锁定: `gem "sinatra_wms", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
