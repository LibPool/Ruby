# kiosk-rls-minitest

**Tag**: testing

## 简介

kiosk-rls-minitest wires the framework-agnostic Kiosk journey-test DSL
(kiosk-test-support) into Minitest.

`include Kiosk::TestHelpers` inside any `Minitest::Test` subclass mixes
in the journey helpers (`as_agent_of`, `as_user`, `as_agent`,
`as_anonymous`, `query`, `run_query`, `run_action`, `pay_action`,
`kiosk_seed`).

Ships the assertions `assert_rls_denied` and `assert_quota_exceeded`
for asserting the structured error classes — both also exposed as
the Minitest `must_raise_*` / `wont_raise_*` spec-DSL forms.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-rls-minitest/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-rls-minitest

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-rls-minitest
- gem 安装: `gem install kiosk-rls-minitest`
- Bundler: `gem "kiosk-rls-minitest"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-rls-minitest-0.6.1.gem
- 版本锁定: `gem "kiosk-rls-minitest", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
