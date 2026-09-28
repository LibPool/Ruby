# arboreal

**Tag**: filesystem, data

## 简介

Arboreal is yet another extension to ActiveRecord to support tree-shaped data structures.

Internally, Arboreal maintains a computed "ancestry_string" column, which caches the path from the root of
a tree to each node, allowing efficient retrieval of both ancestors and descendants.

Arboreal surfaces relationships within the tree like "children", "ancestors", "descendants", and "siblings"
as scopes, so that additional filtering/pagination can be performed.

## 官网

- 主页: http://github.com/mdub/arboreal
- RubyGems: https://rubygems.org/gems/arboreal

## 历史版本号

- 0.2.1 (2012-12-18)
- 0.2.0 (2011-11-02)
- 0.1.2 (2011-05-05)
- 0.1.1 (2010-09-14)
- 0.1.0 (2010-04-18)
- 0.0.5 (2010-04-06)
- 0.0.4 (2010-04-06)
- 0.0.3 (2010-04-05)
- 0.0.2 (2010-04-01)
- 0.0.1 (2010-04-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/arboreal
- gem 安装: `gem install arboreal`
- Bundler: `gem "arboreal"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/arboreal-0.2.1.gem
- 版本锁定: `gem "arboreal", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
