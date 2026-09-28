# gem_kit-plugin

**Tag**: library

## 简介

gem_kit-release's `gem kit` command takes subcommands from other gems. This
gem adds one, `gem kit plugin`, which prints a page explaining how it got
there — and that is all it does. It exists to be read.

The whole mechanism is a GemKit::Release.plugin block in
lib/gem_kit/plugin.rb and a one-line lib/rubygems_plugin.rb that requires
it. RubyGems loads the latter on every `gem` invocation, so installing the
gem is the whole installation.

## 官网

- 主页: https://github.com/n-at-han-k/gem_kit-plugin
- 更新日志: https://github.com/n-at-han-k/gem_kit-plugin/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/n-at-han-k/gem_kit-plugin/issues
- RubyGems: https://rubygems.org/gems/gem_kit-plugin

## 历史版本号

- 0.1.0 (2026-08-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/gem_kit-plugin
- gem 安装: `gem install gem_kit-plugin`
- Bundler: `gem "gem_kit-plugin"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/gem_kit-plugin-0.1.0.gem
- 版本锁定: `gem "gem_kit-plugin", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
