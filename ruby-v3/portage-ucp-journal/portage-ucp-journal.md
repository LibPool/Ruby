# portage-ucp-journal

**Tag**: cli, security

## 简介

An append-only, consumer-swappable record of every purchase a Dispatcher completes (store origin, source, product, amount in minor units, order id, idempotency key), built on a small Store interface in the rate_limiter/authenticator mold — the shared persistence seam design-log §22 asks for so a future console or scheduler gem doesn't each grow an incompatible one. Zero runtime dependency on portage-ucp itself; wires in via Dispatcher's optional journal: argument.

## 官网

- 主页: https://github.com/tomtom87/Portage/tree/main/portage-ucp-journal
- 更新日志: https://github.com/tomtom87/Portage/blob/main/portage-ucp-journal/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/portage-ucp-journal

## 历史版本号

- 0.1.1 (2026-09-17)
- 0.1.0 (2026-09-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/portage-ucp-journal
- gem 安装: `gem install portage-ucp-journal`
- Bundler: `gem "portage-ucp-journal"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/portage-ucp-journal-0.1.1.gem
- 版本锁定: `gem "portage-ucp-journal", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
