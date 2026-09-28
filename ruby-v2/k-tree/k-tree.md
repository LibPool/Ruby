# k-tree

**Tag**: testing, data

## 简介

This is a data structure to represent and manage k-trees,
  primarily created for use in RubyNEAT, but may see other possible applications.
  The goal here is to be roebust in the creation of your k-tree, to allow
  you to prune during creation, since, especially for higher-dimensional trees,
  the number of leaf node can become very large.

  So a parent will have children nodes created down to the desired resolution,
  and immediately after the creation of the children, will check to see if there's
  enough variance among the children to keep them. If not, they are pruned immediately.

## 官网

- 主页: http://github.com/flajann2/k-tree
- 文档: https://www.rubydoc.info/gems/k-tree/0.0.8
- RubyGems: https://rubygems.org/gems/k-tree

## 历史版本号

- 0.0.8 (2018-01-22)
- 0.0.7 (2016-12-27)
- 0.0.6 (2016-12-26)
- 0.0.3 (2015-06-21)
- 0.0.2 (2014-09-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/k-tree
- gem 安装: `gem install k-tree`
- Bundler: `gem "k-tree"`
- 最新版本: 0.0.8
- 最新版归档: https://rubygems.org/downloads/k-tree-0.0.8.gem
- 版本锁定: `gem "k-tree", "~> 0.0.8"`
- 中央仓库: https://rubygems.org/
