# simple_file_cache

**Tag**: testing, serialization, filesystem, data

## 简介

SimpleFileCache writes a ruby object to a binary file so that it can be retrieved later from the disk rather than recomputed from scratch. It defines a single method #load_or_recompute that receives a file path and a block. If the file exists and is recent (last changed today), it returns the file contents read with Marshal#load. Otherwise, it executesthe block, saves its return value with Marshal#dump and returns the new data.

## 官网

- 文档: https://www.rubydoc.info/gems/simple_file_cache/0.0.1
- RubyGems: https://rubygems.org/gems/simple_file_cache

## 历史版本号

- 0.0.1 (2018-11-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/simple_file_cache
- gem 安装: `gem install simple_file_cache`
- Bundler: `gem "simple_file_cache"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/simple_file_cache-0.0.1.gem
- 版本锁定: `gem "simple_file_cache", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
