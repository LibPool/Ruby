# kicks_liveness

**Tag**: web

## 简介

A liveness probe for RabbitMQ worker pods that loads no Rails and never talks
to the broker. Workers check their Bunny consumers in memory and publish a
heartbeat to tmpfs; the probe only reads that heartbeat.

## 官网

- 主页: https://github.com/PoroshkinaVV/kicks_liveness
- 文档: https://rubydoc.info/gems/kicks_liveness/0.1.2
- 更新日志: https://github.com/PoroshkinaVV/kicks_liveness/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/PoroshkinaVV/kicks_liveness/issues
- RubyGems: https://rubygems.org/gems/kicks_liveness

## 历史版本号

- 0.1.2 (2026-09-11)
- 0.1.1 (2026-09-09)
- 0.1.0 (2026-09-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/kicks_liveness
- gem 安装: `gem install kicks_liveness`
- Bundler: `gem "kicks_liveness"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/kicks_liveness-0.1.2.gem
- 版本锁定: `gem "kicks_liveness", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
