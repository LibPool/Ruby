# resque-cedar

**Tag**: web, database, testing, networking

## 简介

A patched version of Resque that interprets Heroku's TERM as a graceful shutdown. 
    Visit http://quickleft.com/blog/heroku-s-cedar-stack-will-kill-your-resque-workers 
    for more information.
    
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

- 主页: http://github.com/mjezzi/resque-cedar
- RubyGems: https://rubygems.org/gems/resque-cedar

## 历史版本号

- 1.20.0 (2012-06-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-cedar
- gem 安装: `gem install resque-cedar`
- Bundler: `gem "resque-cedar"`
- 最新版本: 1.20.0
- 最新版归档: https://rubygems.org/downloads/resque-cedar-1.20.0.gem
- 版本锁定: `gem "resque-cedar", "~> 1.20.0"`
- 中央仓库: https://rubygems.org/
