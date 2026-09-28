# rails_parallel

**Tag**: web, database, testing

## 简介

rails_parallel runs your Rails tests by forking off a worker and running multiple tests concurrently.  It makes heavy use of forking to reduce memory footprint (assuming copy-on-write), only loads your Rails environment once, and automatically scales to the number of cores available.  Designed to work with MySQL only.  For best results, run MySQL on a tmpfs or a RAM disk.

## 官网

- RubyGems: https://rubygems.org/gems/rails_parallel

## 历史版本号

- 0.1.3 (2011-08-10)
- 0.1.2 (2011-08-06)
- 0.1.1 (2011-08-05)
- 0.1.0 (2011-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails_parallel
- gem 安装: `gem install rails_parallel`
- Bundler: `gem "rails_parallel"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/rails_parallel-0.1.3.gem
- 版本锁定: `gem "rails_parallel", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
