# smulube-fixture_dependencies

**Tag**: web, cli, database, testing, serialization, data

## 简介

fixture_dependencies is an advanced fixture loader for ActiveRecord and Sequel,  allowing the loading of models from YAML fixtures, along with their entire  dependency graph.  It has the following features:  - Fixtures specify association names instead of foreign keys - Support both Sequel and ActiveRecord - Supports many_to_one/belongs_to, one_to_many/has_many, many_to_many/has_and_belongs_to_many, and has_one associations - Loads a fixture's dependency graph in such a manner that foreign key constraints aren't violated - Has a very simple API (FixtureDependencies.load(:model__fixture)) - Handles almost all cyclic dependencies - Includes Rails and Sequel test helpers for Test::Unit (and a Sequel test helper for RSpec) that load fixtures for every test inside a transaction, so fixture data is never left in your database - Adds dynamic fixtures (similar to ActiveRecord) with ERb.

## 官网

- 文档: https://www.rubydoc.info/gems/smulube-fixture_dependencies/1.2.4
- RubyGems: https://rubygems.org/gems/smulube-fixture_dependencies

## 历史版本号

- 1.2.4 (2014-08-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/smulube-fixture_dependencies
- gem 安装: `gem install smulube-fixture_dependencies`
- Bundler: `gem "smulube-fixture_dependencies"`
- 最新版本: 1.2.4
- 最新版归档: https://rubygems.org/downloads/smulube-fixture_dependencies-1.2.4.gem
- 版本锁定: `gem "smulube-fixture_dependencies", "~> 1.2.4"`
- 中央仓库: https://rubygems.org/
