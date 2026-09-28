# patient_http

**Tag**: web, networking

## 简介

This gem provides a dedicated async HTTP processor that uses Ruby's Fiber scheduler for non-blocking I/O. Application threads hand off HTTP requests to the processor and return immediately. The processor handles hundreds of concurrent HTTP connections using fibers, then notifies the application when responses arrive via a pluggable callback mechanism. This design keeps application threads free to do other work while HTTP requests are in flight.

## 官网

- 主页: https://github.com/bdurand/patient_http
- 更新日志: https://github.com/bdurand/patient_http/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/patient_http

## 历史版本号

- 1.7.0 (2026-09-24)
- 1.6.1 (2026-09-16)
- 1.6.0 (2026-09-03)
- 1.5.0 (2026-08-27)
- 1.4.0 (2026-08-08)
- 1.3.0 (2026-07-11)
- 1.2.0 (2026-07-09)
- 1.1.2 (2026-06-15)
- 1.1.1 (2026-06-11)
- 1.1.0 (2026-06-08)
- 1.0.0 (2026-05-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/patient_http
- gem 安装: `gem install patient_http`
- Bundler: `gem "patient_http"`
- 最新版本: 1.7.0
- 最新版归档: https://rubygems.org/downloads/patient_http-1.7.0.gem
- 版本锁定: `gem "patient_http", "~> 1.7.0"`
- 中央仓库: https://rubygems.org/
