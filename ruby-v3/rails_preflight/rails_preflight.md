# rails_preflight

**Tag**: web, testing, serialization, template, devops, filesystem

## 简介

Point rails-preflight at a Rails app and a target version. It reads the lockfile,
.ruby-version, Dockerfile, db/schema.rb and config, and scans Ruby, ERB, HAML and Slim
files for removed APIs, then writes a single HTML report: blockers, items to fix, what it
couldn't check, and a suggested path with one step per Rails minor version. The same
findings print as Markdown for coding agents or JSON for CI. Read-only and static. It
never modifies the app, runs it, or runs its tests.

## 官网

- 主页: https://github.com/aslam/rails-preflight
- 更新日志: https://github.com/aslam/rails-preflight/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/aslam/rails-preflight/issues
- RubyGems: https://rubygems.org/gems/rails_preflight

## 历史版本号

- 0.1.2 (2026-10-13)
- 0.1.1 (2026-10-09)
- 0.1.0 (2026-10-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails_preflight
- gem 安装: `gem install rails_preflight`
- Bundler: `gem "rails_preflight"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/rails_preflight-0.1.2.gem
- 版本锁定: `gem "rails_preflight", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
