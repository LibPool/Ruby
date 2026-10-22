# active_durable

**Tag**: web, database, data

## 简介

ActiveDurable runs multi-step business flows (checkouts, onboarding, payouts) as durable sagas
stored in your own database. Completed steps are checkpointed and never repeated after a crash,
failures before the point of no return are compensated in reverse order, and failures after it
are retried. No Redis and no extra servers: just Active Record and Active Job.

## 官网

- 主页: https://webresstudio.github.io/active_durable/
- 源码仓库: https://github.com/webresstudio/active_durable
- 更新日志: https://github.com/webresstudio/active_durable/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/webresstudio/active_durable/issues
- RubyGems: https://rubygems.org/gems/active_durable

## 历史版本号

- 0.8.0 (2026-10-22)
- 0.7.0 (2026-10-07)
- 0.6.0 (2026-10-07)
- 0.5.0 (2026-10-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/active_durable
- gem 安装: `gem install active_durable`
- Bundler: `gem "active_durable"`
- 最新版本: 0.8.0
- 最新版归档: https://rubygems.org/downloads/active_durable-0.8.0.gem
- 版本锁定: `gem "active_durable", "~> 0.8.0"`
- 中央仓库: https://rubygems.org/
