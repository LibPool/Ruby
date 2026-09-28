# disjoint_interval_tree

**Tag**: library

## 简介

A set of pairwise disjoint half-open intervals [a..b[, backed by an
augmented AVL tree written in C. Insertion, point lookup, intersection
queries and range removal are all logarithmic. Each node caches the hull of
the subtree it roots, so intersection queries prune whole subtrees in O(1).

## 官网

- 主页: https://github.com/anlsys/ruby-disjoint-interval-tree
- 问题追踪: https://github.com/anlsys/ruby-disjoint-interval-tree/issues
- RubyGems: https://rubygems.org/gems/disjoint_interval_tree

## 历史版本号

- 0.2.0 (2026-09-21)
- 0.1.0 (2026-09-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/disjoint_interval_tree
- gem 安装: `gem install disjoint_interval_tree`
- Bundler: `gem "disjoint_interval_tree"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/disjoint_interval_tree-0.2.0.gem
- 版本锁定: `gem "disjoint_interval_tree", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
