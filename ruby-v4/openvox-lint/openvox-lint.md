# openvox-lint

**Tag**: testing, tooling, filesystem

## 简介

openvox-lint is a modern style-guide linter for OpenVox and Puppet manifests.
It checks your .pp files against the OpenVox Language Style Guide (the
current canonical reference) and catches common errors, deprecated patterns
(legacy facts, Hiera 3, import, etc.), strict-mode issues, and Puppet 8+ /
OpenVox 8.x problems. Includes real --fix support for five checks:
trailing_whitespace, hard_tabs, quoted_booleans, double_quoted_strings,
and single_quote_string_with_variables.

Fully compatible with OpenVox 8.x and Puppet 8.x. Drop-in replacement for
the archived puppet-lint with Ruby 2.6+ support and OpenVox-specific
checks.

## 官网

- 主页: https://github.com/cvquesty/openvox-lint
- 更新日志: https://github.com/cvquesty/openvox-lint/blob/development/CHANGELOG.md
- 问题追踪: https://github.com/cvquesty/openvox-lint/issues
- RubyGems: https://rubygems.org/gems/openvox-lint

## 历史版本号

- 1.3.4 (2026-09-21)
- 1.3.2 (2026-05-24)
- 1.3.1 (2026-05-24)
- 1.3.0 (2026-05-23)
- 1.0.8 (2026-03-04)
- 1.0.7 (2026-02-27)
- 1.0.4 (2026-02-12)
- 1.0.3 (2026-02-12)
- 1.0.2 (2026-02-12)
- 1.0.1 (2026-02-12)
- 1.0.0 (2026-02-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/openvox-lint
- gem 安装: `gem install openvox-lint`
- Bundler: `gem "openvox-lint"`
- 最新版本: 1.3.4
- 最新版归档: https://rubygems.org/downloads/openvox-lint-1.3.4.gem
- 版本锁定: `gem "openvox-lint", "~> 1.3.4"`
- 中央仓库: https://rubygems.org/
