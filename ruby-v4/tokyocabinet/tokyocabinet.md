# tokyocabinet

**Tag**: database, filesystem, data

## 简介

Tokyo Cabinet is a library of routines for managing a database.  The database is a simple data file containing records, each is a pair of a key and a value.  Every key and value is serial bytes with variable length.  Both binary data and character string can be used as a key and a value.  There is neither concept of data tables nor data types.  Records are organized in hash table, B+ tree, or fixed-length array.

## 官网

- 主页: http://fallabs.com/tokyocabinet/
- 文档: https://www.rubydoc.info/gems/tokyocabinet/1.32.0
- RubyGems: https://rubygems.org/gems/tokyocabinet

## 历史版本号

- 1.32.0 (2016-04-08)
- 1.29.1 (2013-08-02)
- 1.29 (2009-10-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/tokyocabinet
- gem 安装: `gem install tokyocabinet`
- Bundler: `gem "tokyocabinet"`
- 最新版本: 1.32.0
- 最新版归档: https://rubygems.org/downloads/tokyocabinet-1.32.0.gem
- 版本锁定: `gem "tokyocabinet", "~> 1.32.0"`
- 中央仓库: https://rubygems.org/
