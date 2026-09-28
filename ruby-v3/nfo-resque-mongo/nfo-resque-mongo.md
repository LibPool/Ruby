# nfo-resque-mongo

**Tag**: web, testing

## 简介

Resque-mongo is a MongoDB-backed Ruby library for creating background jobs,
    placing those jobs on multiple queues, and processing them later.

 \   Background jobs can be any Ruby class or module that responds to
    perform. Your existing classes can easily be converted to background
    jobs or you can create new classes specifically to do work. Or, you
    can do both.

    Resque is heavily inspired by DelayedJob (which rocks) and is
    comprised of three parts:

 \   * A Ruby library for creating, querying, and processing jobs
    * A Rake task for starting a worker which processes jobs
    * A Sinatra app for monitoring queues, jobs, and workers.

## 官网

- 主页: http://github.com/nfo/resque-mongo
- RubyGems: https://rubygems.org/gems/nfo-resque-mongo

## 历史版本号

- 1.17.2 (2011-10-27)
- 1.17.1 (2011-08-12)
- 1.15.1 (2011-06-29)
- 1.15.0 (2011-03-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/nfo-resque-mongo
- gem 安装: `gem install nfo-resque-mongo`
- Bundler: `gem "nfo-resque-mongo"`
- 最新版本: 1.17.2
- 最新版归档: https://rubygems.org/downloads/nfo-resque-mongo-1.17.2.gem
- 版本锁定: `gem "nfo-resque-mongo", "~> 1.17.2"`
- 中央仓库: https://rubygems.org/
