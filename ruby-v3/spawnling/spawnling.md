# spawnling

**Tag**: database, data

## 简介

This plugin provides a 'Spawnling' class to easily fork OR
thread long-running sections of code so that your application can return
results to your users more quickly.  This plugin works by creating new database
connections in ActiveRecord::Base for the spawned block.

The plugin also patches ActiveRecord::Base to handle some known bugs when using
threads (see lib/patches.rb).

## 官网

- 主页: http://github.com/tra/spawnling
- 文档: https://www.rubydoc.info/gems/spawnling/2.1.6
- RubyGems: https://rubygems.org/gems/spawnling

## 历史版本号

- 2.1.6 (2015-05-14)
- 2.1.5 (2014-07-06)
- 2.1.4 (2014-06-03)
- 2.1.3 (2014-06-02)
- 2.1.2 (2014-06-01)
- 2.1.1 (2013-04-15)
- 2.1 (2013-04-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/spawnling
- gem 安装: `gem install spawnling`
- Bundler: `gem "spawnling"`
- 最新版本: 2.1.6
- 最新版归档: https://rubygems.org/downloads/spawnling-2.1.6.gem
- 版本锁定: `gem "spawnling", "~> 2.1.6"`
- 中央仓库: https://rubygems.org/
