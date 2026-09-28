# rubocop-constable

**Tag**: web, testing, networking, tooling, filesystem

## 简介

The companion RuboCop extension for Constable, the opinionated Rails testing gem.

Constable's second principle is that nondeterminism is caught by the linter, not
discovered in CI. These seven cops are that linter: bare `sleep`, unfrozen
`Time.now`, unstubbed HTTP, class-level shared state, assertions hidden behind a
branch, retry and eventually helpers, and an `unsafe` block that never says why.

Every cop is scoped to native `Constable::Case` files. Cold cases -- untouched
RSpec or Minitest files running through `Constable::ColdCase::*` -- are exempt by
design, because the whole point of the adoption story is that taking the on-ramp
costs nothing.

Install it alongside `constable-rails` and add `require: rubocop-constable` to
`.rubocop.yml`.

## 官网

- 主页: https://github.com/Ray-Hughes/constable
- 源码仓库: https://github.com/Ray-Hughes/constable/tree/main/rubocop-constable
- 文档: https://github.com/Ray-Hughes/constable/blob/main/rubocop-constable/README.md
- 更新日志: https://github.com/Ray-Hughes/constable/blob/main/rubocop-constable/CHANGELOG.md
- 问题追踪: https://github.com/Ray-Hughes/constable/issues
- RubyGems: https://rubygems.org/gems/rubocop-constable

## 历史版本号

- 2.0.0 (2026-09-09)
- 1.4.2 (2026-09-09)
- 1.4.1 (2026-09-09)
- 1.4.0 (2026-09-09)
- 1.3.3 (2026-09-08)
- 1.3.2 (2026-09-08)
- 1.3.1 (2026-09-08)
- 1.3.0 (2026-09-08)
- 1.2.0 (2026-09-08)
- 1.1.0 (2026-09-08)
- 1.0.0 (2026-09-08)
- 0.1.0 (2026-09-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/rubocop-constable
- gem 安装: `gem install rubocop-constable`
- Bundler: `gem "rubocop-constable"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/rubocop-constable-2.0.0.gem
- 版本锁定: `gem "rubocop-constable", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
