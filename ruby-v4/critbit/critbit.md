# critbit

**Tag**: web, networking, template, data

## 简介

A crit bit tree, also known as a Binary Patricia Trie is a trie
(https://en.wikipedia.org/wiki/Trie), also called digital tree and sometimes radix tree
or prefix tree (as they can be searched by prefixes), is an ordered tree data structure
that is used to store a dynamic set or associative array where the keys are usually
strings.

Unlike a binary search tree, no node in the tree stores the key associated with that
node; instead, its position in the tree defines the key with which it is associated.
All the descendants of a node have a common prefix of the string associated with
that node, and the root is associated with the empty string. Values are normally
not associated with every node, only with leaves and some inner nodes that
correspond to keys of interest. For the space-optimized presentation
of prefix tree, see compact prefix tree.

This code is a wrapper around https://github.com/jfager/functional-critbit.

For more information go to: http://cr.yp.to/critbit.html

## 官网

- 主页: http://github.com/rbotafogo/critbit/wiki
- 文档: https://www.rubydoc.info/gems/critbit/0.5.2
- RubyGems: https://rubygems.org/gems/critbit

## 历史版本号

- 0.5.2-java (2016-05-10)
- 0.5.1-java (2015-12-30)
- 0.5.0-java (2015-07-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/critbit
- gem 安装: `gem install critbit`
- Bundler: `gem "critbit"`
- 最新版本: 0.5.2
- 最新版归档: https://rubygems.org/downloads/critbit-0.5.2.gem
- 版本锁定: `gem "critbit", "~> 0.5.2"`
- 中央仓库: https://rubygems.org/
