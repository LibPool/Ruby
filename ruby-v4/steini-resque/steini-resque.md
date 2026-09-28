# steini-resque

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

- 主页: http://github.com/defunkt/resque
- RubyGems: https://rubygems.org/gems/steini-resque

## 历史版本号

- 1.18.5 (2011-08-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/steini-resque
- gem 安装: `gem install steini-resque`
- Bundler: `gem "steini-resque"`
- 最新版本: 1.18.5
- 最新版归档: https://rubygems.org/downloads/steini-resque-1.18.5.gem
- 版本锁定: `gem "steini-resque", "~> 1.18.5"`
- 中央仓库: https://rubygems.org/
