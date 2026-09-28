# pikuri-subagents

**Tag**: networking

## 简介

pikuri-subagents owns the sub-agent (delegation) feature top
to bottom: the +Pikuri::SubAgent::SubAgentTool+ class (exposed
to the LLM as the +agent+ tool), the +Persona+ record, the
+Extension+ that wires it onto an agent, and the bundled
+Pikuri::SubAgent::RESEARCHER+ persona (network-read only).
Hosts that want sub-agents add this gem as a runtime dep and
call +c.add_extension Pikuri::SubAgent::Extension.new(personas: [...])+
inside their +Agent.new+ block — same opt-in shape as
+pikuri-skills+ / +pikuri-mcp+. Also ships +bin/pikuri-minions+
as a fan-out delegation demo.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-subagents

## 历史版本号

- 0.1.0 (2026-08-30)
- 0.0.7 (2026-06-11)
- 0.0.6 (2026-06-04)
- 0.0.5 (2026-06-04)
- 0.0.4 (2026-05-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-subagents
- gem 安装: `gem install pikuri-subagents`
- Bundler: `gem "pikuri-subagents"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-subagents-0.1.0.gem
- 版本锁定: `gem "pikuri-subagents", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
