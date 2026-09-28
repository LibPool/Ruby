# consistency_fail

**Tag**: web, database, data

## 简介

With more than one application server, validates_uniqueness_of becomes a lie.
Two app servers -> two requests -> two near-simultaneous uniqueness checks ->
two processes that commit to the database independently, violating this faux
constraint. You'll need a database-level constraint for cases like these.

consistency_fail will find your missing unique indexes, so you can add them and
stop ignoring the C in ACID.

## 官网

- 主页: http://github.com/trptcolin/consistency_fail
- 文档: https://www.rubydoc.info/gems/consistency_fail/0.3.7
- RubyGems: https://rubygems.org/gems/consistency_fail

## 历史版本号

- 0.3.7 (2018-10-22)
- 0.3.6 (2018-10-09)
- 0.3.5 (2017-02-01)
- 0.3.4 (2016-02-02)
- 0.3.3 (2014-12-12)
- 0.3.2 (2013-07-23)
- 0.3.1 (2013-07-18)
- 0.3.0 (2013-01-18)
- 0.2.2 (2012-01-04)
- 0.2.1 (2011-06-17)
- 0.1.1 (2011-06-17)
- 0.2.0 (2011-06-10)
- 0.1.0 (2011-06-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/consistency_fail
- gem 安装: `gem install consistency_fail`
- Bundler: `gem "consistency_fail"`
- 最新版本: 0.3.7
- 最新版归档: https://rubygems.org/downloads/consistency_fail-0.3.7.gem
- 版本锁定: `gem "consistency_fail", "~> 0.3.7"`
- 中央仓库: https://rubygems.org/
