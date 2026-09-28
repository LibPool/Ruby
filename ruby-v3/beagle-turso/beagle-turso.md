# beagle-turso

**Tag**: database, filesystem, data

## 简介

A Ruby driver for Turso's database engine, backed by a native Rust
extension (beagle_turso_core, via Magnus/rb-sys). Opens a local-only
database (in-memory or on-disk) or one kept in sync with a remote Turso
database via explicit push/pull. Writes are durable to the local file
immediately as they happen; push is what propagates them to the remote
on sync, not synchronously with every write.

## 官网

- 主页: https://github.com/BeagleSoftwareUK/beagle-turso
- RubyGems: https://rubygems.org/gems/beagle-turso

## 历史版本号

- 0.1.3-x86_64-linux (2026-08-09)
- 0.1.3-arm64-darwin (2026-08-09)
- 0.1.3 (2026-08-09)
- 0.1.3-x86_64-linux-musl (2026-08-09)
- 0.1.3-aarch64-linux (2026-08-09)
- 0.1.3-x86_64-darwin (2026-08-09)
- 0.1.2-x86_64-linux-musl (2026-08-08)
- 0.1.2-x86_64-darwin (2026-08-08)
- 0.1.2-arm64-darwin (2026-08-08)
- 0.1.2-x86_64-linux (2026-08-08)
- 0.1.2-aarch64-linux (2026-08-08)
- 0.1.2 (2026-08-08)
- 0.1.1-aarch64-linux (2026-08-08)
- 0.1.1-arm64-darwin (2026-08-08)
- 0.1.1-x86_64-linux-musl (2026-08-08)
- 0.1.1 (2026-08-08)
- 0.1.1-x86_64-darwin (2026-08-08)
- 0.1.1-x86_64-linux (2026-08-08)
- 0.1.0-x86_64-linux-musl (2026-08-08)
- 0.1.0-x86_64-darwin (2026-08-08)
- 0.1.0-aarch64-linux (2026-08-08)
- 0.1.0 (2026-08-08)
- 0.1.0-arm64-darwin (2026-08-08)
- 0.1.0-x86_64-linux (2026-08-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/beagle-turso
- gem 安装: `gem install beagle-turso`
- Bundler: `gem "beagle-turso"`
- 最新版本: 0.1.3
- 最新版归档: https://rubygems.org/downloads/beagle-turso-0.1.3.gem
- 版本锁定: `gem "beagle-turso", "~> 0.1.3"`
- 中央仓库: https://rubygems.org/
