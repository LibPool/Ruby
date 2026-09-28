# solid_queue-listen_notify

**Tag**: database, data

## 简介

A database trigger notifies Solid Queue workers the moment a job becomes ready, so jobs start in milliseconds even with polling intervals raised to seconds or minutes — which cuts the idle query load that polling generates by orders of magnitude. No monkey patches: the gem wires itself in through Solid Queue's documented lifecycle hooks. Polling remains the correctness backstop, and every failure mode — missing trigger, non-Postgres adapter, PgBouncer, a dropped connection, a fork — degrades loudly to stock Solid Queue behavior.

## 官网

- 主页: https://github.com/cmer/solid_queue-listen_notify
- 文档: https://github.com/cmer/solid_queue-listen_notify/blob/main/README.md
- 更新日志: https://github.com/cmer/solid_queue-listen_notify/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/cmer/solid_queue-listen_notify/issues
- RubyGems: https://rubygems.org/gems/solid_queue-listen_notify

## 历史版本号

- 0.5.2 (2026-07-28)
- 0.5.1 (2026-07-28)
- 0.5.0 (2026-07-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/solid_queue-listen_notify
- gem 安装: `gem install solid_queue-listen_notify`
- Bundler: `gem "solid_queue-listen_notify"`
- 最新版本: 0.5.2
- 最新版归档: https://rubygems.org/downloads/solid_queue-listen_notify-0.5.2.gem
- 版本锁定: `gem "solid_queue-listen_notify", "~> 0.5.2"`
- 中央仓库: https://rubygems.org/
