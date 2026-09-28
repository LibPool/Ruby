# box_layout

**Tag**: web, networking, template

## 简介

Allows you to lay out HTML using ASCII art. Stolen from psykotic's code posted to reddit: http://programming.reddit.com/info/k9dx/comments  == SYNOPSIS:  require 'box_layout'  page_template = &lt;&lt;-END ---------- |        | ---------- | |    | | | |    | | | |    | | | |    | | ---------- |        | ---------- END  layout = BoxLayout.html page_template puts &quot;&lt;title&gt;cute&lt;/title&gt;&quot; puts &quot;&lt;style&gt;* { border: 1px solid black }&lt;/style&gt;&quot; puts layout % %w[header left body right footer].map {|s| &quot;**#{s}**&quot; }  == REQUIREMENTS:

## 官网

- 主页: http://seattlerb.rubyforge.org/
- RubyGems: https://rubygems.org/gems/box_layout

## 历史版本号

- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/box_layout
- gem 安装: `gem install box_layout`
- Bundler: `gem "box_layout"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/box_layout-1.0.0.gem
- 版本锁定: `gem "box_layout", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
