# kiosk-rls

**Tag**: web, database, security

## 简介

kiosk-rls provides the row-level-security DSL Kiosk providers use inside
their ActiveRecord migrations: `enable_rls_on`, `policy`, plus the
add/change/remove/rename migration verbs.

The DSL compiles to standard PostgreSQL DDL (ALTER TABLE ENABLE ROW LEVEL
SECURITY, ALTER TABLE FORCE ROW LEVEL SECURITY, GRANT, CREATE POLICY,
COMMENT ON TABLE) and runs inside the migration's transaction via the
host's `#execute` method. FORCE is not optional: without it Postgres
exempts the table owner, and the typical Rails app connects as the owner,
so RLS would be a no-op.

No PostgreSQL runtime dependency — pure SQL generation. The host
provides the connection.

## 官网

- 主页: https://kiosk.tech
- 源码仓库: https://github.com/kiosk-hq/kiosk
- 更新日志: https://github.com/kiosk-hq/kiosk/blob/main/kiosk-rls/CHANGELOG.md
- 问题追踪: https://github.com/kiosk-hq/kiosk/issues
- RubyGems: https://rubygems.org/gems/kiosk-rls

## 历史版本号

- 0.6.1 (2026-10-21)
- 0.5.20 (2026-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/kiosk-rls
- gem 安装: `gem install kiosk-rls`
- Bundler: `gem "kiosk-rls"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/kiosk-rls-0.6.1.gem
- 版本锁定: `gem "kiosk-rls", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
