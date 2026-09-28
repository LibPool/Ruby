# puma-plugin-telemetry_too

**Tag**: web, networking, data

## 简介

NOTE: This is a fork of puma-plugin-telemetry, modified to:

- Support Puma 7
- Add LogTarget, with custom formatter: and transform: options
- Warn about socket telemetry on unsupported platforms

Puma plugin which should be able to handle all your metric needs regarding your webserver:

- ability to publish basic puma statistics (like queue backlog) to both logs and datadog
- ability to add custom target whenever you need it
- ability to monitor puma socket listen queue (!)
- ability to report requests queue time via custom rack middleware - the time request spent between being accepted by Load Balancer and start of its processing by Puma worker

## 官网

- 主页: https://github.com/stevenharman/puma-plugin-telemetry_too
- 更新日志: https://github.com/stevenharman/puma-plugin-telemetry_too/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/puma-plugin-telemetry_too

## 历史版本号

- 0.0.3 (2026-08-14)
- 0.0.2 (2025-12-05)
- 0.0.1.alpha3 (2025-10-21)
- 0.0.1.alpha1 (2025-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/puma-plugin-telemetry_too
- gem 安装: `gem install puma-plugin-telemetry_too`
- Bundler: `gem "puma-plugin-telemetry_too"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/puma-plugin-telemetry_too-0.0.3.gem
- 版本锁定: `gem "puma-plugin-telemetry_too", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
