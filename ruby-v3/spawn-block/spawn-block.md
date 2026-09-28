# spawn-block

**Tag**: database, data

## 简介

This plugin provides a 'Spawn' class to easily fork OR
thread long-running sections of code so that your application can return
results to your users more quickly.  This plugin works by creating new database
connections in ActiveRecord::Base for the spawned block.

The plugin also patches ActiveRecord::Base to handle some known bugs when using
threads (see lib/patches.rb).

## 官网

- 主页: http://github.com/tra/spawn
- RubyGems: https://rubygems.org/gems/spawn-block

## 历史版本号

- 2.0 (2013-04-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/spawn-block
- gem 安装: `gem install spawn-block`
- Bundler: `gem "spawn-block"`
- 最新版本: 2.0
- 最新版归档: https://rubygems.org/downloads/spawn-block-2.0.gem
- 版本锁定: `gem "spawn-block", "~> 2.0"`
- 中央仓库: https://rubygems.org/
