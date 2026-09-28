# sidekiq-disposal

**Tag**: library

## 简介

A mechanism to mark Sidekiq Jobs to be disposed of by Job ID, Batch ID, or Job Class.
Disposal here means to either `:kill` the Job (send to the Dead queue) or `:discard` it (throw it away), at the time the job is picked up and processed by Sidekiq.

## 官网

- 主页: https://github.com/hibachrach/sidekiq-disposal
- 更新日志: https://github.com/hibachrach/sidekiq-disposal/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/sidekiq-disposal

## 历史版本号

- 0.2.0 (2024-12-19)
- 0.1.0 (2024-12-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq-disposal
- gem 安装: `gem install sidekiq-disposal`
- Bundler: `gem "sidekiq-disposal"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/sidekiq-disposal-0.2.0.gem
- 版本锁定: `gem "sidekiq-disposal", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
