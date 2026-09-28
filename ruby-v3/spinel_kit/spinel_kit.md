# spinel_kit

**Tag**: serialization, tooling

## 简介

SpinelKit consolidates the pure-Ruby shims that every Spinel-compiled
project would otherwise hand-roll and that Spinel (the Ruby->native AOT
compiler) does not provide: .git/HEAD provenance, URL percent-codec +
query parsing, a minimal levelled logger, and a hex digit/byte codec.
(JSON left in 0.3.0: Spinel now bundles `json` as a require-gated stdlib
package, so consumers use JSON.parse/JSON.generate directly.) Pure Ruby,
no native extension, no runtime dependencies -- it vendors cleanly via
bundler-spinel. Pre-alpha.

## 官网

- 主页: https://github.com/OriPekelman/spinelkit
- 文档: https://github.com/OriPekelman/spinelkit#readme
- 更新日志: https://github.com/OriPekelman/spinelkit/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/OriPekelman/spinelkit/issues
- RubyGems: https://rubygems.org/gems/spinel_kit

## 历史版本号

- 0.3.0 (2026-07-09)
- 0.2.0 (2026-06-08)
- 0.1.1 (2026-06-08)
- 0.1.0 (2026-06-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/spinel_kit
- gem 安装: `gem install spinel_kit`
- Bundler: `gem "spinel_kit"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/spinel_kit-0.3.0.gem
- 版本锁定: `gem "spinel_kit", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
