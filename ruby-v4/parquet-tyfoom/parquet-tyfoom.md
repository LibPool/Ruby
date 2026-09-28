# parquet-tyfoom

**Tag**: web, filesystem

## 简介

Tyfoom's fork of the `parquet` gem (github.com/njaremko/parquet-ruby), published while the
    incremental streaming-write fix is pending upstream. It wraps the official Apache Rust
    implementation and bounds write memory by streaming row groups to disk instead of buffering the
    whole file. Drop-in compatible with the upstream gem: the library is still required as
    `require "parquet"` and exposes the same `Parquet` API.

## 官网

- 主页: https://github.com/cameronmccord2/parquet-ruby
- 文档: https://www.rubydoc.info/gems/parquet-tyfoom
- 更新日志: https://github.com/cameronmccord2/parquet-ruby/blob/stream-writes-incrementally/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/parquet-tyfoom

## 历史版本号

- 0.8.0-x86_64-linux (2026-07-02)
- 0.8.0-aarch64-linux-musl (2026-07-02)
- 0.8.0-x86_64-linux-musl (2026-07-02)
- 0.8.0-aarch64-linux (2026-07-02)
- 0.8.0-arm64-darwin (2026-07-02)
- 0.8.0-x86_64-darwin (2026-07-02)
- 0.8.0 (2026-07-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/parquet-tyfoom
- gem 安装: `gem install parquet-tyfoom`
- Bundler: `gem "parquet-tyfoom"`
- 最新版本: 0.8.0
- 最新版归档: https://rubygems.org/downloads/parquet-tyfoom-0.8.0.gem
- 版本锁定: `gem "parquet-tyfoom", "~> 0.8.0"`
- 中央仓库: https://rubygems.org/
