# sidekiq_lockable_job

**Tag**: database

## 简介

Sidekiq includes a jobs dependencies mechanism to prevent a job from running before another one when enqueued.

But sometime your jobs will be enqueued independently, then for you do not know the job id on which you depend on (you could parse Sidekiq queue, but...)

`SidekiqLockableJob` allows you to set some locks ( based on job params ) when a job is enqueued or processed (store in redis), to prevent any other jobs to run if locked ( based on job params ) and will unlock any previously set locks ( based on job params ) when a job is **succesfully** completed.

## 官网

- 主页: https://github.com/huguesbr/sidekiq_lockable_job
- 更新日志: https://github.com/huguesbr/sidekiq_lockable_job/README.md
- RubyGems: https://rubygems.org/gems/sidekiq_lockable_job

## 历史版本号

- 0.1.2 (2020-04-26)
- 0.1.1 (2020-04-20)
- 0.1.0 (2020-04-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq_lockable_job
- gem 安装: `gem install sidekiq_lockable_job`
- Bundler: `gem "sidekiq_lockable_job"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/sidekiq_lockable_job-0.1.2.gem
- 版本锁定: `gem "sidekiq_lockable_job", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
