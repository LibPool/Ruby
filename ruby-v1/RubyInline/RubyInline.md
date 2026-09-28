# RubyInline

**Tag**: web, template, tooling

## 简介

Inline allows you to write foreign code within your ruby code. It
automatically determines if the code in question has changed and
builds it only when necessary. The extensions are then automatically
loaded into the class/module that defines it.

You can even write extra builders that will allow you to write inlined
code in any language. Use Inline::C as a template and look at
Module#inline for the required API.

== Features/Problems:

* Quick and easy inlining of your C or C++ code embedded in your ruby script.
* Extendable to work with other languages.
* Automatic conversion between ruby and C basic types
  * char, unsigned, unsigned int, char *, int, long, unsigned long
* inline_c_raw exists for when the automatic conversion isn't sufficient.
* Only recompiles if the inlined code has changed.
* Pretends to be secure.
* Only requires standard ruby libraries, nothing extra to download.

## 官网

- 主页: https://zenspider.com/projects/rubyinline.html
- 源码仓库: https://github.com/seattlerb/rubyinline
- 文档: https://docs.seattlerb.org/RubyInline/
- RubyGems: https://rubygems.org/gems/RubyInline

## 历史版本号

- 3.14.4 (2026-03-29)
- 3.14.3 (2026-02-03)
- 3.14.2 (2025-03-12)
- 3.14.1 (2024-06-23)
- 3.14.0 (2023-06-28)
- 3.13.0 (2023-02-01)
- 3.12.6 (2022-05-23)
- 3.12.5 (2019-10-09)
- 3.12.4 (2015-04-15)
- 3.12.3 (2014-04-29)
- 3.12.2 (2013-04-18)
- 3.12.1 (2013-02-15)
- 3.12.0 (2012-12-18)
- 3.11.4 (2012-11-23)
- 3.11.3 (2012-07-05)
- 3.11.2 (2012-02-22)
- 3.11.1 (2012-01-25)
- 3.11.0 (2011-09-28)
- 3.10.1 (2011-09-13)
- 3.10.0 (2011-08-31)
- 3.9.0 (2011-02-18)
- 3.8.6 (2010-09-03)
- 3.8.5 (2010-09-01)
- 3.8.4 (2009-12-10)
- 3.8.3 (2009-08-09)
- 3.8.2 (2009-08-05)
- 3.6.2 (2009-07-25)
- 3.6.1 (2009-07-25)
- 3.6.0 (2009-07-25)
- 3.5.0 (2009-07-25)
- 3.4.0 (2009-07-25)
- 3.3.2 (2009-07-25)
- 3.3.1 (2009-07-25)
- 3.3.0 (2009-07-25)
- 3.2.1 (2009-07-25)
- 3.2.0 (2009-07-25)
- 3.1.0 (2009-07-25)
- 3.8.1 (2009-07-25)
- 3.8.0 (2009-07-25)
- 3.7.0 (2009-07-25)
- 3.6.7 (2009-07-25)
- 3.6.6 (2009-07-25)
- 3.6.5 (2009-07-25)
- 3.6.4 (2009-07-25)
- 3.6.3 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/RubyInline
- gem 安装: `gem install RubyInline`
- Bundler: `gem "RubyInline"`
- 最新版本: 3.14.4
- 最新版归档: https://rubygems.org/downloads/RubyInline-3.14.4.gem
- 版本锁定: `gem "RubyInline", "~> 3.14.4"`
- 中央仓库: https://rubygems.org/
