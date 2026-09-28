# rails_dm_datastore

**Tag**: web, template, filesystem, data

## 简介

This gem patches all of the problems that appear from running Rails with DataMapper on the GAE.  The main patches are patching DataMapper so that it does not use the ObjectSpace (The ObjectSpace itself is also patched so that this works seamlessly).  Also ActiveView is patched so that all of the partial shortcuts work with DataMapper.  In addition, a generate is provided (dd_model) that will produce a DataMapper model.  One last note is that this gem depends on a dm-core (and other dm gems), dm-appengein, and rails_appengene so all you need is to require this gem in your gem file and you should get all the other gems you need to make DataMapper work with Rails and the GAE.

## 官网

- 主页: http://github.com/joshsmoore/rails_dm_datastore
- RubyGems: https://rubygems.org/gems/rails_dm_datastore

## 历史版本号

- 0.2.17.pre (2010-11-17)
- 0.2.16 (2010-10-30)
- 0.2.15 (2010-10-30)
- 0.2.14 (2010-10-28)
- 0.2.13 (2010-10-19)
- 0.2.12.pre (2010-09-21)
- 0.2.11.pre (2010-09-13)
- 0.2.10 (2010-09-04)
- 0.2.9 (2010-04-19)
- 0.2.8 (2010-03-04)
- 0.2.6 (2010-03-02)
- 0.2.5 (2010-02-20)
- 0.2.4 (2010-02-08)
- 0.2.3 (2010-01-25)
- 0.2.2 (2010-01-14)
- 0.2.1 (2010-01-13)
- 0.2.0 (2010-01-12)
- 0.1.1 (2010-01-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails_dm_datastore
- gem 安装: `gem install rails_dm_datastore`
- Bundler: `gem "rails_dm_datastore"`
- 最新版本: 0.2.16
- 最新版归档: https://rubygems.org/downloads/rails_dm_datastore-0.2.16.gem
- 版本锁定: `gem "rails_dm_datastore", "~> 0.2.16"`
- 中央仓库: https://rubygems.org/
