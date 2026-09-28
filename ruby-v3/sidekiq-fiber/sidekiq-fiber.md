# sidekiq-fiber

**Tag**: web, networking

## 简介

sidekiq-fiber lets you run IO-bound Sidekiq jobs as fibers instead of threads.
A single thread can process thousands of concurrent jobs that spend most of
their time waiting on external IO (HTTP, LLM APIs, S3) — without the memory
and OS overhead of one thread per job.

## 官网

- 主页: https://github.com/yashdave31/sidekiq-fiber
- 文档: https://www.rubydoc.info/gems/sidekiq-fiber/0.1.2
- RubyGems: https://rubygems.org/gems/sidekiq-fiber

## 历史版本号

- 0.1.2 (2026-05-04)
- 0.1.1 (2026-05-04)
- 0.1.0 (2026-05-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq-fiber
- gem 安装: `gem install sidekiq-fiber`
- Bundler: `gem "sidekiq-fiber"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/sidekiq-fiber-0.1.2.gem
- 版本锁定: `gem "sidekiq-fiber", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
