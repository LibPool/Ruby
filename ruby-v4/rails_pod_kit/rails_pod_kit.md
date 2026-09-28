# rails_pod_kit

**Tag**: web, devops

## 简介

Packages the yabeda ecosystem and health-monitor-rails into a single,
opinionated kit for running Rails applications on Kubernetes: Puma, Sidekiq
and SolidQueue runtime metrics in Prometheus text format on an in-process
/metrics endpoint (default port 9394), plus a /healthz endpoint wired for
liveness/readiness/startup probes. No sidecar, no separate collector. It
also hosts the schedulers that let a job executor scale to zero without
stranding its recurring jobs: a supervised SolidQueue scheduler thread, and
a supervised sidekiq-cron poller for Sidekiq.

## 官网

- 主页: https://github.com/fabn/rails_pod_kit
- 更新日志: https://github.com/fabn/rails_pod_kit/releases
- RubyGems: https://rubygems.org/gems/rails_pod_kit

## 历史版本号

- 0.3.2 (2026-09-14)
- 0.3.1 (2026-08-11)
- 0.3.0 (2026-07-30)
- 0.2.0 (2026-07-30)
- 0.1.1 (2026-07-26)
- 0.0.3 (2026-07-23)
- 0.0.2 (2026-07-23)
- 0.0.1 (2026-07-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails_pod_kit
- gem 安装: `gem install rails_pod_kit`
- Bundler: `gem "rails_pod_kit"`
- 最新版本: 0.3.2
- 最新版归档: https://rubygems.org/downloads/rails_pod_kit-0.3.2.gem
- 版本锁定: `gem "rails_pod_kit", "~> 0.3.2"`
- 中央仓库: https://rubygems.org/
