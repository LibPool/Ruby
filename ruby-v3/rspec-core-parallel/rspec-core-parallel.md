# rspec-core-parallel

**Tag**: web, database, testing, data

## 简介

Adds `rspec --parallel` to rspec-core 3.13: the suite is loaded once, forked into one worker per CPU core, and groups are handed out longest first using the run times of the previous run. Formatters, --only-failures, --bisect and exit codes work as in a sequential run. Rails apps get a test database per worker.

## 官网

- 主页: https://github.com/renuo/rspec-core-parallel
- 更新日志: https://github.com/renuo/rspec-core-parallel/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/rspec-core-parallel

## 历史版本号

- 0.4.0 (2026-10-20)
- 0.3.0 (2026-10-20)
- 0.2.1 (2026-10-20)
- 0.2.0 (2026-10-20)
- 0.1.0 (2026-10-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/rspec-core-parallel
- gem 安装: `gem install rspec-core-parallel`
- Bundler: `gem "rspec-core-parallel"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/rspec-core-parallel-0.4.0.gem
- 版本锁定: `gem "rspec-core-parallel", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
