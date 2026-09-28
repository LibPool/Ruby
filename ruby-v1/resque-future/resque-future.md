# resque-future

**Tag**: library

## 简介

Resque plugin that allows querying future jobs for it's result, for example:

  job = Resque.enqueue_future(MixerWorker, "yeah")
  # store job.uuid somewhere

  # Later on
  job = Resque.get_future_job(uuid)
  job.ready?
  job.result
  job.finished_at

## 官网

- 主页: http://github.com/divoxx/resque-future
- RubyGems: https://rubygems.org/gems/resque-future

## 历史版本号

- 0.1.0 (2011-03-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-future
- gem 安装: `gem install resque-future`
- Bundler: `gem "resque-future"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/resque-future-0.1.0.gem
- 版本锁定: `gem "resque-future", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
