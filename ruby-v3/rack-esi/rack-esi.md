# rack-esi

**Tag**: web, serialization, networking, template

## 简介

Rack-ESI is a Nokogiri based ESI middleware implementation for Rack with support for include tags, all other ESI namespaced nodes are just removed.
To make this gem work you must define the (xmlns:esi)[http://www.edge-delivery.org/esi/1.0] namespace in your text/html response.
Note: This gem should only be used in development. For production use setup varnish or any other ESI enabled server.

## 官网

- 源码仓库: https://github.com/boof/rack-esi
- 文档: http://rdoc.info/github/boof/rack-esi/master/frames
- 问题追踪: https://github.com/boof/rack-esi/issues
- RubyGems: https://rubygems.org/gems/rack-esi

## 历史版本号

- 0.2.0 (2011-09-30)
- 0.1.2 (2009-11-27)
- 0.1.1 (2009-11-26)
- 0.1.0 (2009-11-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-esi
- gem 安装: `gem install rack-esi`
- Bundler: `gem "rack-esi"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/rack-esi-0.2.0.gem
- 版本锁定: `gem "rack-esi", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
