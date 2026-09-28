# constable-rails

**Tag**: web, cli, testing, tooling, filesystem

## 简介

Constable replaces RSpec/Minitest for Rails apps that want tests to be fast and
non-flaky by construction. Every test is isolated by default, nondeterminism is a
lint error rather than a CI surprise, and every escape hatch is reported until
someone deals with it. Existing RSpec and Minitest suites adopt it with a one-line
change per file and zero rewriting -- cold cases run verbatim through their original
engine while native cases run under strict rules, side by side in one run.

Ships with a case-file DSL (investigate/witness/briefing/docket), transactional
isolation, flake history with rename-surviving content-hash identity, a jail and
parole docket for legacy red suites, warrants for automatic flake detection, diff-based
coverage, parallel workers, git-diff test selection, and a RuboCop extension.

The gem is published as "constable-rails"; everything inside it -- the module, the
CLI, the config directory -- is simply "constable".

## 官网

- 主页: https://github.com/Ray-Hughes/constable
- 文档: https://github.com/Ray-Hughes/constable#readme
- 更新日志: https://github.com/Ray-Hughes/constable/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/Ray-Hughes/constable/issues
- RubyGems: https://rubygems.org/gems/constable-rails

## 历史版本号

- 2.1.1 (2026-09-09)
- 2.1.0 (2026-09-09)
- 2.0.0 (2026-09-09)
- 1.4.2 (2026-09-09)
- 1.4.1 (2026-09-09)
- 1.4.0 (2026-09-09)
- 1.3.3 (2026-09-08)
- 1.3.2 (2026-09-08)
- 1.3.1 (2026-09-08)
- 1.3.0 (2026-09-08)
- 1.2.0 (2026-09-08)
- 1.1.0 (2026-09-08)
- 1.0.0 (2026-09-08)
- 0.1.0 (2026-09-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/constable-rails
- gem 安装: `gem install constable-rails`
- Bundler: `gem "constable-rails"`
- 最新版本: 2.1.1
- 最新版归档: https://rubygems.org/downloads/constable-rails-2.1.1.gem
- 版本锁定: `gem "constable-rails", "~> 2.1.1"`
- 中央仓库: https://rubygems.org/
