# activejob-debounce

**Tag**: database

## 简介

A zero-dependency debouncing solution for ActiveJob. Uses Redis GETSET for
atomic dispatch-time gating — only 1 job enters the queue per debounce window.
Subsequent calls are true no-ops (nothing queued). Includes crash recovery
via expired timestamp detection. Works with any ActiveJob backend: Sidekiq,
GoodJob, Solid Queue, Resque, etc.

## 官网

- 主页: https://github.com/m2cci-bouzentm/activejob-debounce
- 更新日志: https://github.com/m2cci-bouzentm/activejob-debounce/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/activejob-debounce

## 历史版本号

- 1.0.1 (2026-07-02)
- 1.0.0 (2026-07-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/activejob-debounce
- gem 安装: `gem install activejob-debounce`
- Bundler: `gem "activejob-debounce"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/activejob-debounce-1.0.1.gem
- 版本锁定: `gem "activejob-debounce", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
