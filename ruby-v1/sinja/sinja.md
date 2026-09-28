# sinja

**Tag**: web, testing, serialization, template, tooling, data

## 简介

Sinja is a Sinatra extension for quickly building RESTful,
{json:api}-compliant web services, leveraging the excellent
JSONAPI::Serializers gem for payload serialization. It enhances Sinatra's
DSL to enable resource-, relationship-, and role-centric API development,
and it configures Sinatra with the proper settings, MIME-types, filters,
conditions, and error-handling.

There are many parsing (deserializing), rendering (serializing), and other
"JSON API" libraries available for Ruby, but relatively few that attempt to
correctly implement the entire {json:api} server specification, including
routing, request header and query parameter checking, and relationship
side-loading. Sinja lets you focus on the business logic of your
applications without worrying about the specification, and without pulling
in a heavy framework like Rails. It's lightweight, ORM-agnostic, and
Ember.js-friendly!

## 官网

- 主页: http://sinja-rb.org
- 文档: https://www.rubydoc.info/gems/sinja/1.3.0
- RubyGems: https://rubygems.org/gems/sinja

## 历史版本号

- 1.3.0 (2017-10-27)
- 1.2.5 (2017-03-08)
- 1.2.4 (2017-02-13)
- 1.2.3 (2017-01-11)
- 1.2.2 (2016-12-18)
- 1.2.1 (2016-12-18)
- 1.2.0.pre3 (2016-12-15)
- 1.2.0.pre2 (2016-12-14)
- 1.1.0.pre4 (2016-12-08)
- 1.1.0.pre3 (2016-12-07)
- 1.1.0.pre2 (2016-12-07)
- 1.1.0.pre1 (2016-12-06)
- 1.0.0.pre2 (2016-12-02)
- 1.0.0.pre1 (2016-12-02)
- 0.2.0.beta2 (2016-11-20)
- 0.2.0.beta1 (2016-11-20)
- 0.1.0.beta3 (2016-11-10)
- 0.1.0.beta2 (2016-11-09)
- 0.1.0.beta1 (2016-11-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/sinja
- gem 安装: `gem install sinja`
- Bundler: `gem "sinja"`
- 最新版本: 1.3.0
- 最新版归档: https://rubygems.org/downloads/sinja-1.3.0.gem
- 版本锁定: `gem "sinja", "~> 1.3.0"`
- 中央仓库: https://rubygems.org/
