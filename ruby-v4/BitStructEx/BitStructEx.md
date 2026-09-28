# BitStructEx

**Tag**: web, testing, networking, data

## 简介

Allows the specification of bit-based structures and provides an intuitive way of access data.  Example:  class Flags &lt; StructBase unsigned :direction, 4 unsigned :multiplier, 2 unsigned :offset, 2 end  class Entry &lt; StructBase unsigned :offset, 4 nested   :flags, Flags unsigned :address, 24 unsigned :cache_id, 16 end  In contrast to the already available http://raa.ruby-lang.org/project/bit-struct/ implementation, BitStructEx allows nested structures which are not aligned on byte boundaries.

## 官网

- 文档: https://www.rubydoc.info/gems/BitStructEx/0.0.91
- RubyGems: https://rubygems.org/gems/BitStructEx

## 历史版本号

- 0.0.91 (2009-07-25)
- 0.0.86 (2009-07-25)
- 0.0.85 (2009-07-25)
- 0.0.74 (2009-07-25)
- 0.0.65 (2009-07-25)
- 0.0.64 (2009-07-25)
- 0.0.54 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/BitStructEx
- gem 安装: `gem install BitStructEx`
- Bundler: `gem "BitStructEx"`
- 最新版本: 0.0.91
- 最新版归档: https://rubygems.org/downloads/BitStructEx-0.0.91.gem
- 版本锁定: `gem "BitStructEx", "~> 0.0.91"`
- 中央仓库: https://rubygems.org/
