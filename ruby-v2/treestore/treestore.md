# treestore

**Tag**: database, data

## 简介

treestore stores two different types of data:
1) values, which are stored according to their SHA-1 hashcode
2) trees, which are sets of values and/or other trees, stored via a SHA-1 hashcode

In addition, there are references that allow you to 'bookmark' a SHA-1 hashcode for easier lookup.

If you think of the core git, but on any key-value backend store (like the included Redis one), you've got the right idea.

## 官网

- 文档: https://www.rubydoc.info/gems/treestore/0.1.0
- RubyGems: https://rubygems.org/gems/treestore

## 历史版本号

- 0.1.0 (2013-05-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/treestore
- gem 安装: `gem install treestore`
- Bundler: `gem "treestore"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/treestore-0.1.0.gem
- 版本锁定: `gem "treestore", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
