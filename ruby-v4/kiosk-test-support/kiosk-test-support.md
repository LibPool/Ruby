# kiosk-test-support

**Tag**: web, testing, security, networking, data

## 简介

kiosk-test-support is the framework-agnostic test surface a Kiosk
provider uses on their OWN application.

It carries two things. The CONFORMANCE CHECKS assert the four
properties the protocol makes normative of an origin: that its routes
resolve, that a verb executes, that a query answers the shape it
declared, and that data access is scoped to the authenticated
principal. They ship with a Minitest adapter and an RSpec adapter, both
loaded by explicit require, so the same fault reads identically in
either framework.

The JOURNEY DSL carries the identity-scoped call helpers
(`as_agent_of`, `as_user`, `as_agent`, `as_anonymous`, `query`,
`run_query`, `run_action`, `pay_action`, `kiosk_seed`), the pluggable
executor contract, a NullExecutor for self-tests, and the structured
error classes (`RLSDenied`, `QuotaExceeded`, `ExecutorNotConfigured`).
It is wired into RSpec by `kiosk-rls-rspec` and into Minitest by
`kiosk-rls-minitest`.

The ASSISTANT drives an origin over HTTP as an assistant does: it
registers, pays proof-of-work tolls, queries, runs, pays with signed
mandates and listens on the event stream. `Kyc` stands in for the
operator's KYC provider, and `StripeMock` fronts a local stripe-mock.

`InProcessExecutor`, `InProcessWire` and `Conformance::InProcessOrigin`
run against kiosk-server, and `Person` signs in through
kiosk-user-idp-devise; both are dependencies. The host's bundle brings
the rest: the Minitest and RSpec adapters use the test framework the
host runs, `LiveServer` serves the app with Puma, and `Wire` solves
Equihash tolls with kiosk-pow-equihash.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-test-support/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-test-support

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-test-support
- gem 安装: `gem install kiosk-test-support`
- Bundler: `gem "kiosk-test-support"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-test-support-0.6.1.gem
- 版本锁定: `gem "kiosk-test-support", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
