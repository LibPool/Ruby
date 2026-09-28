# dijkstra_fast

**Tag**: web, testing, networking, filesystem

## 简介

Native implementation of Dijkstra algorithm for finding the shortest path
between two vertices in a large, sparse graphs. Underlying algorithm is
implemented in C using a priority queue.  Edges are represented using linked
lists rather than an adjacency matrix to reduce memory footprint when operating
on very large graphs where the average number of edges between nodes is
relatively small (e.g. < 1/10 the number of nodes). See
https://en.wikipedia.org/wiki/Dijkstra's_algorithm for additional information.

## 官网

- 主页: https://github.com/david-mccullars/dijkstra_fast
- 文档: https://www.rubydoc.info/gems/dijkstra_fast/1.5.3
- RubyGems: https://rubygems.org/gems/dijkstra_fast

## 历史版本号

- 1.5.3 (2022-01-04)
- 1.5.2 (2022-01-04)
- 1.4.2 (2021-12-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/dijkstra_fast
- gem 安装: `gem install dijkstra_fast`
- Bundler: `gem "dijkstra_fast"`
- 最新版本: 1.5.3
- 最新版归档: https://rubygems.org/downloads/dijkstra_fast-1.5.3.gem
- 版本锁定: `gem "dijkstra_fast", "~> 1.5.3"`
- 中央仓库: https://rubygems.org/
