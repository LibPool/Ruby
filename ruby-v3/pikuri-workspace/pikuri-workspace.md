# pikuri-workspace

**Tag**: cli, filesystem

## 简介

pikuri-workspace adds "operate on a directory tree" to pikuri-core
agents: the +Pikuri::Workspace::Filesystem+ class that scopes
filesystem access to an anchor + explicit readable / writable
prefix lists (with optional ephemeral temp playground), the
+Pikuri::Workspace::Confirmer+ seam (+AUTO_APPROVE+ + +TERMINAL+)
for user-state mutations, and five tools wired to those seams:
+Pikuri::Workspace::Read+, +Pikuri::Workspace::Write+,
+Pikuri::Workspace::Edit+, +Pikuri::Workspace::Grep+, and
+Pikuri::Workspace::Glob+. Self-contained — no shell execution;
+Pikuri::Code::Bash+ ships in pikuri-code on top of these.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-workspace

## 历史版本号

- 0.1.0 (2026-08-30)
- 0.0.7 (2026-06-11)
- 0.0.6 (2026-06-04)
- 0.0.5 (2026-06-04)
- 0.0.4 (2026-05-29)
- 0.0.3 (2026-05-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-workspace
- gem 安装: `gem install pikuri-workspace`
- Bundler: `gem "pikuri-workspace"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-workspace-0.1.0.gem
- 版本锁定: `gem "pikuri-workspace", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
