# sidekiq-max-jobs

**Tag**: database, devops, data

## 简介

This gem provides the ability to configure the maximum number of jobs a
Sidekiq worker will process before terminating. For an environment running
Kubernetes this is a perfect addition because once the affected pod dies it
will automatically be restarted [gracefully] resetting memory,
database-connections, etc. with minimal interruption to throughput

## 官网

- 主页: http://github.com/jzaleski/sidekiq-max-jobs
- 文档: https://www.rubydoc.info/gems/sidekiq-max-jobs/0.1.0
- RubyGems: https://rubygems.org/gems/sidekiq-max-jobs

## 历史版本号

- 0.1.0 (2020-06-22)
- 0.0.5 (2020-06-19)
- 0.0.4 (2020-06-18)
- 0.0.2 (2020-06-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq-max-jobs
- gem 安装: `gem install sidekiq-max-jobs`
- Bundler: `gem "sidekiq-max-jobs"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/sidekiq-max-jobs-0.1.0.gem
- 版本锁定: `gem "sidekiq-max-jobs", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
