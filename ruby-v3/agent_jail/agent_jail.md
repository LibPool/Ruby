# agent_jail

**Tag**: filesystem

## 简介

Forks a child process, applies Linux Landlock filesystem restrictions and POSIX resource limits
(setrlimit), then runs your block. If the block times out, exceeds memory, or touches a disallowed
path, the child is killed and the parent gets a typed exception. macOS uses Seatbelt (sandbox_init).
Degrades gracefully on unsupported platforms.

## 官网

- 主页: https://github.com/jibranusman95/agent_jail
- 更新日志: https://github.com/jibranusman95/agent_jail/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/agent_jail

## 历史版本号

- 0.1.0 (2026-06-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/agent_jail
- gem 安装: `gem install agent_jail`
- Bundler: `gem "agent_jail"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/agent_jail-0.1.0.gem
- 版本锁定: `gem "agent_jail", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
