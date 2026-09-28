# sidekiq-cluster

**Tag**: cli, filesystem

## 简介

This library provides CLI interface for starting multiple copies of Sidekiq in parallel,    typically to take advantage of multi-core systems.  By default it starts N - 1 processes,    where N is the number of cores on the current system. Sidekiq Cluster is controlled with CLI    flags that appear before `--` (double dash), while any arguments that follow double dash are    passed to each Sidekiq process. The exception is the `-P pidfile`, which clustering script    passes to each sidekiq process individually.

## 官网

- 主页: https://github.com/kigster/sidekiq-cluster
- 文档: https://www.rubydoc.info/gems/sidekiq-cluster/0.1.2
- RubyGems: https://rubygems.org/gems/sidekiq-cluster

## 历史版本号

- 0.1.2 (2018-05-02)
- 0.1.1 (2018-05-02)
- 0.1.0 (2018-05-02)
- 0.0.1 (2018-05-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq-cluster
- gem 安装: `gem install sidekiq-cluster`
- Bundler: `gem "sidekiq-cluster"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/sidekiq-cluster-0.1.2.gem
- 版本锁定: `gem "sidekiq-cluster", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
