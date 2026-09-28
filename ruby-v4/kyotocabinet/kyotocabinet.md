# kyotocabinet

**Tag**: database, filesystem, data

## 简介

Kyoto Cabinet is a library of routines for managing a database.  The database is a simple data file containing records, each is a pair of a key and a value.  Every key and value is serial bytes with variable length.  Both binary data and character string can be used as a key and a value.  Each key must be unique within a database.  There is neither concept of data tables nor data types.  Records are organized in hash table or B+ tree.

## 官网

- 主页: http://1978th.net/kyotocabinet/
- RubyGems: https://rubygems.org/gems/kyotocabinet

## 历史版本号

- 1.0 (2010-06-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/kyotocabinet
- gem 安装: `gem install kyotocabinet`
- Bundler: `gem "kyotocabinet"`
- 最新版本: 1.0
- 最新版归档: https://rubygems.org/downloads/kyotocabinet-1.0.gem
- 版本锁定: `gem "kyotocabinet", "~> 1.0"`
- 中央仓库: https://rubygems.org/
