# jobpayload

**Tag**: testing, serialization, data

## 简介

jobpayload snapshots Active Job serialized job data (ActiveJob::Base#serialize) into
deterministic JSON fixtures and checks that the current application can still
deserialize them (ActiveJob::Base.deserialize and ActiveJob::Arguments.deserialize)
without ever performing the job.

## 官网

- 主页: https://github.com/cottondesu/jobpayload
- 更新日志: https://github.com/cottondesu/jobpayload/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/jobpayload

## 历史版本号

- 0.2.0 (2026-10-09)
- 0.1.0 (2026-10-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/jobpayload
- gem 安装: `gem install jobpayload`
- Bundler: `gem "jobpayload"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/jobpayload-0.2.0.gem
- 版本锁定: `gem "jobpayload", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
