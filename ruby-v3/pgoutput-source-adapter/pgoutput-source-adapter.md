# pgoutput-source-adapter

**Tag**: database, data

## 简介

pgoutput-source-adapter provides source adapters that normalize
decoded PostgreSQL pgoutput events into downstream event models.

The gem currently includes a CDC::Core adapter that transforms
pgoutput decoder events into ChangeEvent and TransactionEnvelope
primitives while preserving transaction and metadata context.

This package forms the normalization boundary between the
pgoutput family of gems and downstream change-event platforms.

## 官网

- 主页: https://github.com/kanutocd/pgoutput-source-adapter
- 文档: https://kanutocd.github.io/pgoutput-source-adapter/
- 更新日志: https://github.com/kanutocd/pgoutput-source-adapter/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/pgoutput-source-adapter

## 历史版本号

- 0.3.1 (2026-07-18)
- 0.3.0 (2026-07-17)
- 0.2.0 (2026-07-17)
- 0.1.1 (2026-06-16)
- 0.1.0 (2026-06-16)
- 0.0.0 (2026-06-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/pgoutput-source-adapter
- gem 安装: `gem install pgoutput-source-adapter`
- Bundler: `gem "pgoutput-source-adapter"`
- 最新版本: 0.3.1
- 最新版归档: https://rubygems.org/downloads/pgoutput-source-adapter-0.3.1.gem
- 版本锁定: `gem "pgoutput-source-adapter", "~> 0.3.1"`
- 中央仓库: https://rubygems.org/
