# geoptima

**Tag**: web, database, serialization, template, filesystem, data

## 简介

Geoptima is a suite of applications for measuring and locating
mobile/cellular subscriber experience on GPS enabled smartphones.  It is
produced by AmanziTel AB in Helsingborg, Sweden, and supports many phone
manufacturers, with free downloads from the various app stores, markets or
marketplaces.  This Ruby library is capable of reading the JSON format files
produced by these phones and reformating them as CSV, GPX and PNG for
further analysis in Excel.  This is a simple and independent way of
analysing the data, when compared to the full-featured analysis applications
and servers available from AmanziTel.  If you want to analyse a limited
amount of data in excel, or with Ruby, then this GEM might be for you.  If
you want to analyse large amounts of data, from many subscribers, or over
long periods of time then rather consider the NetView and Customer IQ
applications from AmanziTel at www.amanzitel.com.

Current features available in the library and the show_geoptima command:
* Import one or many JSON files
* Organize data by device id (IMEI) into datasets
* Split by event type
* Time ordering and time correlation (associate data from one event to another):
** Add GPS locations to other events (time window and interpolation algorithms)
** Add signal strenth, battery level, etc. to other events
* Export event tables to CSV format for further processing in excel
* Make and export GPS traces in GPX and PNG format for simple map reports

The amount of data possible to process is limited by memory, since all data
is imported in ruby data structures for procssing.  If you need to process
larger amounts of data, you will need a database-driven approach, like that
provided by AmanziTel's NetView and Customer IQ solutions.  This Ruby gem is
actually used by parts of the data pre-processing chain of 'Customer IQ',
but it not used by the main database and statistics engine that generates
the reports.

## 官网

- 主页: http://github.com/craigtaverner/geoptima.rb
- 源码仓库: https://github.com/craigtaverner/geoptima.rb
- 文档: https://www.rubydoc.info/gems/geoptima/0.1.22
- RubyGems: https://rubygems.org/gems/geoptima

## 历史版本号

- 0.1.22 (2013-06-25)
- 0.1.21 (2013-06-19)
- 0.1.20 (2013-06-13)
- 0.1.19 (2013-05-03)
- 0.1.18 (2013-01-07)
- 0.1.17 (2012-12-13)
- 0.1.15 (2012-08-10)
- 0.1.14 (2012-08-03)
- 0.1.13 (2012-07-30)
- 0.1.12 (2012-06-08)
- 0.1.11 (2012-06-07)
- 0.1.10 (2012-05-30)
- 0.1.9 (2012-05-29)
- 0.1.8 (2012-05-18)
- 0.1.7 (2012-05-18)
- 0.1.6 (2012-04-23)
- 0.1.4 (2012-04-17)
- 0.1.3 (2012-04-04)
- 0.1.2 (2012-03-26)
- 0.1.1 (2012-03-23)
- 0.1.0 (2012-03-22)
- 0.0.9 (2012-03-21)
- 0.0.8 (2012-03-19)
- 0.0.7 (2012-03-19)
- 0.0.6 (2012-03-13)
- 0.0.5 (2012-03-09)
- 0.0.4 (2012-03-09)
- 0.0.2 (2012-03-08)
- 0.0.1 (2012-03-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/geoptima
- gem 安装: `gem install geoptima`
- Bundler: `gem "geoptima"`
- 最新版本: 0.1.22
- 最新版归档: https://rubygems.org/downloads/geoptima-0.1.22.gem
- 版本锁定: `gem "geoptima", "~> 0.1.22"`
- 中央仓库: https://rubygems.org/
