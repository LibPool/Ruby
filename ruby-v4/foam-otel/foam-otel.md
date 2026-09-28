# foam-otel

**Tag**: testing

## 简介

A thin, safe wrapper over the official OpenTelemetry libraries: foam owns the pipeline (providers, batch processors, OTLP export to the foam fleet endpoint, opt-in key-list redaction — zero redaction by default), turns on automatic tier-1/2 instrumentation, and ships a small set of never-throw helpers. Configure with Foam::Otel.init(name:, environment:, enabled:, token:); the ingest token is passed EXPLICITLY — the fleet convention is to read it from the FOAM_OTEL_TOKEN environment variable and hand it to init. The gem never reads the token (or any config) from the environment itself. Built to docs/BASE_PACKAGE_SPEC.md; full usage in the README (shown on the source page and on rubydoc.info, not on the RubyGems gem page).

## 官网

- 主页: https://github.com/foam-ai/packages
- 源码仓库: https://github.com/foam-ai/packages/tree/main/ruby/foam-otel
- RubyGems: https://rubygems.org/gems/foam-otel

## 历史版本号

- 3.0.0.alpha.6 (2026-09-24)
- 3.0.0.alpha.5 (2026-09-18)
- 3.0.0.alpha.4 (2026-09-17)
- 3.0.0.alpha.3 (2026-09-14)
- 3.0.0.alpha.2 (2026-09-14)
- 3.0.0.alpha.1 (2026-09-08)
- 2.1.1 (2026-07-30)
- 2.1.0 (2026-07-30)
- 2.0.0 (2026-07-30)
- 1.9.1 (2026-07-29)
- 1.9.0 (2026-07-29)
- 1.8.1 (2026-07-29)
- 1.8.0 (2026-07-29)
- 1.7.0 (2026-07-28)
- 1.6.0 (2026-07-28)
- 1.5.0 (2026-07-28)
- 1.4.0 (2026-07-27)
- 1.3.0 (2026-07-27)
- 1.2.1 (2026-07-26)
- 1.2.0 (2026-07-26)
- 1.1.0 (2026-07-25)
- 1.0.2 (2026-07-24)
- 1.0.1 (2026-07-24)
- 1.0.0 (2026-07-24)
- 0.1.5 (2026-07-22)
- 0.1.0 (2026-07-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/foam-otel
- gem 安装: `gem install foam-otel`
- Bundler: `gem "foam-otel"`
- 最新版本: 2.1.1
- 最新版归档: https://rubygems.org/downloads/foam-otel-2.1.1.gem
- 版本锁定: `gem "foam-otel", "~> 2.1.1"`
- 中央仓库: https://rubygems.org/
