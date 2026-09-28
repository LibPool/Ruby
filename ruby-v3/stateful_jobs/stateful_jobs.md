# stateful_jobs

**Tag**: library

## 简介

StatefulJobs is a Resque based library which allows you to integrate responsive background jobs in a very easy way. StatefulJobs wraps an ActiveRecord Model around a set of jobs and adds a polling mechanism to your frontend to get your users noticed about the state of their tasks.

    Very useful for:

    * background jobs which provide its state to the frontend
    * background jobs which need user interaction between several steps
    * a set of jobs which share process information

    All these jobs can either be implemented as a separate Class or inline with just a handy Proc.

## 官网

- 主页: https://github.com/metascape/stateful_jobs
- 问题追踪: https://github.com/metascape/stateful_jobs/issues
- RubyGems: https://rubygems.org/gems/stateful_jobs

## 历史版本号

- 0.0.2 (2013-03-08)
- 0.0.1 (2013-03-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/stateful_jobs
- gem 安装: `gem install stateful_jobs`
- Bundler: `gem "stateful_jobs"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/stateful_jobs-0.0.2.gem
- 版本锁定: `gem "stateful_jobs", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
