# kiosk-reputation

**Tag**: web

## 简介

kiosk-reputation decides *when* and *how hard* to challenge a request with a
proof-of-work, issues and verifies the signed wire challenge, and provides a
pluggable reputation policy interface.

Pure Ruby — no dependency on any PoW gem or kiosk-core. A PoW backend is
registered via Kiosk::Reputation::Backends.register: kiosk-pow-equihash
registers itself as "equihash" (the shipped default) in a Rails app; the host
registers kiosk-pow-argon2id as the legacy "argon2id" and kiosk-pow-cuckoo as
the opt-in "cuckatoo".

Anti-DoS invariant: Challenge.verify performs cheap HMAC-sig + expiry checks
BEFORE the one expensive backend eval, so floods of forged/expired proofs are
rejected without running a proof check.

Ships one policy, Policies::RecentSpend: it asks one proof of a session,
by a chance that the customer's recent spend lowers.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-reputation/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-reputation

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-reputation
- gem 安装: `gem install kiosk-reputation`
- Bundler: `gem "kiosk-reputation"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-reputation-0.6.1.gem
- 版本锁定: `gem "kiosk-reputation", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
