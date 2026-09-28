# scope_hunter

**Tag**: library

## 简介

Scope Hunter is a RuboCop extension that detects ActiveRecord query chains that duplicate existing named scopes and suggests using those scopes instead. It indexes model scopes, canonicalizes relation chains, and flags matches with an autocorrect that replaces the initial query with Model.scope while preserving any trailing methods. This keeps query logic DRY, improves readability, and helps teams discover and reuse well-named scopes.

## 官网

- 主页: https://github.com/Ajithxolo/scope_hunter
- 更新日志: https://github.com/Ajithxolo/scope_hunter/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/scope_hunter

## 历史版本号

- 0.1.4 (2026-03-27)
- 0.1.3 (2025-11-29)
- 0.1.2 (2025-10-27)
- 0.1.1 (2025-10-27)
- 0.1.0 (2025-10-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/scope_hunter
- gem 安装: `gem install scope_hunter`
- Bundler: `gem "scope_hunter"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/scope_hunter-0.1.4.gem
- 版本锁定: `gem "scope_hunter", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
