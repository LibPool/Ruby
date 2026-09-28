# tastebook-spawn

**Tag**: database, data

## 简介

This plugin provides a 'spawn' method to easily fork OR
thread long-running sections of code so that your application can return
results to your users more quickly.  This plugin works by creating new database
connections in ActiveRecord::Base for the spawned block.

The plugin also patches ActiveRecord::Base to handle some known bugs when using
threads (see lib/patches.rb).

## 官网

- 主页: http://github.com/tra/spawn
- RubyGems: https://rubygems.org/gems/tastebook-spawn

## 历史版本号

- 1.0.1 (2013-05-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/tastebook-spawn
- gem 安装: `gem install tastebook-spawn`
- Bundler: `gem "tastebook-spawn"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/tastebook-spawn-1.0.1.gem
- 版本锁定: `gem "tastebook-spawn", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
