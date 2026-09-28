# pipeloader

**Tag**: networking, tooling, data

## 简介

During GraphQL response building, Pipeloader routes ActiveRecord SELECTs through a libpq pipeline so a query tree resolves in roughly one round trip per level — with plain resolvers and plain models, no Futures, no dataloader.load, no resolver changes. Also ships Pipeloader::Batch: declarative batch-loaded associations and aggregates that eliminate N+1 in plain ActiveRecord traversal via AR's own Preloader.

## 官网

- 主页: https://github.com/joshbuddy/pipeloader
- 文档: https://www.rubydoc.info/gems/pipeloader/0.0.3
- RubyGems: https://rubygems.org/gems/pipeloader

## 历史版本号

- 0.0.3 (2026-06-19)
- 0.0.2 (2026-06-19)
- 0.0.1 (2026-06-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/pipeloader
- gem 安装: `gem install pipeloader`
- Bundler: `gem "pipeloader"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/pipeloader-0.0.3.gem
- 版本锁定: `gem "pipeloader", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
