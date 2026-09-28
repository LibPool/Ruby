# resque

**Tag**: web, database, testing

## 简介

Resque is a Redis-backed Ruby library for creating background jobs,
    placing those jobs on multiple queues, and processing them later.

    Background jobs can be any Ruby class or module that responds to
    perform. Your existing classes can easily be converted to background
    jobs or you can create new classes specifically to do work. Or, you
    can do both.

    Resque is heavily inspired by DelayedJob (which rocks) and is
    comprised of three parts:

    * A Ruby library for creating, querying, and processing jobs
    * A Rake task for starting a worker which processes jobs
    * A Sinatra app for monitoring queues, jobs, and workers.

## 官网

- 主页: https://github.com/resque/resque
- 更新日志: https://github.com/resque/resque/blob/master/HISTORY.md
- RubyGems: https://rubygems.org/gems/resque

## 历史版本号

- 3.1.0 (2026-09-16)
- 3.0.3 (2026-09-10)
- 3.0.2 (2026-08-30)
- 3.0.1 (2026-08-28)
- 3.0.0 (2026-01-12)
- 2.7.0 (2024-12-30)
- 2.6.0 (2023-08-19)
- 2.5.0 (2023-03-01)
- 2.4.0 (2022-09-06)
- 2.3.0 (2022-08-22)
- 2.2.1 (2022-03-27)
- 2.2.0 (2021-11-04)
- 2.1.0 (2021-08-10)
- 2.0.0 (2018-11-06)
- 1.27.4 (2017-04-15)
- 1.27.3 (2017-04-10)
- 1.27.2 (2017-02-20)
- 1.27.1 (2017-02-13)
- 1.27.0 (2017-02-08)
- 1.26.0 (2016-03-11)
- 1.25.2 (2014-03-04)
- 1.26.pre.0 (2013-12-06)
- 1.25.1 (2013-09-26)
- 1.25.0 (2013-09-16)
- 1.25.0.pre (2013-07-23)
- 1.24.1 (2013-03-23)
- 1.24.0 (2013-03-21)
- 1.23.1 (2013-03-07)
- 1.23.0 (2012-10-01)
- 1.22.0 (2012-08-21)
- 1.21.0 (2012-07-03)
- 1.20.0 (2012-02-17)
- 1.19.0 (2011-09-02)
- 1.18.6 (2011-08-30)
- 1.18.5 (2011-08-24)
- 1.18.4 (2011-08-23)
- 1.18.3 (2011-08-23)
- 1.18.2 (2011-08-19)
- 1.18.1 (2011-08-19)
- 1.18.0 (2011-08-18)
- 1.17.1 (2011-05-27)
- 1.17.0 (2011-05-26)
- 1.16.1 (2011-05-17)
- 1.16.0 (2011-05-16)
- 1.15.0 (2011-03-19)
- 1.14.0 (2011-03-17)
- 1.13.0 (2011-02-07)
- 1.11.0 (2011-02-04)
- 1.12.0 (2011-02-04)
- 1.10.0 (2010-08-24)
- 1.9.10 (2010-08-07)
- 1.9.9 (2010-07-26)
- 1.9.8 (2010-07-20)
- 1.9.7 (2010-07-09)
- 1.9.5 (2010-06-16)
- 1.9.4 (2010-06-14)
- 1.9.3 (2010-06-14)
- 1.9.2 (2010-06-13)
- 1.9.1 (2010-06-04)
- 1.9.0 (2010-06-04)
- 1.8.6 (2010-06-04)
- 1.8.5 (2010-05-18)
- 1.8.4 (2010-05-18)
- 1.8.3 (2010-05-17)
- 1.8.2 (2010-05-04)
- 1.8.1 (2010-04-30)
- 1.8.0 (2010-04-07)
- 1.7.1 (2010-04-02)
- 1.7.0 (2010-04-01)
- 1.6.1 (2010-03-25)
- 1.6.0 (2010-03-09)
- 1.5.2 (2010-03-03)
- 1.5.1 (2010-03-03)
- 1.5.0 (2010-02-17)
- 1.4.0 (2010-02-11)
- 1.3.1 (2010-01-11)
- 1.3.0 (2010-01-11)
- 1.2.3 (2009-12-15)
- 1.2.1 (2009-12-08)
- 1.2.0 (2009-11-26)
- 1.1.0 (2009-11-04)
- 1.0.0 (2009-11-03)
- 0.2.0 (2009-11-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque
- gem 安装: `gem install resque`
- Bundler: `gem "resque"`
- 最新版本: 3.1.0
- 最新版归档: https://rubygems.org/downloads/resque-3.1.0.gem
- 版本锁定: `gem "resque", "~> 3.1.0"`
- 中央仓库: https://rubygems.org/
