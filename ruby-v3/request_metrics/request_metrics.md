# request_metrics

**Tag**: web

## 简介

RequestMetrics provides a base class for attaching per-request counters and
timing metrics to Rails controller log lines. Subclass RequestMetrics::Base,
declare metrics with metric_accessor, implement #log and .summary_log, and
the gem wires everything into ActionController via a Railtie automatically.

## 官网

- 主页: https://github.com/nebulab/request_metrics
- 更新日志: https://github.com/nebulab/request_metrics/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/request_metrics

## 历史版本号

- 0.1.0 (2026-05-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/request_metrics
- gem 安装: `gem install request_metrics`
- Bundler: `gem "request_metrics"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/request_metrics-0.1.0.gem
- 版本锁定: `gem "request_metrics", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
