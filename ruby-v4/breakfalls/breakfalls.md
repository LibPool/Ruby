# breakfalls

**Tag**: library

## 简介

Breakfalls provides a small Railtie that wraps selected controllers with an around_action. When a StandardError is raised, it invokes your registered handlers (global and per-controller) with (exception, request, user, params), then re-raises so existing error handling continues.

## 官网

- 主页: https://github.com/atolix/breakfalls
- 更新日志: https://github.com/atolix/breakfalls/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/atolix/breakfalls/issues
- RubyGems: https://rubygems.org/gems/breakfalls

## 历史版本号

- 0.0.2.alpha (2025-09-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/breakfalls
- gem 安装: `gem install breakfalls`
- Bundler: `gem "breakfalls"`
- 最新版本: 0.0.2.alpha
- 最新版归档: https://rubygems.org/downloads/breakfalls-0.0.2.alpha.gem
- 版本锁定: `gem "breakfalls", "~> 0.0.2.alpha"`
- 中央仓库: https://rubygems.org/
