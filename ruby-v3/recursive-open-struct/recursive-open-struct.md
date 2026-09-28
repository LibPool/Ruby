# recursive-open-struct

**Tag**: library

## 简介

RecursiveOpenStruct is a subclass of OpenStruct. It differs from
OpenStruct in that it allows nested hashes to be treated in a recursive
fashion. For example:

    ros = RecursiveOpenStruct.new({ :a => { :b => 'c' } })
    ros.a.b # 'c'

Also, nested hashes can still be accessed as hashes:

    ros.a_as_a_hash # { :b => 'c' }

## 官网

- 主页: https://github.com/aetherknight/recursive-open-struct
- 文档: https://www.rubydoc.info/gems/recursive-open-struct/2.1.1
- RubyGems: https://rubygems.org/gems/recursive-open-struct

## 历史版本号

- 2.1.1 (2026-04-19)
- 2.1.0 (2025-12-05)
- 2.0.0 (2024-10-04)
- 1.3.1 (2024-10-04)
- 1.3.0 (2024-10-02)
- 1.2.2 (2024-06-19)
- 1.2.1 (2024-05-28)
- 1.1.3 (2020-10-16)
- 1.1.2 (2020-06-21)
- 1.1.1 (2020-03-11)
- 1.1.0 (2018-02-03)
- 1.0.5 (2017-06-22)
- 1.0.4 (2017-04-29)
- 1.0.3 (2017-04-10)
- 1.0.2 (2016-12-19)
- 1.0.1 (2016-01-18)
- 1.0.0 (2015-12-12)
- 0.6.5 (2015-07-01)
- 0.6.4 (2015-05-21)
- 0.6.3 (2015-04-11)
- 0.6.2 (2015-04-08)
- 0.6.1 (2015-03-28)
- 0.6.0 (2015-03-28)
- 0.5.0 (2014-06-14)
- 0.4.5 (2013-10-24)
- 0.4.4 (2013-08-28)
- 0.4.3 (2013-05-31)
- 0.4.2 (2013-05-30)
- 0.4.1 (2013-05-29)
- 0.4.0 (2013-05-26)
- 0.3.1 (2013-01-05)
- 0.2.1 (2011-05-31)
- 0.2.0 (2011-05-25)
- 0.1.0 (2011-05-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/recursive-open-struct
- gem 安装: `gem install recursive-open-struct`
- Bundler: `gem "recursive-open-struct"`
- 最新版本: 2.1.1
- 最新版归档: https://rubygems.org/downloads/recursive-open-struct-2.1.1.gem
- 版本锁定: `gem "recursive-open-struct", "~> 2.1.1"`
- 中央仓库: https://rubygems.org/
