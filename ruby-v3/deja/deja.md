# deja

**Tag**: testing

## 简介

Deja records a non-deterministic call (today: an Anthropic LLM call) the first
time a test makes it and replays the recorded response on every run after that,
so tests that exercise real model behavior stay fast, offline, and deterministic.
Ships RSpec helpers (use_llm_cache, expect_llm_called, forbid_calls) and a
meet_requirements matcher that judges free-text requirements with the model and
caches the verdict.

## 官网

- 主页: https://github.com/nbrustein/deja
- 更新日志: https://github.com/nbrustein/deja/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/deja

## 历史版本号

- 0.1.0 (2026-06-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/deja
- gem 安装: `gem install deja`
- Bundler: `gem "deja"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/deja-0.1.0.gem
- 版本锁定: `gem "deja", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
