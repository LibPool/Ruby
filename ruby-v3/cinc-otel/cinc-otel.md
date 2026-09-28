# cinc-otel

**Tag**: cli

## 简介

Emits an OpenTelemetry span tree for each Cinc Client run: a chef.run root
span, a child span for each run phase, and one span per resource action.
Implemented as a Chef::EventDispatch handler. Loaded inside a cinc-client
process; OpenTelemetry exporter and endpoint are configured through the
standard OTEL_* environment variables.

## 官网

- 主页: https://github.com/fastly/cinc-otel
- 更新日志: https://github.com/fastly/cinc-otel/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/cinc-otel

## 历史版本号

- 1.0.0 (2026-08-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/cinc-otel
- gem 安装: `gem install cinc-otel`
- Bundler: `gem "cinc-otel"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/cinc-otel-1.0.0.gem
- 版本锁定: `gem "cinc-otel", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
