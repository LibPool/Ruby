# rubocop-rspec-unused-let

**Tag**: testing

## 简介

rubocop-rspec-unused-let adds the RSpec/UnusedLet cop, which flags `let` (and optionally `let!`) definitions, `subject` definitions and helper methods (`def`) that are never referenced within their scope. It resolves `shared_examples` precisely when it can see the shared block, and stays conservative otherwise to avoid false positives.

## 官网

- 主页: https://github.com/tk0miya/rubocop-rspec-unused-let
- 更新日志: https://github.com/tk0miya/rubocop-rspec-unused-let/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/rubocop-rspec-unused-let

## 历史版本号

- 1.3.0 (2026-08-23)
- 1.2.0 (2026-08-08)
- 1.1.0 (2026-07-15)
- 1.0.0 (2026-07-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/rubocop-rspec-unused-let
- gem 安装: `gem install rubocop-rspec-unused-let`
- Bundler: `gem "rubocop-rspec-unused-let"`
- 最新版本: 1.3.0
- 最新版归档: https://rubygems.org/downloads/rubocop-rspec-unused-let-1.3.0.gem
- 版本锁定: `gem "rubocop-rspec-unused-let", "~> 1.3.0"`
- 中央仓库: https://rubygems.org/
