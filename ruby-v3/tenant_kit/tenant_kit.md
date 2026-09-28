# tenant_kit

**Tag**: web, database, data

## 简介

TenantKit makes a Rails app multi-tenant using the row-level / shared-schema strategy: one database, a tenant_id foreign key on owned tables, automatic query scoping via ActiveSupport::CurrentAttributes, auto-assignment of the current tenant, and first-class tenant propagation into ActiveJob background jobs. It is strict by default: querying a tenant-scoped model with no tenant set raises rather than leaking another tenant's data.

## 官网

- 主页: https://github.com/wintan1418/tenant_kit
- 源码仓库: https://github.com/wintan1418/tenant_kit/tree/main
- 更新日志: https://github.com/wintan1418/tenant_kit/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/wintan1418/tenant_kit/issues
- RubyGems: https://rubygems.org/gems/tenant_kit

## 历史版本号

- 0.1.0 (2026-07-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/tenant_kit
- gem 安装: `gem install tenant_kit`
- Bundler: `gem "tenant_kit"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/tenant_kit-0.1.0.gem
- 版本锁定: `gem "tenant_kit", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
