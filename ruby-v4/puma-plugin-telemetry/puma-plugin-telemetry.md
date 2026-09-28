# puma-plugin-telemetry

**Tag**: web, networking, data

## 简介

Puma plugin which should be able to handle all your metric needs regarding your webserver:

- ability to publish basic puma statistics (like queue backlog) to both logs and datadog
- ability to add custom target whenever you need it
- ability to monitor puma socket listen queue (!)
- ability to report requests queue time via custom rack middleware - the time request spent between being accepted by Load Balancer and start of its processing by Puma worker

## 官网

- 主页: https://github.com/babbel/puma-plugin-telemetry
- 更新日志: https://github.com/babbel/puma-plugin-telemetry/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/puma-plugin-telemetry

## 历史版本号

- 1.2.0 (2026-08-05)
- 1.1.6 (2026-08-03)
- 1.1.5 (2026-07-31)
- 1.1.4 (2024-05-29)
- 1.1.2 (2022-12-28)
- 1.1.1 (2022-06-22)
- 1.1.0 (2022-06-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/puma-plugin-telemetry
- gem 安装: `gem install puma-plugin-telemetry`
- Bundler: `gem "puma-plugin-telemetry"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/puma-plugin-telemetry-1.2.0.gem
- 版本锁定: `gem "puma-plugin-telemetry", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
