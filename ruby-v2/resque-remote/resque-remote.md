# resque-remote

**Tag**: database

## 简介

Compatible with Resque 1.x. Use Resque.push if you are using >= 2.x.

Resque is great. So is job processing with redis. Our biggest drawback has been that
resque requires the class that will be processing a job to be loaded when the job
is enqueued. But what happens when the implementing job is defined in a separate application
and isn't currently loaded into memory?

Enter Resque Remote.

Resque Remote's simple goal is to allow you to add a job to a queue with a string
identifier for the class rather than the class constant. It is assumed that the worker-side of
the equation _will_ have the class in memory and hence will be able to run it no problem.

Feedback, comments and questions are welcome at bj [dot] neilsen [at] gmail [dot] com.

## 官网

- 主页: http://github.com/localshred/resque-remote
- 文档: https://www.rubydoc.info/gems/resque-remote/0.1.3
- RubyGems: https://rubygems.org/gems/resque-remote

## 历史版本号

- 0.1.3 (2014-04-03)
- 0.1.2 (2013-03-20)
- 0.1.1 (2012-07-27)
- 0.1.0 (2012-02-06)
- 0.0.1 (2010-08-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-remote
- gem 安装: `gem install resque-remote`
- Bundler: `gem "resque-remote"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/resque-remote-0.1.3.gem
- 版本锁定: `gem "resque-remote", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
