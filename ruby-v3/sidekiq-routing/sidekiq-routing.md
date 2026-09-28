# sidekiq-routing

**Tag**: web, database, devops, filesystem

## 简介

sidekiq-routing gives you runtime control over which Sidekiq queue a
job class lands in or runs from — without a deploy. Park a misbehaving class
onto a worker-less parking queue (reversible), blackhole it (drop), or let
the optional auto-rerouter move noisy classes between latency tiers. Ships a
read-only Sidekiq Web tab. Routing state lives in a single Redis hash read
from a process-local snapshot, so the per-job hot path stays an in-memory
lookup rather than a Redis round-trip.

## 官网

- 主页: https://github.com/neetozone/sidekiq-routing
- RubyGems: https://rubygems.org/gems/sidekiq-routing

## 历史版本号

- 0.1.2 (2026-07-17)
- 0.1.0 (2026-06-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq-routing
- gem 安装: `gem install sidekiq-routing`
- Bundler: `gem "sidekiq-routing"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/sidekiq-routing-0.1.2.gem
- 版本锁定: `gem "sidekiq-routing", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
