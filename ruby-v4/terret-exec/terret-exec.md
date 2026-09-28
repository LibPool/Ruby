# terret-exec

**Tag**: cli, security, filesystem

## 简介

ctx[:fs]: workspace-contained file ops (read/write/edit/stat/glob) behind an fs/authorize waterfall, with realpath-based containment that fails closed on traversal and symlink escapes. ctx[:subprocess] spawns and captures under the fiber scheduler with cooperative cancellation; ctx[:shell] keeps a bash per agent alive across calls; ctx[:terminals] holds named long-lived PTYs; ctx[:jobs] runs a command past the turn that started it; and every argv reaches a process through the ctx[:sandbox] seam. Zero runtime dependencies beyond stdlib.

## 官网

- 主页: https://terret.org
- 源码仓库: https://github.com/terret-org/terret
- 问题追踪: https://github.com/terret-org/terret/issues
- RubyGems: https://rubygems.org/gems/terret-exec

## 历史版本号

- 0.1.0 (2026-08-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/terret-exec
- gem 安装: `gem install terret-exec`
- Bundler: `gem "terret-exec"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/terret-exec-0.1.0.gem
- 版本锁定: `gem "terret-exec", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
