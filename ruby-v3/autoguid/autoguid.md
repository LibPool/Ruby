# autoguid

**Tag**: testing, filesystem, data

## 简介

Autoguid lets you trivially add human readable uuids to all
   your models, a whitelisted set of models, or a blacklisted set.
   Indices are automatically created based on a configuration option.
   There's also a rake task that will backfill these uuids into resources that
   have already been created.
   To get started, include the gem file, run `bundle install`, then run
   `rake autoguid:install`. From there, edit the config/initializers/autoguid.rb
   file to specifcy your configuration. Next, migrate your tables with
   `rake autoguid:migrate:up` and `rake autoguid:migrate:backfill` as required.
   `rake autoguid:migrate:drop_all` will drop all autoguid generated columns and
   the data in them. You can always change the config/initializers/autoguid.rb file
   and rerun `rake autoguid:migrate:up` to add autoguid to new models.

## 官网

- 主页: http://hacktivism.cc
- 源码仓库: https://github.com/peterkinnaird/autoguid
- RubyGems: https://rubygems.org/gems/autoguid

## 历史版本号

- 1.1 (2014-09-24)
- 1.0 (2014-09-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/autoguid
- gem 安装: `gem install autoguid`
- Bundler: `gem "autoguid"`
- 最新版本: 1.1
- 最新版归档: https://rubygems.org/downloads/autoguid-1.1.gem
- 版本锁定: `gem "autoguid", "~> 1.1"`
- 中央仓库: https://rubygems.org/
