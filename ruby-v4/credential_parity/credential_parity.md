# credential_parity

**Tag**: web, testing, security, filesystem

## 简介

Compares the leaf key paths declared by each of your Rails encrypted credential files and fails when they disagree. Paths only, never values, so rotating a secret is not drift and no secret reaches an error message. Hooked where Rails already checks for pending migrations: a development middleware, the test suite boot, and a rake task.

## 官网

- 主页: https://github.com/velocity-labs/credential_parity
- 更新日志: https://github.com/velocity-labs/credential_parity/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/credential_parity

## 历史版本号

- 0.1.0 (2026-09-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/credential_parity
- gem 安装: `gem install credential_parity`
- Bundler: `gem "credential_parity"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/credential_parity-0.1.0.gem
- 版本锁定: `gem "credential_parity", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
