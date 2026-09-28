# mongoid-history

**Tag**: web, filesystem

## 简介

This library tracks historical changes for any document, including embedded ones. It achieves this by storing all history tracks in a single collection that you define. Embedded documents are referenced by storing an association path, which is an array of document_name and document_id fields starting from the top most parent document and down to the embedded document that should track history. Mongoid-history implements multi-user undo, which allows users to undo any history change in any order. Undoing a document also creates a new history track. This is great for auditing and preventing vandalism, but it is probably not suitable for use cases such as a wiki.

## 官网

- 主页: http://github.com/mongoid/mongoid-history
- 源码仓库: https://github.com/aq1018/mongoid-history
- 文档: https://www.rubydoc.info/gems/mongoid-history/0.8.5
- RubyGems: https://rubygems.org/gems/mongoid-history

## 历史版本号

- 0.8.5 (2021-09-18)
- 0.8.3 (2020-06-17)
- 0.8.2 (2019-12-02)
- 0.8.1 (2018-06-28)
- 0.8.0 (2018-01-16)
- 0.7.0 (2017-11-14)
- 0.6.1 (2017-01-04)
- 0.6.0 (2016-09-13)
- 0.5.0 (2015-09-18)
- 0.4.7 (2015-04-06)
- 0.4.5 (2015-02-09)
- 0.4.4 (2014-07-21)
- 0.4.3 (2014-07-10)
- 0.4.2 (2014-07-01)
- 0.4.1 (2014-01-11)
- 0.4.0 (2013-07-12)
- 0.3.3 (2013-04-01)
- 0.3.2 (2013-01-24)
- 0.3.1 (2012-11-16)
- 0.3.0 (2012-08-21)
- 0.2.4 (2012-08-21)
- 0.2.3 (2012-04-20)
- 0.2.2 (2012-04-05)
- 0.2.1 (2012-03-19)
- 0.1.7 (2011-12-09)
- 0.1.6 (2011-12-07)
- 0.1.5 (2011-11-21)
- 0.1.4 (2011-08-30)
- 0.1.3 (2011-07-12)
- 0.1.2 (2011-06-21)
- 0.1.1 (2011-05-25)
- 0.1.0 (2011-05-13)
- 0.0.9 (2011-04-06)
- 0.0.8 (2011-04-03)
- 0.0.7 (2011-03-17)
- 0.0.6 (2011-03-17)
- 0.0.5 (2011-03-08)
- 0.0.4 (2011-03-07)
- 0.0.3 (2011-03-07)
- 0.0.2 (2011-03-07)
- 0.0.1 (2011-03-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/mongoid-history
- gem 安装: `gem install mongoid-history`
- Bundler: `gem "mongoid-history"`
- 最新版本: 0.8.5
- 最新版归档: https://rubygems.org/downloads/mongoid-history-0.8.5.gem
- 版本锁定: `gem "mongoid-history", "~> 0.8.5"`
- 中央仓库: https://rubygems.org/
