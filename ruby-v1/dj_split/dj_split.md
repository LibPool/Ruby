# dj_split

**Tag**: web

## 简介

Gem is designed to "Split or Break" Time Taking Jobs(Delayed Jobs, Crons, Bulk Operations, etc.) into smaller size Mutually Exclusive Delayed Jobs. These Sub-Jobs can be picked by "Multiple Workers" in "Single" or "Multiple Servers". After splitting and enqueuing, the process will wait for the sub-jobs to complete and also processes sub-jobs instead of blocking. "Parallelism" can be achieved across multiple servers through Delayed Jobs which can directly impact performance. "Performance" can improve up to "n+1" times, where n = number of workers picking the jobs.

## 官网

- 源码仓库: https://github.com/nehalamin93/dj_split
- 文档: https://www.rubydoc.info/gems/dj_split/1.1.1
- RubyGems: https://rubygems.org/gems/dj_split

## 历史版本号

- 1.1.1 (2018-08-08)
- 1.0.1 (2018-08-04)
- 1.0.0 (2018-08-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/dj_split
- gem 安装: `gem install dj_split`
- Bundler: `gem "dj_split"`
- 最新版本: 1.1.1
- 最新版归档: https://rubygems.org/downloads/dj_split-1.1.1.gem
- 版本锁定: `gem "dj_split", "~> 1.1.1"`
- 中央仓库: https://rubygems.org/
