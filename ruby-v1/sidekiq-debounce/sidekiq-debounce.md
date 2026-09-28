# sidekiq-debounce

**Tag**: testing

## 简介

Sidekiq::Debounce provides a way to rate-limit creation of Sidekiq jobs.  When
you create a job on a Worker with debounce enabled, Sidekiq::Debounce will
delay the job until the debounce period has elapsed with no additional debounce
calls. If you make another job with the same arguments before the specified
time has elapsed, the timer is reset and the entire period must pass again
before the job is executed.

## 官网

- 主页: https://github.com/hummingbird-me/sidekiq-debounce
- 文档: https://www.rubydoc.info/gems/sidekiq-debounce/1.1.0
- RubyGems: https://rubygems.org/gems/sidekiq-debounce

## 历史版本号

- 1.1.0 (2016-09-20)
- 1.0.2 (2015-08-09)
- 1.0.1 (2015-06-13)
- 1.0.0 (2015-04-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq-debounce
- gem 安装: `gem install sidekiq-debounce`
- Bundler: `gem "sidekiq-debounce"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/sidekiq-debounce-1.1.0.gem
- 版本锁定: `gem "sidekiq-debounce", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
