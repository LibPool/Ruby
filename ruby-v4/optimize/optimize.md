# optimize

**Tag**: testing, tooling, filesystem

## 简介

Optimize is an ahead-of-time YARV bytecode optimizer for CRuby. It decodes
iseq binaries into an in-memory IR, runs a configurable pipeline of passes
(constant folding, inlining, dead-stash elimination, arithmetic
reassociation, and others) under a narrow contract that the program's hot
path respects, and re-emits an optimized iseq. Intended as a demo and an
experiment, not a production compiler.

## 官网

- 主页: https://github.com/segiddins/optimize-rb
- 更新日志: https://github.com/segiddins/optimize-rb/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/optimize

## 历史版本号

- 0.0.0 (2026-04-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/optimize
- gem 安装: `gem install optimize`
- Bundler: `gem "optimize"`
- 最新版本: 0.0.0
- 最新版归档: https://rubygems.org/downloads/optimize-0.0.0.gem
- 版本锁定: `gem "optimize", "~> 0.0.0"`
- 中央仓库: https://rubygems.org/
