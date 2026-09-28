# pikuri-code

**Tag**: web, filesystem

## 简介

pikuri-code adds the shell-and-dev-loop layer on top of
pikuri-workspace's filesystem tools: a +Pikuri::Code::Bash+ that
runs commands via the +Pikuri::Subprocess+ chokepoint with
+Confirmer+ gating (optionally wrapped in a
+Pikuri::Code::Bash::Sandbox::Bubblewrap+ filesystem sandbox),
plus the demo +bin/pikuri-code+ binary that wires file + shell +
web tools into an interactive coding agent rooted at the current
working directory. The +Pikuri.prompt+ search path picks up this
gem's +prompts/coding-system-prompt.txt+ automatically on require.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-code

## 历史版本号

- 0.1.0 (2026-08-30)
- 0.0.7 (2026-06-11)
- 0.0.6 (2026-06-04)
- 0.0.5 (2026-06-04)
- 0.0.4 (2026-05-29)
- 0.0.3 (2026-05-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-code
- gem 安装: `gem install pikuri-code`
- Bundler: `gem "pikuri-code"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-code-0.1.0.gem
- 版本锁定: `gem "pikuri-code", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
