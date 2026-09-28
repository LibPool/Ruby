# dead_simple_cms

**Tag**: web, database, testing, template, tooling, data

## 简介

Dead Simple CMS is a library for modifying different parts of your website without the overhead of having a
fullblown CMS. The idea with this library is simple: provide an easy way to hook into different parts of your
application (not only views) by defining the different parts to modify in an easy, straight-forward DSL.

The basic components of this library include:

 * A DSL to define the changeable values in your app
 * Form generators based on SimpleForm (with or without Bootstrap) and default rails FormBuilder
 * Expandable storage mechanisms so you can store the data in different locations
   * Currently supported: Redis, Database, Memcache, even Memory (for testing)
 * Presenters/renderers so you can take groups of variables and render them into your views (ie image_tag)

What it doesn't have:

 * Versioning - be able to look at old versions of the content
 * Timing - set start and end time for different content
 * Page builder tools - this is not the right tool if you want to design full pages

## 官网

- 主页: http://github.com/Aryk/dead_simple_cms
- 文档: https://www.rubydoc.info/gems/dead_simple_cms/0.12.11
- RubyGems: https://rubygems.org/gems/dead_simple_cms

## 历史版本号

- 0.12.11 (2019-03-12)
- 0.12.10 (2015-07-29)
- 0.12.9 (2015-05-28)
- 0.12.8 (2014-10-22)
- 0.12.7 (2014-08-29)
- 0.12.6 (2014-08-27)
- 0.12.4 (2013-05-07)
- 0.12.3 (2013-04-24)
- 0.12.1 (2013-04-22)
- 0.12.0 (2013-04-19)
- 0.11.1 (2013-01-28)
- 0.11.0 (2012-12-07)
- 0.10.1 (2012-09-13)
- 0.10.0 (2012-06-29)
- 0.9.4 (2012-06-26)
- 0.9.3 (2012-06-26)
- 0.9.2 (2012-06-25)
- 0.9.1 (2012-06-24)
- 0.9.0 (2012-06-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/dead_simple_cms
- gem 安装: `gem install dead_simple_cms`
- Bundler: `gem "dead_simple_cms"`
- 最新版本: 0.12.11
- 最新版归档: https://rubygems.org/downloads/dead_simple_cms-0.12.11.gem
- 版本锁定: `gem "dead_simple_cms", "~> 0.12.11"`
- 中央仓库: https://rubygems.org/
