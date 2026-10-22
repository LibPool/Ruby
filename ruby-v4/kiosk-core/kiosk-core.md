# kiosk-core

**Tag**: web, database, tooling

## 简介

kiosk-core is the foundation for the Kiosk framework. It defines the value
types (Identity, Mandate), the abstract base classes adapters extend
(AgentIdentityProviders, UserIdentityProviders, PaymentProviders,
KycProviders), the Postgres GUC namespace constants, the protocol-version
surface, the canonical-uuid shape guard (UuidCheck), and the Kiosk.configure
block.

No Rails dependency. Loadable in any Ruby app; the heavier kiosk-server
and kiosk-rls gems build on top of this.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-core/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-core

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-core
- gem 安装: `gem install kiosk-core`
- Bundler: `gem "kiosk-core"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-core-0.6.1.gem
- 版本锁定: `gem "kiosk-core", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
