# zuzu

**Tag**: cli, database, tooling, devops, filesystem, data

## 简介

Every installed application is an orchestrator of OS capabilities. LLMs are simply a more expressive interface for that orchestration. Zuzu is a framework for building installable, AI-native desktop apps where the intelligence runs on the user's hardware — not in a data center. It uses JRuby and Glimmer DSL for SWT for the GUI, Mozilla's llamafile for local LLM inference, and SQLite (via AgentFS) as a sandboxed virtual filesystem the agent can read and write without touching the host OS. Apps ship as a cross-platform .jar, or as a native installer (.dmg/.deb/.exe) with a JRE bundled via jpackage — users download, double-click, and run with no Java installation required. No cloud. No subscriptions. No infrastructure to operate. Scaffolded projects include CLAUDE.md and Claude Code skills pre-tuned to Zuzu's patterns, so coding agents generate correct framework code from the start.

## 官网

- 主页: https://github.com/parolkar/zuzu
- 源码仓库: https://github.com/parolkar/zuzu/tree/main
- 问题追踪: https://github.com/parolkar/zuzu/issues
- RubyGems: https://rubygems.org/gems/zuzu

## 历史版本号

- 0.2.3-java (2026-03-07)
- 0.2.2-java (2026-03-06)
- 0.2.1-java (2026-03-06)
- 0.0.1-java (2026-03-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/zuzu
- gem 安装: `gem install zuzu`
- Bundler: `gem "zuzu"`
- 最新版本: 0.2.3
- 最新版归档: https://rubygems.org/downloads/zuzu-0.2.3.gem
- 版本锁定: `gem "zuzu", "~> 0.2.3"`
- 中央仓库: https://rubygems.org/
