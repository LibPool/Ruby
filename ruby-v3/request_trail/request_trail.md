# request_trail

**Tag**: web, serialization, networking, filesystem

## 简介

Rack middleware that traces every request through all processing layers — controller, ActiveRecord, cache, ActiveJob, and outbound HTTP via Faraday — then emits a flame-graph-style summary to the Rails log. Supports plain-text, ASCII flame-graph, and JSON output; N+1 detection; sampling; path filtering; Sidekiq and ActiveJob adapters; and Rails log tags. Overhead under 1ms per request.

## 官网

- 主页: https://github.com/eclectic-coding/request-trail
- 更新日志: https://github.com/eclectic-coding/request-trail/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/request_trail

## 历史版本号

- 1.0.0 (2026-06-14)
- 0.7.0 (2026-06-14)
- 0.6.0 (2026-06-14)
- 0.5.0 (2026-06-13)
- 0.4.0 (2026-06-12)
- 0.3.0 (2026-06-12)
- 0.2.0 (2026-06-11)
- 0.1.0 (2026-06-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/request_trail
- gem 安装: `gem install request_trail`
- Bundler: `gem "request_trail"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/request_trail-1.0.0.gem
- 版本锁定: `gem "request_trail", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
