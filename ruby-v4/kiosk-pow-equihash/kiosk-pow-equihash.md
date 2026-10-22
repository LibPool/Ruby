# kiosk-pow-equihash

**Tag**: web, cli, testing

## 简介

kiosk-pow-equihash is the shipped default proof-of-work backend for the
Kiosk framework: a pure-Ruby Equihash (Biryukov & Khovratovich birthday-
collision PoW) VERIFIER built on kiosk-pow, which holds the pure-Ruby
BLAKE2b-256. The gem depends on neither kiosk-core nor Rails.

`Kiosk::Pow::Equihash.verify(salt:, params:, nonce:)` recomputes the 2^k
BLAKE2b-256 hashes named by the proof's indices, checks that they XOR to
zero over all n bits, and walks the Wagner collision tree (per-level XOR
cancellation plus the Zcash-canonical subtree ordering that pins one
canonical form per solution). Difficulty is set by (n, k) alone — there is
no post-hoc target check.

Default parameters are n=168, k=7, chosen by the benchmark in bench/: the
largest params whose reference solve stays inside a consumer-laptop budget
(p95 ~10 s on one M-series laptop core, the only hardware the seconds have
ever been measured on; the ~1.3 GiB peak is THIS solver's table, not the
host's -- and not a floor (n, k) imposes on every implementation, since a
memory-optimised solver trades it for time) while verify costs 128 BLAKE2b evaluations —
~22 ms and a few KB in pure Ruby without YJIT. That asymmetry is the point: the gem
prices a request, it does not equalise hardware. Equihash is neither ASIC-
nor GPU-proof (it was ASIC'd on Zcash); abuse resistance comes from the
reputation policy's N-proofs knob and caps, not from this algorithm.

Ships the provider-side verifier only. A reference Python + numpy solver
(solve.py) rides along for parity testing and for assistants that need
one; production solving is the client's concern.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-pow-equihash/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-pow-equihash

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-pow-equihash
- gem 安装: `gem install kiosk-pow-equihash`
- Bundler: `gem "kiosk-pow-equihash"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-pow-equihash-0.6.1.gem
- 版本锁定: `gem "kiosk-pow-equihash", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
