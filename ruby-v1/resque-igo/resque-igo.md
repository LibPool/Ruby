# resque-igo

**Tag**: web, database, testing

## 简介

Resque is a Redis-backed Ruby library for creating background jobs,
    placing those jobs on multiple queues, and processing them later.

    Resque-igo is the same thing, but for mongo.  It would not exist without the work of defunkt and ctrochalakis on github.

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

- 主页: http://github.com/mediocretes/resque-mongo
- RubyGems: https://rubygems.org/gems/resque-igo

## 历史版本号

- 1.12.8 (2011-02-04)
- 1.12.7 (2011-01-31)
- 1.12.6 (2010-12-22)
- 1.12.5 (2010-12-15)
- 1.12.4 (2010-12-14)
- 1.12.3 (2010-12-14)
- 1.12.2 (2010-12-03)
- 1.12.1 (2010-12-01)
- 1.1.5 (2010-12-01)
- 1.1.4 (2010-11-03)
- 1.1.3 (2010-10-28)
- 1.1.2 (2010-10-28)
- 1.1.1 (2010-10-28)
- 1.1 (2010-10-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-igo
- gem 安装: `gem install resque-igo`
- Bundler: `gem "resque-igo"`
- 最新版本: 1.12.8
- 最新版归档: https://rubygems.org/downloads/resque-igo-1.12.8.gem
- 版本锁定: `gem "resque-igo", "~> 1.12.8"`
- 中央仓库: https://rubygems.org/
