# soup-ruby

**Tag**: web, networking

## 简介

Libsoup bindings for ruby.  Partial coverage sufficient to allow HTTP requests to be handled without blocking the mainloop.

e.g
require 'gtk2'
require 'soup'


message = Soup::Message.new("GET", "http://www.example.com/")
Soup::SessionAsync.new.queue(message) do |_sess,_mess|
  puts "Got response"
  Gtk.main_quit
end

Gtk.main

## 官网

- 主页: http://github.com/geoffyoungs/soup-ruby
- 文档: https://www.rubydoc.info/gems/soup-ruby/0.0.10
- RubyGems: https://rubygems.org/gems/soup-ruby

## 历史版本号

- 0.0.10 (2016-08-31)
- 0.0.9 (2016-08-31)
- 0.0.8 (2016-06-08)
- 0.0.7 (2013-09-05)
- 0.0.6 (2013-09-04)
- 0.0.5 (2013-08-22)
- 0.0.4 (2013-08-16)
- 0.0.2 (2013-03-05)
- 0.0.1 (2013-03-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/soup-ruby
- gem 安装: `gem install soup-ruby`
- Bundler: `gem "soup-ruby"`
- 最新版本: 0.0.10
- 最新版归档: https://rubygems.org/downloads/soup-ruby-0.0.10.gem
- 版本锁定: `gem "soup-ruby", "~> 0.0.10"`
- 中央仓库: https://rubygems.org/
