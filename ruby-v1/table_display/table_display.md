# table_display

**Tag**: web, cli, testing, serialization, template, data

## 简介

Adds support for displaying your ActiveRecord tables, named scopes, collections, or
plain arrays in a table view when working in rails console, shell, or email template.

Enumerable#to_table_display returns the printable strings; Object#pt calls #to_table_display on its
first argument and puts out the result.

Columns you haven't loaded (eg. from using :select) are omitted, and derived/calculated
columns (eg. again, from using :select) are added.

Both #to_table_display and Object#pt methods take :only, :except, and :methods which work like
the #to_xml method to change what attributes/methods are output.

The normal output uses #inspect on the data values to make them printable, so you can
see what type the values had.  When that's inconvenient or you'd prefer direct display,
you can pass the option :inspect => false to disable inspection.

## 官网

- 主页: http://github.com/willbryant/table_display
- 文档: https://www.rubydoc.info/gems/table_display/3.0.0
- RubyGems: https://rubygems.org/gems/table_display

## 历史版本号

- 3.0.0 (2025-11-07)
- 2.2.0 (2020-02-18)
- 2.1.0 (2018-10-17)
- 2.0.0 (2016-09-04)
- 1.0.0 (2013-04-21)
- 0.5.1 (2012-08-18)
- 0.5.0 (2012-08-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/table_display
- gem 安装: `gem install table_display`
- Bundler: `gem "table_display"`
- 最新版本: 3.0.0
- 最新版归档: https://rubygems.org/downloads/table_display-3.0.0.gem
- 版本锁定: `gem "table_display", "~> 3.0.0"`
- 中央仓库: https://rubygems.org/
