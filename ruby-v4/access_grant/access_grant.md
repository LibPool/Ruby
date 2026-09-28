# access_grant

**Tag**: web, database, devops, data

## 简介

AccessGrant gives Rails apps a role-based access control system where permissions
live in the database and can be reassigned to roles by tenant admins at runtime,
with no deploy required. Unlike Pundit/CanCanCan/Action Policy (which hardcode
permission logic in Ruby policy/ability classes) or Rolify (which manages role
assignment but has no concept of permissions), AccessGrant ships a code-defined
permission catalog synced into the database, dynamic per-tenant roles, and a
permitted?(key) check.

## 官网

- 主页: https://github.com/SahSantoshh/access_grant
- 更新日志: https://github.com/SahSantoshh/access_grant/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/access_grant

## 历史版本号

- 1.0.0 (2026-09-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/access_grant
- gem 安装: `gem install access_grant`
- Bundler: `gem "access_grant"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/access_grant-1.0.0.gem
- 版本锁定: `gem "access_grant", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
