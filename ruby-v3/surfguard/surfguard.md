# surfguard

**Tag**: networking

## 简介

Surfguard resolves a hostname to the public IP addresses it points at and refuses anything that would reach an internal network: private, loopback, link-local and carrier-grade NAT space, plus the IPv6 transition ranges a naive guard misses (IPv4-mapped, SIIT, NAT64, 6to4, Teredo). It resolves and classifies only; the caller owns the fetch and pins the connection to a returned address so DNS rebinding cannot swap in a blocked one. Standard library only, no runtime dependencies.

## 官网

- 主页: https://github.com/basecamp/surfguard
- 更新日志: https://github.com/basecamp/surfguard/releases
- 问题追踪: https://github.com/basecamp/surfguard/issues
- RubyGems: https://rubygems.org/gems/surfguard

## 历史版本号

- 0.2.0 (2026-08-31)
- 0.1.3 (2026-08-13)
- 0.1.2 (2026-08-12)
- 0.1.1 (2026-08-12)
- 0.1.0 (2026-08-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/surfguard
- gem 安装: `gem install surfguard`
- Bundler: `gem "surfguard"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/surfguard-0.2.0.gem
- 版本锁定: `gem "surfguard", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
