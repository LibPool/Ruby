# drnic-liquid

**Tag**: web, testing, template

## 简介

A secure non evaling end user template engine with aesthetic markup.

Liquid is a template engine which I wrote for very specific requirements.

* It has to have beautiful and simple markup. 
  Template engines which don't produce good looking markup are no fun to use. 
* It needs to be non evaling and secure. Liquid templates are made so that users can edit them. You don't want to run code on your server which your users wrote. 
* It has to be stateless. Compile and render steps have to be seperate so that the expensive parsing and compiling can be done once and later on you can 
  just render it   passing in a hash with local variables and objects.

## 官网

- 主页: http://www.liquidmarkup.org
- RubyGems: https://rubygems.org/gems/drnic-liquid

## 历史版本号

- 2.1.0 (2009-10-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/drnic-liquid
- gem 安装: `gem install drnic-liquid`
- Bundler: `gem "drnic-liquid"`
- 最新版本: 2.1.0
- 最新版归档: https://rubygems.org/downloads/drnic-liquid-2.1.0.gem
- 版本锁定: `gem "drnic-liquid", "~> 2.1.0"`
- 中央仓库: https://rubygems.org/
