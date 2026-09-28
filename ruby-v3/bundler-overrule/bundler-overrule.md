# bundler-overrule

**Tag**: testing, filesystem

## 简介

bundler-overrule is a Bundler plugin that gives application developers the final
say over their dependency graph. It adds `force` and `ban` to the Gemfile DSL:
`force` rewrites every version constraint on a gem, from other gems' gemspecs and
from your own Gemfile; `ban` removes a gem from resolution entirely. This is the
Ruby equivalent of Cargo's [patch], npm's overrides, and yarn's resolutions.

## 官网

- 主页: https://github.com/TheSoloHacker47/bundler-overrule
- 文档: https://github.com/TheSoloHacker47/bundler-overrule#readme
- 更新日志: https://github.com/TheSoloHacker47/bundler-overrule/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/TheSoloHacker47/bundler-overrule/issues
- RubyGems: https://rubygems.org/gems/bundler-overrule

## 历史版本号

- 0.3.0 (2026-08-16)
- 0.2.0 (2026-08-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/bundler-overrule
- gem 安装: `gem install bundler-overrule`
- Bundler: `gem "bundler-overrule"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/bundler-overrule-0.3.0.gem
- 版本锁定: `gem "bundler-overrule", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
