# carray

**Tag**: web, template

## 简介

Ruby/CArray adds multi-dimensional numerical arrays to Ruby. Elements are held
    in a single flat memory block, so whole-array work -- element-wise arithmetic,
    reductions along any axis, sorting, searching -- runs in C. Slicing, transposing,
    reshaping, and selecting by a boolean condition all return views that share
    storage with the original array and can be chained freely; nothing is copied
    until you ask for a copy. Any array, view included, can carry a mask marking
    individual elements as undefined, and arrays are exchanged with other numerical
    libraries without copying through Ruby's MemoryView protocol.

## 官网

- 主页: https://github.com/himotoyoshi/carray
- 文档: https://www.rubydoc.info/gems/carray/3.0.2
- RubyGems: https://rubygems.org/gems/carray

## 历史版本号

- 3.0.2 (2026-09-24)
- 3.0.1 (2026-09-06)
- 3.0.0 (2026-08-25)
- 2.0.1 (2025-12-22)
- 2.0.0 (2025-06-03)
- 1.5.9 (2023-06-19)
- 1.5.8 (2023-01-13)
- 1.5.7 (2021-06-16)
- 1.5.6 (2021-02-24)
- 1.5.5 (2021-02-02)
- 1.5.4 (2020-09-09)
- 1.5.3 (2020-07-31)
- 1.5.2 (2020-07-22)
- 1.5.1 (2020-07-01)
- 1.4.0 (2020-06-15)
- 1.3.7 (2020-04-07)
- 1.3.6 (2020-01-22)
- 1.3.5 (2019-09-02)
- 1.3.4 (2019-08-16)
- 1.3.3 (2019-08-06)
- 1.3.2 (2018-12-10)
- 1.3.1 (2018-10-02)
- 1.3.0 (2018-02-18)
- 1.2.0 (2017-02-09)
- 1.1.8 (2016-08-24)
- 1.1.7 (2016-05-06)
- 1.1.6 (2016-05-06)
- 1.1.5 (2016-05-06)
- 1.1.4 (2016-05-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/carray
- gem 安装: `gem install carray`
- Bundler: `gem "carray"`
- 最新版本: 3.0.2
- 最新版归档: https://rubygems.org/downloads/carray-3.0.2.gem
- 版本锁定: `gem "carray", "~> 3.0.2"`
- 中央仓库: https://rubygems.org/
