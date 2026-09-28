# auser-macmap

**Tag**: library

## 简介

= macmap  Ever wanted to map your interface to an ip?  If you haven't, why not?  Alas, Macmap is here to help!  Usage is easy:  Macmap.map_iface_to_ip %{ifconfig -a}  Or  require "rubygems" require "popen3"  Open3.popen3('ifconfig -a') { |stdin, stdout, stderr| Macmap.map_iface_to_ip(stdout) }    Try it! It's fun  == Copyright  Copyright (c) 2009 Ari Lerner. See LICENSE for details.

## 官网

- 主页: http://github.com/auser/macmap
- 文档: https://www.rubydoc.info/gems/auser-macmap/0.0.2
- RubyGems: https://rubygems.org/gems/auser-macmap

## 历史版本号

- 0.0.1 (2014-08-11)
- 0.0.2 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/auser-macmap
- gem 安装: `gem install auser-macmap`
- Bundler: `gem "auser-macmap"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/auser-macmap-0.0.2.gem
- 版本锁定: `gem "auser-macmap", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
