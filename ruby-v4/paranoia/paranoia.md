# paranoia

**Tag**: web

## 简介

Paranoia is a re-implementation of acts_as_paranoid for Rails 5, 6, and 7,
    using much, much, much less code. You would use either plugin / gem if you
    wished that when you called destroy on an Active Record object that it
    didn't actually destroy it, but just "hid" the record. Paranoia does this
    by setting a deleted_at field to the current time when you destroy a record,
    and hides it by scoping all queries on your model to only include records
    which do not have a deleted_at field.

## 官网

- 主页: https://github.com/rubysherpas/paranoia
- 文档: https://www.rubydoc.info/gems/paranoia/3.1.0
- RubyGems: https://rubygems.org/gems/paranoia

## 历史版本号

- 3.1.0 (2025-11-07)
- 3.0.1 (2025-01-19)
- 3.0.0 (2024-08-13)
- 2.6.4 (2024-07-20)
- 2.6.3 (2023-10-11)
- 2.6.2 (2023-06-05)
- 2.6.1 (2022-11-15)
- 2.6.0 (2022-03-23)
- 2.5.3 (2022-03-23)
- 2.5.2 (2022-02-02)
- 2.5.1 (2022-02-02)
- 2.5.0 (2021-12-18)
- 2.4.3 (2020-12-16)
- 2.4.2 (2019-04-26)
- 2.4.1 (2018-04-10)
- 2.4.0 (2017-11-03)
- 2.3.1 (2017-04-27)
- 2.3.0 (2017-04-14)
- 2.2.1 (2017-02-16)
- 2.2.0 (2016-10-20)
- 2.2.0.pre (2016-07-14)
- 2.1.5 (2016-01-07)
- 2.1.4 (2015-11-05)
- 2.1.3 (2015-06-17)
- 2.1.2 (2015-04-28)
- 2.1.1 (2015-03-23)
- 1.3.4 (2015-01-29)
- 2.1.0 (2015-01-24)
- 2.1.0.pre (2015-01-22)
- 2.0.5 (2015-01-22)
- 2.0.4 (2014-12-03)
- 2.0.3 (2014-11-21)
- 2.0.2 (2014-01-16)
- 1.3.3 (2014-01-16)
- 2.0.1 (2013-10-24)
- 1.3.2 (2013-10-24)
- 1.3.1 (2013-07-08)
- 2.0.0 (2013-07-08)
- 1.3.0 (2013-07-08)
- 1.2.0 (2012-11-22)
- 1.1.0 (2011-07-11)
- 1.0.3 (2011-05-26)
- 1.0.2 (2011-05-24)
- 1.0.1 (2011-05-12)
- 1.0.0 (2011-04-06)
- 0.0.1 (2010-10-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/paranoia
- gem 安装: `gem install paranoia`
- Bundler: `gem "paranoia"`
- 最新版本: 3.1.0
- 最新版归档: https://rubygems.org/downloads/paranoia-3.1.0.gem
- 版本锁定: `gem "paranoia", "~> 3.1.0"`
- 中央仓库: https://rubygems.org/
