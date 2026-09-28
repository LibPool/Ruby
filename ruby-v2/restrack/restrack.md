# restrack

**Tag**: web, testing, serialization, template, tooling, filesystem, data

## 简介

RESTRack is a Rack-based MVC framework that makes it extremely easy to develop RESTful data services. It is inspired by
Rails, and follows a few of its conventions.  But it has no routes file, routing relationships are done through
supplying custom code blocks to class methods such as "has_relationship_to" or "has_mapped_relationships_to".

RESTRack aims at being lightweight and easy to use.  It will automatically render JSON and XML for the data
structures you return in your actions (any structure parsable by the "json" and
"xml-simple" gems, respectively).

If you supply a view for a controller action, you do that using a builder file.  Builder files are stored in the
view directory grouped by controller name subdirectories (`view/<controller>/<action>.xml.builder`).  XML format
requests will then render the view template with the builder gem, rather than generating XML with XmlSimple.

## 官网

- 主页: http://github.com/stjohncj/RESTRack
- 源码仓库: https://github.com/RESTRack/RESTRack
- RubyGems: https://rubygems.org/gems/restrack

## 历史版本号

- 1.8.2 (2013-01-29)
- 1.8.1 (2013-01-23)
- 1.7.0 (2013-01-03)
- 1.6.9 (2012-12-20)
- 1.6.8 (2012-11-14)
- 1.6.7 (2012-10-16)
- 1.6.6 (2012-10-03)
- 1.6.5 (2012-10-01)
- 1.6.4 (2012-08-30)
- 1.6.3 (2012-08-21)
- 1.6.2 (2012-08-21)
- 1.6.1 (2012-07-12)
- 1.6.0 (2012-07-05)
- 1.5.1 (2012-05-22)
- 1.5.0 (2012-05-16)
- 1.4.3 (2012-05-08)
- 1.4.2 (2012-05-03)
- 1.4.1 (2012-03-20)
- 1.4.0 (2012-02-22)
- 1.3.4 (2012-02-14)
- 1.3.3 (2012-01-13)
- 1.3.2 (2012-01-13)
- 1.3.1 (2011-12-13)
- 1.3.0 (2011-11-16)
- 1.2.6 (2011-11-01)
- 1.2.5 (2011-10-21)
- 1.2.4 (2011-10-10)
- 1.2.3 (2011-10-10)
- 1.2.2 (2011-10-07)
- 1.2.1 (2011-10-07)
- 1.2.0 (2011-10-06)
- 1.1.9 (2011-09-23)
- 1.1.8 (2011-09-22)
- 1.1.7 (2011-09-16)
- 1.1.6 (2011-09-15)
- 1.1.5 (2011-09-14)
- 1.1.3 (2011-09-08)
- 1.1.2 (2011-09-08)
- 1.1.1 (2011-07-18)
- 1.1.0 (2011-07-11)
- 1.0.0 (2011-05-18)
- 0.1.4 (2011-03-27)
- 0.1.3 (2011-02-13)
- 0.1.2 (2011-02-13)
- 0.1.1 (2011-02-06)
- 0.1.0 (2011-02-06)
- 0.0.6 (2011-02-05)
- 0.0.5 (2011-01-27)
- 0.0.3 (2011-01-26)
- 0.0.2 (2011-01-26)
- 0.0.1 (2011-01-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/restrack
- gem 安装: `gem install restrack`
- Bundler: `gem "restrack"`
- 最新版本: 1.8.2
- 最新版归档: https://rubygems.org/downloads/restrack-1.8.2.gem
- 版本锁定: `gem "restrack", "~> 1.8.2"`
- 中央仓库: https://rubygems.org/
