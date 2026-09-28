# sequence

**Tag**: web, filesystem, data

## 简介

Sequence provides a unified api for access to sequential data types, like
Strings, Arrays, Files, IOs, and Enumerations. This is the external 
iterator pattern (ruby's usual iterators are internal). Each sequence 
encapsulates some data and a current position within it. Some operations 
apply to data at (or relative to) the position, others are independant 
of position. The api contains operations for moving the position, and 
reading  and writing data (with or without moving the position) forward 
or backward from the current position or anywhere.

Its perhaps most unusual feature is the ability to scan for Regexps in
not just Strings, but Files and any other type of sequence.

## 官网

- 主页: http://github.com/coatl/sequence
- 文档: https://www.rubydoc.info/gems/sequence/0.2.4
- RubyGems: https://rubygems.org/gems/sequence

## 历史版本号

- 0.2.4 (2016-08-12)
- 0.2.3 (2010-01-03)
- 0.2.2 (2009-08-07)
- 0.2.1 (2009-08-05)
- 0.2.0 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/sequence
- gem 安装: `gem install sequence`
- Bundler: `gem "sequence"`
- 最新版本: 0.2.4
- 最新版归档: https://rubygems.org/downloads/sequence-0.2.4.gem
- 版本锁定: `gem "sequence", "~> 0.2.4"`
- 中央仓库: https://rubygems.org/
