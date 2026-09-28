# pikuri-memory

**Tag**: web, cli, networking, devops, filesystem

## 简介

pikuri-memory gives a pikuri-core agent durable, long-lived
memory: facts about the user and their work that persist across
conversations. It wires a +recall+ tool plus an automatic
per-turn prefetch onto an agent via
+c.add_extension Pikuri::Memory::Extension.new(...)+ inside the
+Agent.new+ block — same opt-in shape as +pikuri-tasks+ /
+pikuri-vectordb+. Recall is automatic and synchronous (embed +
vector search, milliseconds); capture is automatic and
asynchronous (an off-the-interaction-path extraction queue), so
a turn never blocks on "what should I remember?".

Storage is mem0 (https://github.com/mem0ai/mem0) reached over a
thin Faraday HTTP client — the append-only +add+ / read-time
+search+ model. Only the *user's own words* are fed to
extraction (a write-side hygiene rule that structurally drops
system/assistant/tool-sourced junk), and recalled context enters
the chat as a +:system+ message so it is provenance-tagged and
excluded from the next extraction pass. This release ships the
Ruby client + extension + tool against a *bring-your-own* mem0
endpoint; a self-managed mem0 sidecar supervisor (the
+ChromaServer+-style docker pattern) is a follow-on.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-memory

## 历史版本号

- 0.1.0 (2026-08-30)
- 0.0.7 (2026-06-11)
- 0.0.6 (2026-06-04)
- 0.0.5 (2026-06-04)
- 0.0.4 (2026-05-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-memory
- gem 安装: `gem install pikuri-memory`
- Bundler: `gem "pikuri-memory"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-memory-0.1.0.gem
- 版本锁定: `gem "pikuri-memory", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
