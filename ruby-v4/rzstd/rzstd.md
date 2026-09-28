# rzstd

**Tag**: library

## 简介

Ruby bindings (via Rust/magnus) for the Zstandard compressor with
persistent ZSTD_CCtx / ZSTD_DCtx contexts that are reused across
calls. Provides Zstd frame compress/decompress at module level and
a stateful Dictionary class for dict-bound compression. Designed to
be safe to call from multiple Ractors and competitive with rlz4 on
small messages, where per-call context allocation in zstd-ruby
dominates the cost.

## 官网

- 主页: https://github.com/paddor/rzstd
- RubyGems: https://rubygems.org/gems/rzstd

## 历史版本号

- 0.4.0 (2026-05-04)
- 0.3.0 (2026-04-15)
- 0.2.0 (2026-04-13)
- 0.1.0 (2026-04-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/rzstd
- gem 安装: `gem install rzstd`
- Bundler: `gem "rzstd"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/rzstd-0.4.0.gem
- 版本锁定: `gem "rzstd", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
