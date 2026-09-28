# index_tree

**Tag**: library

## 简介

This Gem eagerly loads trees by indexing the nodes of the tree. The number of queries needed for loading a tree is N,
Where N is the number of different models(ActiveRecords) in the tree.
Each inner object in the tree have an index node instance that is connecting it to the root.
When the root of the tree is loaded, only the objects that are in the tree are fetched(Pruning).
The index nodes are created when the root element is saved and stored in the IndexNode model.

## 官网

- 主页: http://www.naturalint.com
- 源码仓库: https://github.com/Natural-Intelligence/index_tree
- 文档: https://github.com/Natural-Intelligence/index_tree/blob/master/README.md
- 问题追踪: https://github.com/Natural-Intelligence/index_tree/issues
- RubyGems: https://rubygems.org/gems/index_tree

## 历史版本号

- 0.0.5 (2014-10-04)
- 0.0.3 (2014-10-01)
- 0.0.1 (2014-09-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/index_tree
- gem 安装: `gem install index_tree`
- Bundler: `gem "index_tree"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/index_tree-0.0.5.gem
- 版本锁定: `gem "index_tree", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
