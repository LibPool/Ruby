# geotree

**Tag**: data

## 简介

A GeoTree  is a variant of a k-d tree, and stores data points that have a latitude and longitude, 
a unique integer identifier, and an optional 'weight' (e.g., the size of a city).  
GeoTrees are disk-based data structures and can store a very large number of points efficiently.
If desired, for smaller data sets, memory-only trees can be constructed instead.

The gem includes MultiTree, a GeoTree variant that supports queries at 
multiple levels of detail. For example, when focusing on a 
small region it can return points that would be omitted when querying a much larger region.

## 官网

- 主页: http://www.cs.ubc.ca/~jpsember/
- RubyGems: https://rubygems.org/gems/geotree

## 历史版本号

- 1.1.5 (2013-04-15)
- 1.1.4 (2013-04-09)
- 1.1.3 (2013-04-04)
- 1.1.2 (2013-04-04)
- 1.1.1 (2013-04-03)
- 1.1.0 (2013-04-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/geotree
- gem 安装: `gem install geotree`
- Bundler: `gem "geotree"`
- 最新版本: 1.1.5
- 最新版归档: https://rubygems.org/downloads/geotree-1.1.5.gem
- 版本锁定: `gem "geotree", "~> 1.1.5"`
- 中央仓库: https://rubygems.org/
