# puma-plugin-delayed_stop

**Tag**: devops

## 简介

A Puma plugin that intercepts a configurable signal (default: SIGQUIT) and
waits a configurable number of seconds before telling Puma to stop. This
gives orchestrators like Kubernetes and Docker Swarm time to remove the
container from load balancing before connections are closed.

## 官网

- 主页: https://github.com/BerkeleyLibrary/puma-plugin-delayed_stop
- 更新日志: https://github.com/BerkeleyLibrary/puma-plugin-delayed_stop/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/puma-plugin-delayed_stop

## 历史版本号

- 0.1.2 (2026-03-20)
- 0.1.1 (2026-03-20)
- 0.1.0 (2026-03-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/puma-plugin-delayed_stop
- gem 安装: `gem install puma-plugin-delayed_stop`
- Bundler: `gem "puma-plugin-delayed_stop"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/puma-plugin-delayed_stop-0.1.2.gem
- 版本锁定: `gem "puma-plugin-delayed_stop", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
