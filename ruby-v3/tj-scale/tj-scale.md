# tj-scale

**Tag**: web, serialization

## 简介

TJ Scale is a lightweight metrics agent that lets a TJ Scale dashboard autoscale
your Heroku dynos based on real queue pressure instead of CPU or memory.

Add the gem, set a few environment variables, and a background reporter starts on
exactly one dyno (web.1 or worker.1 — your choice). Every few seconds it POSTs a
small JSON payload to your dashboard, which applies the scaling rules, limits, and
cooldowns you configure there and calls the Heroku Platform API. The gem itself
never scales anything, keeping your app free of Heroku credentials.

Worker mode reports the number of waiting jobs and the age of the oldest one, from
either Delayed Job or Sidekiq (auto-detected). Web mode reports router queue time
(via Rack middleware and the X-Request-Start header), request volume, and average
response time.

Zero-config inside Rails: no initializer needed, everything is driven by
environment variables. Requires Rails 6.1+ and Ruby 3.0+. For worker metrics,
bring your own queue gem (delayed_job_active_record or sidekiq).

## 官网

- 主页: https://github.com/Untechnickle/tj-scale-gem
- 文档: https://github.com/Untechnickle/tj-scale-gem#readme
- 更新日志: https://github.com/Untechnickle/tj-scale-gem/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/Untechnickle/tj-scale-gem/issues
- RubyGems: https://rubygems.org/gems/tj-scale

## 历史版本号

- 1.1.1 (2026-07-20)
- 1.1.0 (2026-06-12)
- 1.0.2 (2026-06-12)
- 1.0.1 (2026-06-12)
- 1.0.0 (2026-06-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/tj-scale
- gem 安装: `gem install tj-scale`
- Bundler: `gem "tj-scale"`
- 最新版本: 1.1.1
- 最新版归档: https://rubygems.org/downloads/tj-scale-1.1.1.gem
- 版本锁定: `gem "tj-scale", "~> 1.1.1"`
- 中央仓库: https://rubygems.org/
