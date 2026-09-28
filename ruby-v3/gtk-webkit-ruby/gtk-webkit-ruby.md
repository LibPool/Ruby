# gtk-webkit-ruby

**Tag**: web, template

## 简介

Gtk Webkit bindings for ruby.  Partial coverage sufficient to embed a webview in a Ruby-GNOME2 application.

Also initial/experimental support for allowing ruby code to be called by javascript & executing javascript
from ruby.

e.g
require 'gtk2'
require 'webkit'

v = WebKit::WebView.new
v.main_frame.setup_ruby
puts v.main_frame.exec_js("ruby_eval('RUBY_DESCRIPTION')")
puts v.main_frame.exec_js("document.root.innerHTML")

## 官网

- 主页: http://github.com/geoffyoungs/gtk-webkit-ruby
- 文档: https://www.rubydoc.info/gems/gtk-webkit-ruby/0.0.8
- RubyGems: https://rubygems.org/gems/gtk-webkit-ruby

## 历史版本号

- 0.0.8 (2013-08-12)
- 0.0.7 (2013-08-12)
- 0.0.6 (2013-06-14)
- 0.0.5 (2013-01-24)
- 0.0.4 (2012-11-16)
- 0.0.3 (2012-04-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/gtk-webkit-ruby
- gem 安装: `gem install gtk-webkit-ruby`
- Bundler: `gem "gtk-webkit-ruby"`
- 最新版本: 0.0.8
- 最新版归档: https://rubygems.org/downloads/gtk-webkit-ruby-0.0.8.gem
- 版本锁定: `gem "gtk-webkit-ruby", "~> 0.0.8"`
- 中央仓库: https://rubygems.org/
