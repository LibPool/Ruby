# stampeded

**Tag**: web, database

## 简介

Rails integration for Stampeded: an ActiveJob adapter, a worker that executes
jobs, and a launcher for the precompiled daemon.

Enqueueing is a plain INSERT in your own transaction, so a rolled-back
transaction takes its jobs with it. Claiming goes through SQL functions
shared with the Rust worker, so there is no second implementation of the
attempt accounting or the ownership rules.

## 官网

- 主页: https://github.com/seuros/stampeded
- RubyGems: https://rubygems.org/gems/stampeded

## 历史版本号

- 0.3.2 (2026-10-19)
- 0.3.2-x86_64-linux-musl (2026-10-19)
- 0.3.2-x86_64-linux-gnu (2026-10-19)
- 0.3.2-x86_64-darwin (2026-10-19)
- 0.3.2-arm64-darwin (2026-10-19)
- 0.3.2-amd64-freebsd-15 (2026-10-19)
- 0.3.2-aarch64-linux-musl (2026-10-19)
- 0.3.2-aarch64-linux-gnu (2026-10-19)
- 0.3.1 (2026-10-19)
- 0.3.1-x86_64-linux-musl (2026-10-19)
- 0.3.1-x86_64-linux-gnu (2026-10-19)
- 0.3.1-x86_64-darwin (2026-10-19)
- 0.3.1-arm64-darwin (2026-10-19)
- 0.3.1-amd64-freebsd-15 (2026-10-19)
- 0.3.1-aarch64-linux-musl (2026-10-19)
- 0.3.1-aarch64-linux-gnu (2026-10-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/stampeded
- gem 安装: `gem install stampeded`
- Bundler: `gem "stampeded"`
- 最新版本: 0.3.2
- 最新版归档: https://rubygems.org/downloads/stampeded-0.3.2.gem
- 版本锁定: `gem "stampeded", "~> 0.3.2"`
- 中央仓库: https://rubygems.org/
