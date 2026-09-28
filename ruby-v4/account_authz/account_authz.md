# account_authz

**Tag**: security, data

## 简介

AccountAuthz is the authorization layer for multi-tenant apps. The app declares a fixed catalog of capabilities (permission + metric keys) in code; accounts manage roles as data that bundle those capabilities; AccountAuthz resolves what a member may do (can?) and which metrics they may see (approved_metrics) from their roles, and plugs into Pundit for enforcement.

## 官网

- 主页: https://github.com/DYB-Development/account_authz
- 更新日志: https://github.com/DYB-Development/account_authz/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/DYB-Development/account_authz/issues
- RubyGems: https://rubygems.org/gems/account_authz

## 历史版本号

- 0.1.1 (2026-09-22)
- 0.1.0 (2026-09-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/account_authz
- gem 安装: `gem install account_authz`
- Bundler: `gem "account_authz"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/account_authz-0.1.1.gem
- 版本锁定: `gem "account_authz", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
