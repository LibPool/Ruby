# acts_as_archival

**Tag**: filesystem

## 简介

*Atomic archiving/unarchiving for ActiveRecord-based apps*

We had the problem that acts_as_paranoid and similar plugins/gems always work on
a record by record basis and made it very difficult to restore records
atomically (or archive them, for that matter).

Because the archive and unarchive methods are in transactions, and every
archival record involved gets the same archive number upon archiving, you can
easily restore or remove an entire set of records without having to worry about
partial deletion or restoration.

Additionally, other plugins generally screw with how destroy/delete work. We
don't because we actually want to be able to destroy records.

## 官网

- 主页: http://github.com/expectedbehavior/acts_as_archival
- 文档: https://www.rubydoc.info/gems/acts_as_archival/2.1.0
- RubyGems: https://rubygems.org/gems/acts_as_archival

## 历史版本号

- 2.1.0 (2022-06-21)
- 2.0.0 (2021-10-19)
- 1.4.0 (2019-07-09)
- 1.3.0 (2017-10-21)
- 1.2.0 (2017-03-19)
- 1.1.1 (2016-04-10)
- 1.1.0 (2016-04-10)
- 1.0.0 (2016-04-05)
- 0.6.1 (2014-07-24)
- 0.6.0 (2014-04-14)
- 0.5.3 (2013-05-17)
- 0.5.2 (2013-05-17)
- 0.5.1 (2013-05-17)
- 0.5.0 (2013-03-16)
- 0.4.2 (2012-03-04)
- 0.4.1 (2012-03-04)
- 0.4.0 (2012-03-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/acts_as_archival
- gem 安装: `gem install acts_as_archival`
- Bundler: `gem "acts_as_archival"`
- 最新版本: 2.1.0
- 最新版归档: https://rubygems.org/downloads/acts_as_archival-2.1.0.gem
- 版本锁定: `gem "acts_as_archival", "~> 2.1.0"`
- 中央仓库: https://rubygems.org/
