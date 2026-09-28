# rutema_web

**Tag**: web, database, testing, serialization, networking, template, filesystem, data

## 简介

== DESCRIPTION:
rutema_web is the web frontend for rutema. 

It can be used as a viewer for database files created with the rutema ActiveRecord reporter.
It also provides you with some basic statistics about the tests in your database in the form of 
diagrams of debatable aesthetics but undoubtable value!

== SYNOPSIS:
rutema_web config.yaml and browse to http://localhost:7000 for the glorious view

Here is a sample of the configuration YAML:
--- 
:db: 
  :adapter: sqlite3
  :database: rutema_test.db
:settings: 
  :page_size: 10
  :last_n_runs: 20
  :port: 7000
  :show_setup_teardown: true

The :db: section should be the activerecord adapter configuration. The :settings: section controls the behaviour of the web app.

## 官网

- 主页: http://patir.rubyforge.org/rutema
- RubyGems: https://rubygems.org/gems/rutema_web

## 历史版本号

- 1.0.6 (2011-11-30)
- 1.0.5 (2011-04-01)
- 1.0.4 (2010-04-23)
- 1.0.3 (2009-12-17)
- 1.0.2 (2009-09-24)
- 1.0.0 (2009-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/rutema_web
- gem 安装: `gem install rutema_web`
- Bundler: `gem "rutema_web"`
- 最新版本: 1.0.6
- 最新版归档: https://rubygems.org/downloads/rutema_web-1.0.6.gem
- 版本锁定: `gem "rutema_web", "~> 1.0.6"`
- 中央仓库: https://rubygems.org/
