# foreign_key_saver

**Tag**: web, database, testing

## 简介

Adds a add_foreign_key_constraint schema method, and extends the schema dump code to output these
foreign key constraints.

Only MySQL and PostgreSQL are currently supported.


Examples
========

# adds a constraint on projects.customer_id with parent customers.id
add_foreign_key :projects, :customer_id, :customers, :id

# adds a constraint on projects(a, b) with parent(a, b) with the default RESTRICT update/delete actions
add_foreign_key "child", ["a", "b"], "parent", ["a", "b"]

# adds a constraint with the ON UPDATE action set to CASCADE and the ON DELETE action set to SET NULL
add_foreign_key 'projects', 'customer_id', 'customers', 'id', :on_update => :cascade, :on_delete => :set_null

The following actions are defined:
  :restrict
  :no_action
  :cascade
  :set_null (aka :nullify)
  :set_default
Note that MySQL does not support :set_default, and also treats :no_action as :restrict.


Compatibility
=============

Supports mysql, mysql2, postgresql.

Currently tested against Rails 3.2.13 on 2.0.0p0 and Rails 3.2.13, 3.1.8, 3.0.17, and 2.3.14 on Ruby 1.8.7.

## 官网

- 主页: http://github.com/willbryant/foreign_key_saver
- RubyGems: https://rubygems.org/gems/foreign_key_saver

## 历史版本号

- 2.0.0 (2013-04-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/foreign_key_saver
- gem 安装: `gem install foreign_key_saver`
- Bundler: `gem "foreign_key_saver"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/foreign_key_saver-2.0.0.gem
- 版本锁定: `gem "foreign_key_saver", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
