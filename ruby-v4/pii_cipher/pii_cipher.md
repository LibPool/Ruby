# pii_cipher

**Tag**: security

## 简介

PiiCipher lets you search encrypted PII columns in ActiveRecord without ever
storing or querying plaintext. It generates HMAC-SHA256 blind indexes alongside
your ciphertext — trigram arrays for partial (substring) searches and single
hashes for exact-match lookups. The hash functions run in a native Rust
extension for performance. Query interception is transparent: call `where`
as normal and PiiCipher rewrites the query against the blind index automatically.

## 官网

- 主页: https://github.com/selvachezhian/pii_cipher
- 更新日志: https://github.com/selvachezhian/pii_cipher/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/pii_cipher

## 历史版本号

- 0.1.1 (2026-06-29)
- 0.1.1-x86_64-linux (2026-06-29)
- 0.1.1-x86_64-linux-musl (2026-06-29)
- 0.1.1-x86_64-darwin (2026-06-29)
- 0.1.1-x64-mingw-ucrt (2026-06-29)
- 0.1.1-arm64-darwin (2026-06-29)
- 0.1.1-arm-linux (2026-06-29)
- 0.1.1-aarch64-mingw-ucrt (2026-06-29)
- 0.1.1-aarch64-linux (2026-06-29)
- 0.1.1-aarch64-linux-musl (2026-06-29)
- 0.1.0 (2026-06-29)
- 0.1.0-x86_64-linux (2026-06-29)
- 0.1.0-x86_64-darwin (2026-06-29)
- 0.1.0-x64-mingw-ucrt (2026-06-29)
- 0.1.0-arm64-darwin (2026-06-29)
- 0.1.0-aarch64-linux (2026-06-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/pii_cipher
- gem 安装: `gem install pii_cipher`
- Bundler: `gem "pii_cipher"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/pii_cipher-0.1.1.gem
- 版本锁定: `gem "pii_cipher", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
