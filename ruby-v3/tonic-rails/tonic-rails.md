# tonic-rails

**Tag**: web, serialization, networking

## 简介

Tonic::Rails serves gRPC from Rails applications. The transport layer
(HTTP/2 framing, connection management, TLS, health checks, reflection)
is handled by tonic in Rust and exposed to Ruby through a native
extension built with Magnus. Protobuf (de)serialization and business
logic remain in Ruby, giving you Rails-grade handlers, routing,
interceptors, and the Rails executor around every RPC.

## 官网

- 主页: https://github.com/CodingAnarchy/tonic-rails
- 更新日志: https://github.com/CodingAnarchy/tonic-rails/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/CodingAnarchy/tonic-rails/issues
- RubyGems: https://rubygems.org/gems/tonic-rails

## 历史版本号

- 0.8.1 (2026-10-13)
- 0.8.1-x86_64-linux-musl (2026-10-13)
- 0.8.1-x86_64-linux-gnu (2026-10-13)
- 0.8.1-x86_64-darwin (2026-10-13)
- 0.8.1-x64-mingw-ucrt (2026-10-13)
- 0.8.1-arm64-darwin (2026-10-13)
- 0.8.1-aarch64-linux-musl (2026-10-13)
- 0.8.1-aarch64-linux-gnu (2026-10-13)
- 0.8.0 (2026-10-12)
- 0.8.0-x86_64-linux-musl (2026-10-12)
- 0.8.0-x86_64-linux-gnu (2026-10-12)
- 0.8.0-x86_64-darwin (2026-10-12)
- 0.8.0-x64-mingw-ucrt (2026-10-12)
- 0.8.0-arm64-darwin (2026-10-12)
- 0.8.0-aarch64-linux-musl (2026-10-12)
- 0.8.0-aarch64-linux-gnu (2026-10-12)
- 0.7.0 (2026-10-11)
- 0.7.0-x86_64-linux-musl (2026-10-11)
- 0.7.0-x86_64-linux-gnu (2026-10-11)
- 0.7.0-x86_64-darwin (2026-10-11)
- 0.7.0-x64-mingw-ucrt (2026-10-11)
- 0.7.0-arm64-darwin (2026-10-11)
- 0.7.0-aarch64-linux-musl (2026-10-11)
- 0.7.0-aarch64-linux-gnu (2026-10-11)
- 0.6.0 (2026-10-11)
- 0.6.0-x86_64-linux-musl (2026-10-11)
- 0.6.0-x86_64-linux-gnu (2026-10-11)
- 0.6.0-x86_64-darwin (2026-10-11)
- 0.6.0-x64-mingw-ucrt (2026-10-11)
- 0.6.0-arm64-darwin (2026-10-11)
- 0.6.0-aarch64-linux-musl (2026-10-11)
- 0.6.0-aarch64-linux-gnu (2026-10-11)
- 0.5.0 (2026-10-11)
- 0.5.0-x86_64-linux-musl (2026-10-11)
- 0.5.0-x86_64-linux-gnu (2026-10-11)
- 0.5.0-x86_64-darwin (2026-10-11)
- 0.5.0-x64-mingw-ucrt (2026-10-11)
- 0.5.0-arm64-darwin (2026-10-11)
- 0.5.0-aarch64-linux-musl (2026-10-11)
- 0.5.0-aarch64-linux-gnu (2026-10-11)
- 0.4.0 (2026-10-11)
- 0.4.0-x86_64-linux-musl (2026-10-11)
- 0.4.0-x86_64-linux-gnu (2026-10-11)
- 0.4.0-x86_64-darwin (2026-10-11)
- 0.4.0-x64-mingw-ucrt (2026-10-11)
- 0.4.0-arm64-darwin (2026-10-11)
- 0.4.0-aarch64-linux-musl (2026-10-11)
- 0.4.0-aarch64-linux-gnu (2026-10-11)
- 0.3.0 (2026-10-11)
- 0.3.0-x86_64-linux-musl (2026-10-11)
- 0.3.0-x86_64-linux-gnu (2026-10-11)
- 0.3.0-x86_64-darwin (2026-10-11)
- 0.3.0-x64-mingw-ucrt (2026-10-11)
- 0.3.0-arm64-darwin (2026-10-11)
- 0.3.0-aarch64-linux-musl (2026-10-11)
- 0.3.0-aarch64-linux-gnu (2026-10-11)
- 0.2.0 (2026-10-11)
- 0.2.0-x86_64-linux-musl (2026-10-11)
- 0.2.0-x86_64-linux-gnu (2026-10-11)
- 0.2.0-x86_64-darwin (2026-10-11)
- 0.2.0-x64-mingw-ucrt (2026-10-11)
- 0.2.0-arm64-darwin (2026-10-11)
- 0.2.0-aarch64-linux-musl (2026-10-11)
- 0.2.0-aarch64-linux-gnu (2026-10-11)
- 0.1.0 (2026-10-11)
- 0.1.0-x86_64-linux-musl (2026-10-11)
- 0.1.0-x86_64-linux-gnu (2026-10-11)
- 0.1.0-x86_64-darwin (2026-10-11)
- 0.1.0-arm64-darwin (2026-10-11)
- 0.1.0-aarch64-linux-musl (2026-10-11)
- 0.1.0-aarch64-linux-gnu (2026-10-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/tonic-rails
- gem 安装: `gem install tonic-rails`
- Bundler: `gem "tonic-rails"`
- 最新版本: 0.8.1
- 最新版归档: https://rubygems.org/downloads/tonic-rails-0.8.1.gem
- 版本锁定: `gem "tonic-rails", "~> 0.8.1"`
- 中央仓库: https://rubygems.org/
