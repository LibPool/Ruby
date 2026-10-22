# sqlite_search

**Tag**: database, data

## 简介

Full-text, vector, and hybrid search for ActiveRecord, without leaving SQLite. sqlite_search gives a model full-text search (FTS5 with BM25 ranking), vector search (sqlite-vec through the neighbor gem, with your app supplying embeddings), and hybrid search that fuses the two with Reciprocal Rank Fusion and an optional reranking step, all behind one declarative DSL. No search cluster to run, no separate copy of your data, no database triggers, and a schema that restores cleanly from schema.rb.

## 官网

- 主页: https://github.com/radioactive-labs/sqlite_search
- 文档: https://github.com/radioactive-labs/sqlite_search#readme
- 更新日志: https://github.com/radioactive-labs/sqlite_search/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/radioactive-labs/sqlite_search/issues
- RubyGems: https://rubygems.org/gems/sqlite_search

## 历史版本号

- 0.1.0 (2026-10-05)
- 0.0.1 (2026-10-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/sqlite_search
- gem 安装: `gem install sqlite_search`
- Bundler: `gem "sqlite_search"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/sqlite_search-0.1.0.gem
- 版本锁定: `gem "sqlite_search", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
