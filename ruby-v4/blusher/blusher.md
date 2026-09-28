# blusher

**Tag**: testing, template, filesystem

## 简介

blusher routes Ruby's rouge lexing — and, for the common HTML path, its
formatting — through the Rust `carmine` engine, which executes rule tables
extracted from rouge's own lexers. For an unadorned Rouge::Formatters::HTML
pipeline it fuses lex+format in Rust and returns one String, crossing the
Ruby boundary once instead of per-token: ~1.7x faster on a mixed corpus
(2.5x+ on large files), byte-identical, with transparent fallback to rouge
for callback lexers and other formatters. Verified against rouge's full
lexer spec suite (757/757). The engine's raw 4.6x is realized Rust-to-Rust.

## 官网

- 主页: https://github.com/momiji-rs/blusher
- 更新日志: https://github.com/momiji-rs/blusher/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/blusher

## 历史版本号

- 0.1.2 (2026-06-17)
- 0.1.2-x86_64-linux (2026-06-17)
- 0.1.2-x86_64-linux-musl (2026-06-17)
- 0.1.2-x86_64-darwin (2026-06-17)
- 0.1.2-x64-mingw-ucrt (2026-06-17)
- 0.1.2-arm64-darwin (2026-06-17)
- 0.1.2-aarch64-linux (2026-06-17)
- 0.1.2-aarch64-linux-musl (2026-06-17)
- 0.1.1 (2026-06-17)
- 0.1.0 (2026-06-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/blusher
- gem 安装: `gem install blusher`
- Bundler: `gem "blusher"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/blusher-0.1.2.gem
- 版本锁定: `gem "blusher", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
