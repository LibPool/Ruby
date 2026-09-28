# rails_error_dashboard

**Tag**: web, database, testing, networking, template, filesystem, data

## 简介

== Rails-native failure investigation

Rails Error Dashboard (RED) is an open-source, self-hosted Rails engine for
investigating production exceptions without sending error data to a monitoring
vendor. It groups errors and records request context and cause chains and, when
enabled, breadcrumbs plus local and instance variables captured before Ruby
unwinds the stack.

== What it records

* Rails and Ruby runtime health on the error record, refreshed on every captured
  occurrence: Active Record pool, Puma, background jobs, GC, memory, threads,
  file descriptors and system pressure
* Built-in storm protection that progressively sheds expensive context and I/O
  during error floods while retaining useful exemplars and exact occurrence
  counts
* Copy as RSpec, curl or LLM prompt; swallowed-exception detection; LLM
  observability without prompt capture; OpenTelemetry span export
* Workflow, notifications (Slack, Email, Discord, PagerDuty, webhooks) and
  two-way issue sync with GitHub, GitLab, Codeberg and Linear
* Rails-specific operational views: jobs, database, cache, Action Cable, Active
  Storage, Rack::Attack and deprecations

== Running it

Run RED with your application's database or an isolated error database, on
PostgreSQL, MySQL/Trilogy or SQLite. The dashboard is translated into 11
languages (French native-reviewed; the rest machine-translated and awaiting
native review). A
self-hosted Sentry alternative that keeps error data in your own database. The
gem is MIT and free forever.

Supports Rails 7.0-8.1 and Ruby 3.2-4.0. Beta: APIs may change before 1.0.

Live demo: https://rails-error-dashboard.anjan.dev

Documentation: https://AnjanJ.github.io/rails_error_dashboard

## 官网

- 主页: https://AnjanJ.github.io/rails_error_dashboard
- 源码仓库: https://github.com/AnjanJ/rails_error_dashboard
- 更新日志: https://github.com/AnjanJ/rails_error_dashboard/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/AnjanJ/rails_error_dashboard/issues
- RubyGems: https://rubygems.org/gems/rails_error_dashboard

## 历史版本号

- 0.14.2 (2026-09-27)
- 0.14.1 (2026-09-25)
- 0.14.0 (2026-09-20)
- 0.13.0 (2026-09-18)
- 0.12.1 (2026-09-16)
- 0.12.0 (2026-09-15)
- 0.11.9 (2026-09-14)
- 0.11.8 (2026-09-08)
- 0.11.7 (2026-09-08)
- 0.11.6 (2026-09-08)
- 0.11.5 (2026-09-07)
- 0.11.4 (2026-08-30)
- 0.11.3 (2026-08-29)
- 0.11.2 (2026-08-29)
- 0.11.1 (2026-08-27)
- 0.11.0 (2026-08-26)
- 0.10.0 (2026-08-25)
- 0.9.1 (2026-08-24)
- 0.9.0 (2026-08-24)
- 0.8.4 (2026-08-13)
- 0.8.3 (2026-07-31)
- 0.8.2 (2026-06-22)
- 0.8.1 (2026-06-12)
- 0.8.0 (2026-06-10)
- 0.7.2 (2026-06-01)
- 0.7.1 (2026-05-31)
- 0.7.0 (2026-05-31)
- 0.6.4 (2026-05-04)
- 0.6.3 (2026-05-03)
- 0.6.2 (2026-05-03)
- 0.6.1 (2026-05-01)
- 0.6.0 (2026-04-27)
- 0.5.15 (2026-04-25)
- 0.5.14 (2026-04-20)
- 0.5.13 (2026-04-20)
- 0.5.12 (2026-04-16)
- 0.5.11 (2026-03-28)
- 0.5.10 (2026-03-27)
- 0.5.9 (2026-03-27)
- 0.5.8 (2026-03-27)
- 0.5.7 (2026-03-25)
- 0.5.6 (2026-03-25)
- 0.5.5 (2026-03-25)
- 0.5.4 (2026-03-25)
- 0.5.3 (2026-03-25)
- 0.5.2 (2026-03-24)
- 0.5.1 (2026-03-24)
- 0.5.0 (2026-03-24)
- 0.4.2 (2026-03-24)
- 0.4.1 (2026-03-08)
- 0.4.0 (2026-03-07)
- 0.3.1 (2026-03-05)
- 0.3.0 (2026-03-03)
- 0.2.4 (2026-03-02)
- 0.2.3 (2026-02-28)
- 0.2.2 (2026-02-28)
- 0.2.1 (2026-02-24)
- 0.2.0 (2026-02-23)
- 0.1.38 (2026-02-18)
- 0.1.37 (2026-02-12)
- 0.1.36 (2026-02-10)
- 0.1.35 (2026-02-10)
- 0.1.34 (2026-02-10)
- 0.1.33 (2026-01-23)
- 0.1.32 (2026-01-23)
- 0.1.31 (2026-01-23)
- 0.1.30 (2026-01-23)
- 0.1.29 (2026-01-22)
- 0.1.28 (2026-01-19)
- 0.1.27 (2026-01-12)
- 0.1.26 (2026-01-12)
- 0.1.25 (2026-01-11)
- 0.1.24 (2026-01-11)
- 0.1.23 (2026-01-08)
- 0.1.22 (2026-01-08)
- 0.1.21 (2026-01-04)
- 0.1.20 (2026-01-03)
- 0.1.19 (2026-01-03)
- 0.1.18 (2026-01-02)
- 0.1.17 (2026-01-02)
- 0.1.16 (2026-01-02)
- 0.1.15 (2025-12-31)
- 0.1.14 (2025-12-31)
- 0.1.13 (2025-12-31)
- 0.1.12 (2025-12-31)
- 0.1.11 (2025-12-31)
- 0.1.10 (2025-12-30)
- 0.1.9 (2025-12-30)
- 0.1.8 (2025-12-30)
- 0.1.7 (2025-12-30)
- 0.1.6 (2025-12-29)
- 0.1.5 (2025-12-28)
- 0.1.4 (2025-12-27)
- 0.1.3 (2025-12-26)
- 0.1.1 (2025-12-25)
- 0.1.0 (2025-12-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails_error_dashboard
- gem 安装: `gem install rails_error_dashboard`
- Bundler: `gem "rails_error_dashboard"`
- 最新版本: 0.14.2
- 最新版归档: https://rubygems.org/downloads/rails_error_dashboard-0.14.2.gem
- 版本锁定: `gem "rails_error_dashboard", "~> 0.14.2"`
- 中央仓库: https://rubygems.org/
