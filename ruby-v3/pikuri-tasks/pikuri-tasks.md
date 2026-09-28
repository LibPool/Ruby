# pikuri-tasks

**Tag**: web

## 简介

pikuri-tasks gives a pikuri-core agent an in-memory task list it
can use to plan and track multi-step work. A +Pikuri::Tasks::List+
holds the per-Agent state; four tools (+task_create+,
+task_in_progress+, +task_completed+, +task_delete+) mutate it via
content-as-identifier (no item IDs to hallucinate).
+Pikuri::Tasks::Extension+ wires the list and tools onto an
+Pikuri::Agent+ via +c.add_extension(...)+ inside the +Agent.new+
block.

The list lives in process memory only — nothing is written to disk.
Sub-agents do not inherit the parent's list (consistent with the
"sub-agents do not inherit extensions" rule).

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-tasks

## 历史版本号

- 0.1.0 (2026-08-30)
- 0.0.7 (2026-06-11)
- 0.0.6 (2026-06-04)
- 0.0.5 (2026-06-04)
- 0.0.4 (2026-05-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-tasks
- gem 安装: `gem install pikuri-tasks`
- Bundler: `gem "pikuri-tasks"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-tasks-0.1.0.gem
- 版本锁定: `gem "pikuri-tasks", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
