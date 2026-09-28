# quic

**Tag**: web, security

## 简介

A thin Ruby binding around ngtcp2 for the QUIC transport protocol, using picotls for TLS 1.3. ngtcp2 and picotls are vendored via mini_portile2 at install time and linked statically; the crypto primitives and X.509 come from the host's OpenSSL (or LibreSSL), linked dynamically, so the process shares one libcrypto with Ruby's openssl extension. The API is intentionally optimized for synchronous I/O and String-based buffers. Public API is not yet stable.

## 官网

- 主页: https://github.com/unasuke/quic-ruby
- 更新日志: https://github.com/unasuke/quic-ruby/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/quic

## 历史版本号

- 0.0.2 (2026-09-27)
- 0.0.1 (2026-05-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/quic
- gem 安装: `gem install quic`
- Bundler: `gem "quic"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/quic-0.0.2.gem
- 版本锁定: `gem "quic", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
