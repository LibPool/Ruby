# pikuri

**Tag**: web, filesystem

## 简介

+pikuri+ is the convenience bundle for the pikuri AI-assistant
toolkit. It ships no Ruby code of its own beyond a tiny entry
file that +require+'s each sibling gem; +gem install pikuri+
pulls in pikuri-core, pikuri-extractors, pikuri-pdf,
pikuri-skills, pikuri-tasks, pikuri-memory, pikuri-workspace,
pikuri-code, pikuri-lsp, pikuri-mcp, pikuri-subagents,
pikuri-vectordb, pikuri-assistant, and pikuri-os in one shot, and
+require 'pikuri'+ boots all of them.

Privacy-conscious users who want a minimal dependency tree to
audit should install +pikuri-core+ directly and opt into the
extension gems they actually need — same +bundle add+ pattern
Rails users have always had. See each pikuri-* gem's README
for its individual surface.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri

## 历史版本号

- 0.1.0 (2026-08-30)
- 0.0.7 (2026-06-11)
- 0.0.6 (2026-06-04)
- 0.0.5 (2026-06-04)
- 0.0.4 (2026-05-29)
- 0.0.3 (2026-05-22)
- 0.0.1 (2026-05-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri
- gem 安装: `gem install pikuri`
- Bundler: `gem "pikuri"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-0.1.0.gem
- 版本锁定: `gem "pikuri", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
