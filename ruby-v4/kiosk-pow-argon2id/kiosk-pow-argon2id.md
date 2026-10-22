# kiosk-pow-argon2id

**Tag**: web, testing, filesystem

## 简介

kiosk-pow-argon2id is the legacy proof-of-work backend for the Kiosk
framework: an Argon2id search-form proof of work. The shipped default is
Equihash (kiosk-pow-equihash). Argon2id stays a legacy backend because its
64 MiB verify is too expensive for a gateway.

Ships the operator-side Ruby verify (one Argon2id evaluation, no loop) and
a Python solver (solve.py, argon2-cffi). The Ruby verify and the Python
solver produce byte-identical Argon2id digests. The gem's `:parity` spec
examples check this, and so does the `rake parity` task. Neither the
Rakefile nor spec/ is in the package.

Built on kiosk-pow. kiosk-reputation reaches it when a host registers it
under "argon2id"; it does not register itself. Does not depend on
kiosk-core or Rails: pure Ruby and libargon2 through FFI.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-pow-argon2id/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-pow-argon2id

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-pow-argon2id
- gem 安装: `gem install kiosk-pow-argon2id`
- Bundler: `gem "kiosk-pow-argon2id"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-pow-argon2id-0.6.1.gem
- 版本锁定: `gem "kiosk-pow-argon2id", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
