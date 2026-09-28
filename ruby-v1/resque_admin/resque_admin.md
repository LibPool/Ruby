# resque_admin

**Tag**: web, database, testing

## 简介

ResqueAdmin is a Redis-backed Ruby library for creating background jobs,
    placing those jobs on multiple queues, and processing them later.

    Background jobs can be any Ruby class or module that responds to
    perform. Your existing classes can easily be converted to background
    jobs or you can create new classes specifically to do work. Or, you
    can do both.

    ResqueAdmin is heavily inspired by DelayedJob (which rocks) and is
    comprised of three parts:

    * A Ruby library for creating, querying, and processing jobs
    * A Rake task for starting a worker which processes jobs
    * A Sinatra app for monitoring queues, jobs, and workers.

## 官网

- 主页: http://resque.github.io/
- 文档: https://www.rubydoc.info/gems/resque_admin/2.4.4
- RubyGems: https://rubygems.org/gems/resque_admin

## 历史版本号

- 1.0.5 (2017-09-22)
- 1.0.4 (2017-09-22)
- 1.0.3 (2017-09-22)
- 1.0.2 (2017-09-22)
- 0.2.0 (2017-09-07)
- 2.4.4 (2017-09-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque_admin
- gem 安装: `gem install resque_admin`
- Bundler: `gem "resque_admin"`
- 最新版本: 2.4.4
- 最新版归档: https://rubygems.org/downloads/resque_admin-2.4.4.gem
- 版本锁定: `gem "resque_admin", "~> 2.4.4"`
- 中央仓库: https://rubygems.org/
