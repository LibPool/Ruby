# pikuri-os

**Tag**: testing, networking, devops, filesystem

## 简介

pikuri-os is the OS-integration layer for pikuri and the home of
the +bin/pikuri-os+ demo: a single, local, network-severed
agent that understands and operates the host OS (answer questions
about the machine, find and open files, read logs and explain
errors, advise on configuration). It is the federation's privacy-
first +@os+ member shipped standalone — no egress, no MCP, no cloud.

The gem holds the OS-specific surface (a localsearch-backed
content-search tool, a single-file +MACHINE.md+ resident memory,
and boot-time machine grounding) on top of pikuri-core's Agent +
Tool framework, pikuri-workspace's file tools, and pikuri-code's
Bash + sandbox. It deliberately does NOT depend on
pikuri-mcp/-memory/-vectordb: severing those keeps the no-egress,
"small enough to audit" posture honest.

See +ideas/pikuri-os.md+ in the repo for the full design.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-os

## 历史版本号

- 0.1.0 (2026-08-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-os
- gem 安装: `gem install pikuri-os`
- Bundler: `gem "pikuri-os"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-os-0.1.0.gem
- 版本锁定: `gem "pikuri-os", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
