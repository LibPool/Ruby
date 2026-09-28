# gem_kit-release

**Tag**: testing, tooling

## 简介

The maintainer's half of gem_kit: one RubyGems command, `gem kit`, with
subcommands for bumping the version, writing and linting the changelog,
listing outstanding deprecations, releasing and tagging.

It keeps the promises gem_kit records. `gem kit bump` refuses to move onto
a deprecation's removal version while the old name is still in the tree,
and `gem kit release` refuses to ship a version with an unkept promise or
no changelog entry of its own.

Everything is read from the .gemspec in the working directory, so the
normal case needs no configuration at all.

## 官网

- 主页: https://github.com/n-at-han-k/gem_kit
- 更新日志: https://github.com/n-at-han-k/gem_kit/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/n-at-han-k/gem_kit/issues
- RubyGems: https://rubygems.org/gems/gem_kit-release

## 历史版本号

- 0.3.2 (2026-08-30)
- 0.3.1 (2026-08-20)
- 0.3.0 (2026-08-20)
- 0.2.2 (2026-08-20)
- 0.2.1 (2026-08-20)
- 0.2.0 (2026-08-20)
- 0.1.0 (2026-08-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/gem_kit-release
- gem 安装: `gem install gem_kit-release`
- Bundler: `gem "gem_kit-release"`
- 最新版本: 0.3.2
- 最新版归档: https://rubygems.org/downloads/gem_kit-release-0.3.2.gem
- 版本锁定: `gem "gem_kit-release", "~> 0.3.2"`
- 中央仓库: https://rubygems.org/
