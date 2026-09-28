# has_normalized_sti

**Tag**: web, database, data

## 简介

has_normalzied_sti is a rails extension to allow Single Table Inheritance
      to work with a database normalized type column.
      The extension expects the STI model to have a type_id column instead of
      a type column. type_id should reference a Types table containg all the possible types.
      The types table will be auto populated with new types as new
      subclasses are saved.

## 官网

- 源码仓库: https://github.com/kjg/has_normalized_sti
- 文档: http://rubydoc.info/github/kjg/has_normalized_sti/master/frames
- 问题追踪: https://github.com/kjg/has_normalized_sti/issues
- RubyGems: https://rubygems.org/gems/has_normalized_sti

## 历史版本号

- 1.1.1 (2011-09-20)
- 1.1.0 (2011-09-20)
- 1.0.0 (2011-06-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/has_normalized_sti
- gem 安装: `gem install has_normalized_sti`
- Bundler: `gem "has_normalized_sti"`
- 最新版本: 1.1.1
- 最新版归档: https://rubygems.org/downloads/has_normalized_sti-1.1.1.gem
- 版本锁定: `gem "has_normalized_sti", "~> 1.1.1"`
- 中央仓库: https://rubygems.org/
