# kiosk-rls-rspec

**Tag**: testing

## 简介

kiosk-rls-rspec wires the framework-agnostic Kiosk journey-test DSL
(kiosk-test-support) into RSpec.

Automatically mixes the journey helpers (`as_agent_of`, `as_user`,
`as_agent`, `as_anonymous`, `query`, `run_query`, `run_action`,
`pay_action`, `kiosk_seed`) into any example group tagged
`type: :kiosk_journey` (or `type: :kiosk_agent`, the same DSL under a
second tag).

Ships the matchers `be_rls_denied` and `be_quota_exceeded` for asserting
the structured error classes.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-rls-rspec/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-rls-rspec

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-rls-rspec
- gem 安装: `gem install kiosk-rls-rspec`
- Bundler: `gem "kiosk-rls-rspec"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-rls-rspec-0.6.1.gem
- 版本锁定: `gem "kiosk-rls-rspec", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
