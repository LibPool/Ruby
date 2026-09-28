# name_parse

**Tag**: web, networking, tooling

## 简介

=========================================================
Name Parse
Copyright (c) 2009 The Rubyists (Jayson Vaughn, Tj Vanderpoel, Michael Fellinger, Kevin Berry) 
Distributed under the terms of the MIT License.
==========================================================

About
-----
A ruby library for turning arbitrary name strings such as "Dr Helen Hunt", "Mr James T. Kirk" into a 
standardized object usable as 
  parsed = NameParse::Parser.new("Dr Helen Hunt")
  puts "%s %s" % [parsed.first, parsed.last]


Requirements
------------
- ruby (>= 1.8)

Usage
-----

Example of using on a list:

  bougyman@zero:~/git_checkouts/name_parse$ irb -r lib/name_parse
  irb(main):001:0> list = ["Jayson Vaughn", "Dr Helen Hunt",  "Mr James T. Kirk"]
  => ["Jayson Vaughn", "Dr Helen Hunt", "Mr James T. Kirk"]
  irb(main):002:0> list.map { |n| p = NameParse[n]; [p.first, p.last] }
  => [["Jayson", "Vaughn"], ["Helen", "Hunt"], ["James", "Kirk"]]


Support
-------
Home page at http://github.com/bougyman/name_parse
#rubyists on FreeNode

## 官网

- 主页: http://github.com/bougyman/name_parse
- RubyGems: https://rubygems.org/gems/name_parse

## 历史版本号

- 0.0.5 (2011-02-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/name_parse
- gem 安装: `gem install name_parse`
- Bundler: `gem "name_parse"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/name_parse-0.0.5.gem
- 版本锁定: `gem "name_parse", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
