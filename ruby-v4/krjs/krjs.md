# krjs

**Tag**: cli, template

## 简介

RJS is a great Ruby DSL to write javascript. However, it's so tempting to write RJS directly in the views, and soon the views contain substantial controller knowledge (e.g. link_to_remote, link_to, etc)  KRJS attempts to solve that problem by allowing dynamic inclusion of AJAX calls on HTML elements. When a controller defines a method (based on naming convention) that handles a client-side event, the rendering engine will do the wiring  automatically - when the event happens, an AJAX call will be made to the controller's method which would ideally reply  with RJS and update portions of the document.

## 官网

- 主页: http://github.com/gbdev/krjs
- RubyGems: https://rubygems.org/gems/krjs

## 历史版本号

- 0.5.5 (2010-02-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/krjs
- gem 安装: `gem install krjs`
- Bundler: `gem "krjs"`
- 最新版本: 0.5.5
- 最新版归档: https://rubygems.org/downloads/krjs-0.5.5.gem
- 版本锁定: `gem "krjs", "~> 0.5.5"`
- 中央仓库: https://rubygems.org/
