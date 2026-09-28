# em-resque

**Tag**: web, database, networking, data

## 简介

Em-resque is a version of Resque, which offers non-blocking and non-forking
    workers. The idea is to have fast as possible workers for tasks with lots of
    IO like pinging third party servers or hitting the database.

    The async worker is using fibers through Synchrony library to reduce the amount
    of callback functions. There's one fiber for worker and if one of the workers
    is blocking, it will block all the workers at the same time.

    The idea to use this version and not the regular Resque is to reduce the amount
    of SQL connections for high-load services. Using one process for many workers
    gives a better control to the amount of SQL connections.

    For using Resque please refer the original project.

    https://github.com/defunkt/resque/

    The library adds two rake tasks over Resque:

      * resque:work_async for working inside the EventMachine

## 官网

- 主页: http://github.com/SponsorPay/em-resque
- RubyGems: https://rubygems.org/gems/em-resque

## 历史版本号

- 1.1.1 (2012-09-23)
- 1.1.0 (2012-07-23)
- 1.0.4 (2012-05-05)
- 1.0.3 (2012-02-14)
- 1.0.2 (2012-01-25)
- 1.0.1 (2012-01-24)
- 1.0.0 (2012-01-24)
- 1.0.0.beta8 (2012-01-23)
- 1.0.0.beta7 (2012-01-20)
- 1.0.0.beta6 (2012-01-17)
- 1.0.0.beta5 (2012-01-17)
- 1.0.0.beta4 (2012-01-12)
- 1.0.0.beta3 (2012-01-12)
- 1.0.0.beta2 (2012-01-09)
- 1.0.0.beta1 (2012-01-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/em-resque
- gem 安装: `gem install em-resque`
- Bundler: `gem "em-resque"`
- 最新版本: 1.1.1
- 最新版归档: https://rubygems.org/downloads/em-resque-1.1.1.gem
- 版本锁定: `gem "em-resque", "~> 1.1.1"`
- 中央仓库: https://rubygems.org/
