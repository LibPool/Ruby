# deprecate_soft

**Tag**: web, database, testing, data

## 简介

DeprecateSoft is a lightweight Ruby gem that lets you gracefully deprecate methods
in your codebase without breaking functionality. It wraps existing instance or
class methods and lets you plug in custom before/after hooks for tracking usage
via logging, Redis, DataDog, or any other observability tools.

Once you verify in your tracking that a method is no longer called,
you can remove it safely from your code base.

This is especially useful in large codebases where you want to safely remove
legacy methods, but first need insight into whether and where they're still
being called.

Hooks are configured once globally and apply project-wide. Fully compatible
with Rails or plain Ruby applications.

## 官网

- 主页: https://github.com/tilo/deprecate_soft
- 更新日志: https://github.com/tilo/deprecate_soft/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/deprecate_soft

## 历史版本号

- 1.2.0 (2025-04-06)
- 1.1.0 (2025-03-29)
- 1.0.0 (2025-03-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/deprecate_soft
- gem 安装: `gem install deprecate_soft`
- Bundler: `gem "deprecate_soft"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/deprecate_soft-1.2.0.gem
- 版本锁定: `gem "deprecate_soft", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
