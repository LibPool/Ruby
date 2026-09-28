# code_quality_check

**Tag**: web, security, tooling, filesystem

## 简介

Code Quality Check is a Ruby on Rails gem that runs automated quality and security
checks on every commit using Overcommit and Git hooks. It bundles and configures
RuboCop (style and lint), Brakeman (security), Rails Best Practices, and
BundleAudit (CVE checks). The installer sets up a Rails initializer that verifies
the gem is installed and ensures Overcommit hooks are present, so teams don't
silently skip checks. Optional support for Reek, Flay, and Fasterer via
.overcommit.yml. Requires Overcommit in your Gemfile; add the gem and run
`rails generate code_quality_check:install` to get started.

## 官网

- 主页: https://github.com/aniruddhami/code_quality_check
- 文档: https://github.com/aniruddhami/code_quality_check#readme
- 更新日志: https://github.com/aniruddhami/code_quality_check/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/code_quality_check

## 历史版本号

- 0.1.9 (2026-08-21)
- 0.1.8 (2026-03-03)
- 0.1.6 (2025-02-27)
- 0.1.5 (2025-02-20)
- 0.1.4 (2025-02-03)
- 0.1.3 (2025-01-29)
- 0.1.2 (2025-01-29)
- 0.1.1 (2025-01-28)
- 0.1.0 (2025-01-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/code_quality_check
- gem 安装: `gem install code_quality_check`
- Bundler: `gem "code_quality_check"`
- 最新版本: 0.1.9
- 最新版归档: https://rubygems.org/downloads/code_quality_check-0.1.9.gem
- 版本锁定: `gem "code_quality_check", "~> 0.1.9"`
- 中央仓库: https://rubygems.org/
