# leakferret

**Tag**: web, cli, networking, tooling

## 简介

Context-aware secret scanning for Ruby projects. A thin wrapper around the
native leakferret binary (written in Rust): it finds hardcoded secrets,
confirms which ones are actually live by calling the provider, and rewrites
them to read from environment variables instead.

Precompiled platform gems bundle the native binary inside the gem, so a
normal `gem install` ships the binary through RubyGems itself: no download,
no network access, and no Rust toolchain. You can audit exactly what you are
about to run with `gem unpack leakferret`. The gem never fetches and runs a
binary off the internet - there is no download code to vet. On a platform
without a prebuilt gem, the source gem tells you to build from source
(`cargo install leakferret-cli`) or point LEAKFERRET_BIN at a binary.

The API exposes Leakferret.scan, Leakferret.verify, and Leakferret.rewrite
(each returning Finding objects), plus a `leakferret` command-line tool.

## 官网

- 主页: https://github.com/leakferrethq/leakferret-ruby
- 文档: https://rubydoc.info/gems/leakferret
- 更新日志: https://github.com/leakferrethq/leakferret-ruby/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/leakferret

## 历史版本号

- 0.2.0 (2026-06-04)
- 0.2.0-x86_64-linux (2026-06-04)
- 0.2.0-x86_64-darwin (2026-06-04)
- 0.2.0-x64-mingw-ucrt (2026-06-04)
- 0.2.0-arm64-darwin (2026-06-04)
- 0.1.14 (2026-06-03)
- 0.1.13 (2026-06-03)
- 0.1.12 (2026-06-02)
- 0.1.10 (2026-06-02)
- 0.1.9 (2026-06-01)
- 0.1.8 (2026-06-01)
- 0.1.7 (2026-06-01)
- 0.1.6 (2026-06-01)
- 0.1.5 (2026-05-31)
- 0.1.4 (2026-05-31)
- 0.1.3 (2026-05-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/leakferret
- gem 安装: `gem install leakferret`
- Bundler: `gem "leakferret"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/leakferret-0.2.0.gem
- 版本锁定: `gem "leakferret", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
