# gem_kit

**Tag**: library

## 简介

A deprecation is a dated promise: it names its replacement and the version
the old name stops existing in. GemKit::Deprecate declares that promise --
`deprecate` for a method, `superseded_by` for a renamed constant -- warns
on use naming the caller, and registers the deadline so it can be checked.

Built on Gem::Deprecate, so the message format and Gem::Deprecate.skip_during
work as they already do. No dependencies beyond RubyGems' own: a library
that deprecates a name should not thereby acquire a release toolchain.

The checking lives in the gem_kit-release gem, which reads this registry.

## 官网

- 主页: https://github.com/n-at-han-k/gem_kit
- 更新日志: https://github.com/n-at-han-k/gem_kit/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/n-at-han-k/gem_kit/issues
- RubyGems: https://rubygems.org/gems/gem_kit

## 历史版本号

- 0.2.0 (2026-08-20)
- 0.1.1 (2026-03-20)
- 0.1.0 (2026-03-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/gem_kit
- gem 安装: `gem install gem_kit`
- Bundler: `gem "gem_kit"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/gem_kit-0.2.0.gem
- 版本锁定: `gem "gem_kit", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
