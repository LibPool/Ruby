# lithos

**Tag**: database, data

## 简介

lithos is a self-contained embedded key-value store written from scratch as a
native extension — no external database dependency. It uses a log-structured
merge (LSM) tree: a write-ahead log makes every write durable, an in-memory
sorted memtable flushes to immutable SSTables (with bloom filters), and
compaction merges them. Keys and values are arbitrary binary strings; keys
are kept in sorted order so you get ordered iteration and range scans, plus
crash recovery via WAL replay. Windows MSVC (mswin) Ruby only.

## 官网

- 主页: https://github.com/main-path/lithos
- 更新日志: https://github.com/main-path/lithos/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/lithos/issues
- RubyGems: https://rubygems.org/gems/lithos

## 历史版本号

- 0.1.0 (2026-05-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/lithos
- gem 安装: `gem install lithos`
- Bundler: `gem "lithos"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/lithos-0.1.0.gem
- 版本锁定: `gem "lithos", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
