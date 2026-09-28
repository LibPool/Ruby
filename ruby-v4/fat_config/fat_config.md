# fat_config

**Tag**: serialization, filesystem

## 简介

This library provides a reader for configuration files, looking for them in places
designated by (1) a user-set environment variable, (2) in the standard XDG
locations (e.g., /etc/xdg/app.yml), or (3) in the classical UNIX locations
(e.g. /etc/app/config.yml or ~/.apprc).  Config files can be written in one of
YAML, TOML, INI-style, or JSON.  It enforces precedence of user-configs over
system-level configs, and enviroment or command-line configs over the file-based
configs.

## 官网

- 主页: https://github.com/ddoherty.net/fat_config
- RubyGems: https://rubygems.org/gems/fat_config

## 历史版本号

- 0.8.0 (2026-02-10)
- 0.7.1 (2026-02-06)
- 0.7.0 (2026-02-05)
- 0.6.1 (2026-02-02)
- 0.4.2 (2025-03-19)
- 0.4.1 (2024-12-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/fat_config
- gem 安装: `gem install fat_config`
- Bundler: `gem "fat_config"`
- 最新版本: 0.8.0
- 最新版归档: https://rubygems.org/downloads/fat_config-0.8.0.gem
- 版本锁定: `gem "fat_config", "~> 0.8.0"`
- 中央仓库: https://rubygems.org/
