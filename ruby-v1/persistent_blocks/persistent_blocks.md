# persistent_blocks

**Tag**: serialization, filesystem, data

## 简介

This gem provides a rake extension to wrap blocks of ruby code so
  that the output of the block is persisted using marshal.  Blocks
  with persisted data will not be rerun and their data is available to
  subsequent blocks which can themselves generate persistent data.
  This allow a very simple and robust pipeline to be constructed in
  within a regular rakefile.

## 官网

- 主页: http://github.com/morrifeldman/persistent_blocks
- 文档: https://www.rubydoc.info/gems/persistent_blocks/0.1.0
- RubyGems: https://rubygems.org/gems/persistent_blocks

## 历史版本号

- 0.1.0 (2013-09-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/persistent_blocks
- gem 安装: `gem install persistent_blocks`
- Bundler: `gem "persistent_blocks"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/persistent_blocks-0.1.0.gem
- 版本锁定: `gem "persistent_blocks", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
