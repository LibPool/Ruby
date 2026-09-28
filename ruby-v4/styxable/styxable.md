# styxable

**Tag**: filesystem, data

## 简介

Styxable turns deletion into a three-stage lifecycle for ActiveRecord models: active,
archived, purged. Calling styx_archive soft-deletes a record — it (optionally) vanishes
from default scopes like being in a trash can or recycle bin, but the row survives, so foreign
keys, joins, reports and audits keep working. Archived records can still be listed,
counted and restored during a configurable grace or retention period, giving you an undo window or
restore window instead of an irreversible destroy.

While a record sits in the archive it is immutable: writes are rejected, so nothing can
be silently edited between archiving and erasure — like in a vault.
styx_unarchive brings a record back, unless it cannot, for example when
a newer record has claimed a unique attribute in the meantime. Archiving cascades along
dependent: associations, so closing an account, deactivating a user or tearing down a
tenant can archive everything it owns in a single call, with callbacks around each step.

Each model declares its own data retention period. A recurring background job then permanently
destroys records whose retention window has expired, expressing your retention schedule,
records disposition and automatic purge in code rather than in a runbook — useful for
GDPR storage limitation and right to erasure ("right to be forgotten") obligations, or
any policy with a TTL or expiry date. A before-purge callback lets you detach
ActiveStorage blobs, delete remote files or notify external systems before a record
crosses the Styx for good.

## 官网

- 主页: https://github.com/mediafinger/styxable
- 更新日志: https://github.com/mediafinger/styxable/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/styxable

## 历史版本号

- 0.1.1 (2026-09-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/styxable
- gem 安装: `gem install styxable`
- Bundler: `gem "styxable"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/styxable-0.1.1.gem
- 版本锁定: `gem "styxable", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
