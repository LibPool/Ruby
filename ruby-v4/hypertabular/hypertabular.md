# hypertabular

**Tag**: filesystem, data

## 简介

CSV, TSV and any single-byte ASCII separator, and XLSX and ODS workbooks, read by a
native Rust core into typed column batches. The core owns no memory: this gem allocates the buffers once and the
core fills them in one native call per batch. Every cell is a HyperCast verdict — the
value, or a reason plus the offending span — and a file that is not rows of cells at
all is an exception raised after the intact rows. Two backends behind one surface,
selected automatically and both shipped prebuilt: a Magnus extension where a precompiled
platform gem matches, and stdlib Fiddle everywhere else. No compile on install.

## 官网

- 主页: https://github.com/SkunkWerkx/HyperTabular
- 文档: https://github.com/SkunkWerkx/HyperTabular/tree/master/ruby#readme
- 更新日志: https://github.com/SkunkWerkx/HyperTabular/blob/master/CHANGELOG.md
- 问题追踪: https://github.com/SkunkWerkx/HyperTabular/issues
- RubyGems: https://rubygems.org/gems/hypertabular

## 历史版本号

- 0.9.0 (2026-10-21)
- 0.9.0-x86_64-linux-musl (2026-10-21)
- 0.9.0-x86_64-linux-gnu (2026-10-21)
- 0.9.0-x64-mingw-ucrt (2026-10-21)
- 0.9.0-arm64-darwin (2026-10-21)
- 0.9.0-aarch64-mingw-ucrt (2026-10-21)
- 0.9.0-aarch64-linux-musl (2026-10-21)
- 0.9.0-aarch64-linux-gnu (2026-10-21)
- 0.8.0 (2026-10-09)
- 0.8.0-x86_64-linux-musl (2026-10-09)
- 0.8.0-x86_64-linux-gnu (2026-10-09)
- 0.8.0-x64-mingw-ucrt (2026-10-09)
- 0.8.0-arm64-darwin (2026-10-09)
- 0.8.0-aarch64-mingw-ucrt (2026-10-09)
- 0.8.0-aarch64-linux-musl (2026-10-09)
- 0.8.0-aarch64-linux-gnu (2026-10-09)
- 0.7.0 (2026-10-07)
- 0.7.0-x86_64-linux-musl (2026-10-07)
- 0.7.0-x86_64-linux-gnu (2026-10-07)
- 0.7.0-x64-mingw-ucrt (2026-10-07)
- 0.7.0-arm64-darwin (2026-10-07)
- 0.7.0-aarch64-mingw-ucrt (2026-10-07)
- 0.7.0-aarch64-linux-musl (2026-10-07)
- 0.7.0-aarch64-linux-gnu (2026-10-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/hypertabular
- gem 安装: `gem install hypertabular`
- Bundler: `gem "hypertabular"`
- 最新版本: 0.9.0
- 最新版归档: https://rubygems.org/downloads/hypertabular-0.9.0.gem
- 版本锁定: `gem "hypertabular", "~> 0.9.0"`
- 中央仓库: https://rubygems.org/
