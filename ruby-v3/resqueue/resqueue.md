# resqueue

**Tag**: web, database, testing

## 简介

Resqueue is a Redis-backed Ruby library for creating background jobs,
    placing those jobs on multiple queues, and processing them later.

    It is meant to be the continuation of Resque since it is no longer
    released by its maintainers.

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

- 主页: http://resque.github.io/
- 文档: https://www.rubydoc.info/gems/resqueue/1.0.0
- RubyGems: https://rubygems.org/gems/resqueue

## 历史版本号

- 1.0.0 (2017-01-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/resqueue
- gem 安装: `gem install resqueue`
- Bundler: `gem "resqueue"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/resqueue-1.0.0.gem
- 版本锁定: `gem "resqueue", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
