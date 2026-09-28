# lazy_chain

**Tag**: web, template, filesystem

## 简介

Most slow Rails pages are not slow -- a handful of method calls on them are. LazyChain lets you
mark those calls in your templates and moves them off the critical path. The page renders right
away, and each deferred value loads on its own in a Turbo Frame as soon as it is ready. Values
below the fold are never computed at all unless the user scrolls to them. No background job
infrastructure, no cache to invalidate by hand, and no JavaScript to write -- just standard
Turbo Frames and standard Rails caching.

## 官网

- 主页: https://github.com/OutlawAndy/lazy_chain
- 更新日志: https://github.com/OutlawAndy/lazy_chain/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/OutlawAndy/lazy_chain/issues
- RubyGems: https://rubygems.org/gems/lazy_chain

## 历史版本号

- 0.0.1 (2026-09-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/lazy_chain
- gem 安装: `gem install lazy_chain`
- Bundler: `gem "lazy_chain"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/lazy_chain-0.0.1.gem
- 版本锁定: `gem "lazy_chain", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
