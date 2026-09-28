# mini_racer-csim

**Tag**: web, filesystem

## 简介

A private fork of mini_racer (minimal embedded V8 for Ruby) adding browser-level behavior used by capybara-simulated: the V8 ES Module API, per-frame realms, realm reset, cross-process bytecode caching, an opt-in host namespace, and a batched module-graph loader with a URL module registry. These are niche browser-fidelity features; general users should use upstream mini_racer. It loads under its own `mini_racer_csim` require path and `MiniRacerCsim` namespace, so it never collides with upstream mini_racer in the same bundle.

## 官网

- 主页: https://github.com/ursm/mini_racer
- 源码仓库: https://github.com/ursm/mini_racer/tree/main
- 问题追踪: https://github.com/ursm/mini_racer/issues
- RubyGems: https://rubygems.org/gems/mini_racer-csim

## 历史版本号

- 0.21.1.5 (2026-06-08)
- 0.21.1.4 (2026-06-08)
- 0.21.1.3 (2026-06-08)
- 0.21.1.2 (2026-06-06)
- 0.21.1.1 (2026-06-06)
- 0.21.1.0 (2026-06-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/mini_racer-csim
- gem 安装: `gem install mini_racer-csim`
- Bundler: `gem "mini_racer-csim"`
- 最新版本: 0.21.1.5
- 最新版归档: https://rubygems.org/downloads/mini_racer-csim-0.21.1.5.gem
- 版本锁定: `gem "mini_racer-csim", "~> 0.21.1.5"`
- 中央仓库: https://rubygems.org/
