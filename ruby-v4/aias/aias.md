# aias

**Tag**: web, serialization, filesystem

## 简介

aias turns AIA prompt files into unattended cron jobs. Add a schedule: key
to any prompt's YAML frontmatter and run `aias update` to install the full
set, or `aias add <path>` to install a single prompt without touching the
rest. Schedules accept raw cron expressions or natural-language strings
("every weekday at 9am"). Run `aias install` once to capture your PATH,
API keys, and AIA variables into env.sh — every job sources it at runtime.
Output is written to a per-prompt log under ~/.config/aia/schedule/logs/.
Prompts are self-describing — no separate configuration file is needed.

## 官网

- 主页: https://github.com/madbomber/aias
- 更新日志: https://github.com/madbomber/aias/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/aias

## 历史版本号

- 0.1.0 (2026-03-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/aias
- gem 安装: `gem install aias`
- Bundler: `gem "aias"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/aias-0.1.0.gem
- 版本锁定: `gem "aias", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
