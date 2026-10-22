# kiosk-pow-cuckoo

**Tag**: web, cli, testing, security

## 简介

kiosk-pow-cuckoo is an optional Cuckatoo-Cycle (Cuckoo Cycle variant)
proof-of-work backend for the Kiosk framework.

Ships the provider-side Ruby VERIFIER only.  The verifier is cheap
(a handful of hash evaluations; no wall-clock figure is benchmarked),
security-critical, and validated against Grin's Cuckatoo29 CI test
vector.  A reference Python solver (solve_cuckoo.py) ships alongside for
parity testing; production solving is the client's concern.

The implementation is clean-room from Tromp's public-domain algorithm
spec (doc/spec, doc/mathspec) — no GPL/FAIR-MINING code is included.
BLAKE2b-256 comes from kiosk-pow, the base of every Kiosk PoW backend.
SipHash-2-4 is pure Ruby from the public-domain SipHash spec with
Cuckatoo's non-standard initialization (keys feed directly into v0..v3
without XOR-ing the 0x736f6d65... magic constants).

Does not depend on kiosk-core or Rails — pure Ruby, no native extensions.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-pow-cuckoo/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-pow-cuckoo

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-pow-cuckoo
- gem 安装: `gem install kiosk-pow-cuckoo`
- Bundler: `gem "kiosk-pow-cuckoo"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-pow-cuckoo-0.6.1.gem
- 版本锁定: `gem "kiosk-pow-cuckoo", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
