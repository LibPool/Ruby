# kiosk-all

**Tag**: web, testing, security, serialization, networking, tooling, filesystem, data

## 简介

kiosk-all is the «I just want to start» entry point for the Kiosk
framework. Installing it pulls in the production data-plane gems:
kiosk-core (value types, abstract bases, configuration) and
kiosk-server — the whole host-side surface: the wire controllers
(one endpoint per verb — GET /kiosk/<query-name>, POST
/kiosk/<action-name> — plus /kiosk/{schema,openapi.json,pay}), the
register/login auth plane, JWKS,
KYC attestation, discovery, the account-binding ceremony, the
Executor, the PoW gate, the headers middleware and the `kiosk:install`
generator.

Deliberately out of scope:
  - kiosk-rls — opt-in DB-level RLS defense-in-depth; add it
    explicitly if you use enable_rls_on in migrations.
  - Test harnesses (kiosk-test-support, kiosk-rls-rspec,
    kiosk-rls-minitest) — host picks one per stack and adds it to
    the dev/test group of its Gemfile.
  - Adapter gems (kiosk-user-idp-*, kiosk-pay-*) —
    providers pick per market/stack.

See https://kiosk.tech.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-all/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-all

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-all
- gem 安装: `gem install kiosk-all`
- Bundler: `gem "kiosk-all"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-all-0.6.1.gem
- 版本锁定: `gem "kiosk-all", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
