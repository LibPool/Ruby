# devbench

**Tag**: web, template

## 简介

Reports unhandled exceptions, Rails.error reports, failed ActiveJob and
Sidekiq jobs, and failures the application handled, with who was
affected, to Dev Bench. Fingerprints and counts in-process and sends one
small request a minute; detail is uploaded only when Dev Bench asks for
it, scrubbed first. Keeps recent server log lines per user action for
triage, renders the browser sensor's tag, and hooks itself into Rails:
bundle add devbench, bin/rails generate devbench, set DEVBENCH_DSN.

Adds no dependencies beyond the standard library, never alters a response
body, and never raises: a diagnostics gem that can fail a request is worse
than no diagnostics.

## 官网

- 主页: https://github.com/pasperry/devbench-sdk
- RubyGems: https://rubygems.org/gems/devbench

## 历史版本号

- 0.8.1 (2026-10-15)
- 0.8.0 (2026-10-13)
- 0.7.0 (2026-10-10)
- 0.6.0 (2026-10-05)
- 0.5.0 (2026-10-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/devbench
- gem 安装: `gem install devbench`
- Bundler: `gem "devbench"`
- 最新版本: 0.8.1
- 最新版归档: https://rubygems.org/downloads/devbench-0.8.1.gem
- 版本锁定: `gem "devbench", "~> 0.8.1"`
- 中央仓库: https://rubygems.org/
