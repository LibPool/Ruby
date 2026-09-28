# sas-linter

**Tag**: cli, serialization, tooling, filesystem

## 简介

A configurable lint engine for SAS source files. Walks the token
stream produced by the `sas-lexer` gem and applies a set of pluggable
rules covering structural defects (malformed `if` conditions,
identical `then`/`else` branches, unreachable inner branches),
cosmetic issues (trailing whitespace, tab expansion, line endings,
encoding gremlins), and source-header conventions. Includes a
`bin/sas_lint` CLI and YAML-based config.

## 官网

- 主页: https://github.com/mes-amis/sas-linter
- RubyGems: https://rubygems.org/gems/sas-linter

## 历史版本号

- 0.2.6 (2026-05-08)
- 0.2.5 (2026-05-07)
- 0.2.4 (2026-05-07)
- 0.2.3 (2026-05-07)
- 0.2.2 (2026-05-06)
- 0.2.1 (2026-05-06)
- 0.2.0 (2026-05-05)
- 0.1.0 (2026-05-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/sas-linter
- gem 安装: `gem install sas-linter`
- Bundler: `gem "sas-linter"`
- 最新版本: 0.2.6
- 最新版归档: https://rubygems.org/downloads/sas-linter-0.2.6.gem
- 版本锁定: `gem "sas-linter", "~> 0.2.6"`
- 中央仓库: https://rubygems.org/
