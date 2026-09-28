# phlex-reactive

**Tag**: web, cli, database, template, data

## 简介

phlex-reactive makes Phlex components reactive without writing Stimulus
controllers or hand-picking Turbo Stream targets. Declare actions in Ruby;
a single generic client runtime turns clicks and form input into a server
round trip that re-renders the component and morphs it back in. Components
self-target by a stable DOM id, so the same unit re-renders for client
actions AND server-pushed broadcasts. State lives in the database behind a
signed identity — no attacker-controlled snapshot. Pairs with pgbus for
reliable, transactional, reconnect-safe live updates with no Action Cable
and no Redis.

## 官网

- 主页: https://github.com/zoolutions/phlex-reactive
- 源码仓库: https://github.com/zoolutions/phlex-reactive/tree/main
- 更新日志: https://github.com/zoolutions/phlex-reactive/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/phlex-reactive

## 历史版本号

- 0.13.2 (2026-09-14)
- 0.13.1 (2026-09-13)
- 0.13.0 (2026-08-30)
- 0.12.6 (2026-08-26)
- 0.12.5 (2026-08-24)
- 0.12.4 (2026-07-16)
- 0.12.3 (2026-07-13)
- 0.12.2 (2026-07-11)
- 0.12.1 (2026-07-10)
- 0.12.0 (2026-07-09)
- 0.11.7 (2026-07-08)
- 0.11.6 (2026-07-08)
- 0.11.5 (2026-07-08)
- 0.11.4 (2026-07-08)
- 0.11.3 (2026-07-08)
- 0.11.2 (2026-07-08)
- 0.11.1 (2026-07-08)
- 0.11.0 (2026-07-07)
- 0.10.0 (2026-07-07)
- 0.9.5 (2026-07-06)
- 0.9.4 (2026-07-05)
- 0.9.3 (2026-07-05)
- 0.9.2 (2026-07-04)
- 0.9.1 (2026-07-04)
- 0.9.0 (2026-07-04)
- 0.4.8 (2026-07-02)
- 0.4.7 (2026-06-30)
- 0.4.6 (2026-06-30)
- 0.4.5 (2026-06-29)
- 0.4.4 (2026-06-28)
- 0.4.3 (2026-06-28)
- 0.4.2 (2026-06-28)
- 0.4.1 (2026-06-28)
- 0.4.0 (2026-06-28)
- 0.3.0 (2026-06-27)
- 0.2.9 (2026-06-27)
- 0.2.8 (2026-06-27)
- 0.2.7 (2026-06-27)
- 0.2.6 (2026-06-25)
- 0.2.5 (2026-06-25)
- 0.2.4 (2026-06-25)
- 0.2.3 (2026-06-24)
- 0.2.2 (2026-06-24)
- 0.2.1 (2026-06-24)
- 0.2.0 (2026-06-24)
- 0.1.0 (2026-06-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/phlex-reactive
- gem 安装: `gem install phlex-reactive`
- Bundler: `gem "phlex-reactive"`
- 最新版本: 0.13.2
- 最新版归档: https://rubygems.org/downloads/phlex-reactive-0.13.2.gem
- 版本锁定: `gem "phlex-reactive", "~> 0.13.2"`
- 中央仓库: https://rubygems.org/
