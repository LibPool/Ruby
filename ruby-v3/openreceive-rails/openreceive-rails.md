# openreceive-rails

**Tag**: web, database, security, networking, tooling, devops, data

## 简介

Add Bitcoin Lightning checkout to your Rails app and receive payments directly
into a wallet you control. Mount the engine, connect a receive-only Nostr Wallet
Connect (NWC) wallet, and wire up three hooks for authorization, order amounts,
and fulfillment.

Optional swaps let customers pay with USDT, USDC, SOL, and ETH through a
configured provider; you receive BTC over Lightning in your wallet. Available
assets and networks depend on the provider.

OpenReceive handles invoices, payment attempts, and settlement reconciliation
using your existing application database. Keep your orders,
users, prices, and fulfillment in your app, with no separate OpenReceive database,
Redis, or payment service to deploy. Includes an install generator, PostgreSQL,
SQLite, and MySQL support, plus an optional wallet-notifications worker.

## 官网

- 主页: https://openreceive.org
- 源码仓库: https://github.com/openreceive/openreceive
- 文档: https://github.com/openreceive/openreceive/blob/master/docs/guides/quickstart-rails.md
- 更新日志: https://github.com/openreceive/openreceive/blob/master/packages/ruby/openreceive-rails/CHANGELOG.md
- 问题追踪: https://github.com/openreceive/openreceive/issues
- RubyGems: https://rubygems.org/gems/openreceive-rails

## 历史版本号

- 0.4.11 (2026-09-21)
- 0.4.10 (2026-09-16)
- 0.4.9 (2026-09-14)
- 0.4.8 (2026-09-14)
- 0.4.6 (2026-09-11)
- 0.4.5 (2026-09-07)
- 0.4.4 (2026-09-07)
- 0.4.3 (2026-09-03)
- 0.4.2 (2026-09-03)
- 0.4.1 (2026-09-02)
- 0.4.0 (2026-09-02)
- 0.3.3 (2026-09-02)
- 0.3.2 (2026-08-29)
- 0.3.1 (2026-08-28)
- 0.3.0 (2026-08-26)
- 0.2.3 (2026-08-25)
- 0.2.2 (2026-08-25)
- 0.2.1 (2026-08-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/openreceive-rails
- gem 安装: `gem install openreceive-rails`
- Bundler: `gem "openreceive-rails"`
- 最新版本: 0.4.11
- 最新版归档: https://rubygems.org/downloads/openreceive-rails-0.4.11.gem
- 版本锁定: `gem "openreceive-rails", "~> 0.4.11"`
- 中央仓库: https://rubygems.org/
