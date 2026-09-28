# terret-sandbox-docker

**Tag**: cli, networking, devops, filesystem

## 简介

ctx[:sandbox] backed by a long-lived container: one patch row swaps this plugin in and every argv the harness spawns — Bash, Grep, the PTY tools — starts running inside it, with no change to any tool. The workspace is bind-mounted at its own realpath, so host-side file ops and in-container processes see one world at one set of paths; the network is denied by default. Shells out to the docker CLI, so there are no runtime dependencies beyond stdlib.

## 官网

- 主页: https://terret.org
- 源码仓库: https://github.com/terret-org/terret
- 问题追踪: https://github.com/terret-org/terret/issues
- RubyGems: https://rubygems.org/gems/terret-sandbox-docker

## 历史版本号

- 0.1.0 (2026-08-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/terret-sandbox-docker
- gem 安装: `gem install terret-sandbox-docker`
- Bundler: `gem "terret-sandbox-docker"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/terret-sandbox-docker-0.1.0.gem
- 版本锁定: `gem "terret-sandbox-docker", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
