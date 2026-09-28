# glader

**Tag**: template, filesystem

## 简介

Glader is a tiny helper script that works with ruby-glade-create-template to create a Ruby program that will show a Glade form. ruby-glade-create-template only creates a class and doesn't actually show the window, and if you change that class subsequent runs of the script will overwrite your changes.   Glader makes a main file that uses the class and extends it, so you can change your glade file and regenerate it as often as you like, keeping code changes in the main file.  ruby-glade-create-template is part of libglade2-ruby1.8 on my Ubuntu system.

## 官网

- 主页: http://www.lesismore.co.za
- RubyGems: https://rubygems.org/gems/glader

## 历史版本号

- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/glader
- gem 安装: `gem install glader`
- Bundler: `gem "glader"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/glader-1.0.0.gem
- 版本锁定: `gem "glader", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
