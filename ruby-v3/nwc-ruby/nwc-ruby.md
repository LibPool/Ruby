# nwc-ruby

**Tag**: web, cli, security, networking

## 简介

A production-grade Ruby client for Nostr Wallet Connect (NIP-47). Handles the Nostr
protocol, NIP-04 and NIP-44 v2 encryption, secp256k1 key derivation, Schnorr signing,
and — most importantly — a reliable long-running WebSocket connection to the relay
with heartbeat pings, forced recycle, exponential backoff, and SIGTERM handling.
Developers call `pay_invoice`, `make_invoice`, `lookup_invoice`, etc. and
`subscribe_to_notifications { |n| ... }` — the transport reliability is hidden.

## 官网

- 主页: https://github.com/MegalithicBTC/nwc-ruby
- 源码仓库: https://github.com/MegalithicBTC/nwc-ruby/tree/master
- 更新日志: https://github.com/MegalithicBTC/nwc-ruby/blob/master/CHANGELOG.md
- 问题追踪: https://github.com/MegalithicBTC/nwc-ruby/issues
- RubyGems: https://rubygems.org/gems/nwc-ruby

## 历史版本号

- 0.2.4 (2026-07-17)
- 0.2.3 (2026-04-23)
- 0.2.2 (2026-04-21)
- 0.2.1 (2026-04-20)
- 0.2.0 (2026-04-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/nwc-ruby
- gem 安装: `gem install nwc-ruby`
- Bundler: `gem "nwc-ruby"`
- 最新版本: 0.2.4
- 最新版归档: https://rubygems.org/downloads/nwc-ruby-0.2.4.gem
- 版本锁定: `gem "nwc-ruby", "~> 0.2.4"`
- 中央仓库: https://rubygems.org/
