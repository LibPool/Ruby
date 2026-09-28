# gem_override_marker

**Tag**: template

## 简介

When you override a gem's method (e.g. with prepend) or copy a gem's
view/partial and edit it, upstream changes on upgrade can silently break it.
gem_override_marker lets you declare what each override is based on with a
@gem-override marker, and generate the diff against upstream on demand, so you
can efficiently re-apply your customization to the new version.

## 官网

- 主页: https://github.com/be-agile/gem_override_marker
- 文档: https://www.rubydoc.info/gems/gem_override_marker/0.1.0
- RubyGems: https://rubygems.org/gems/gem_override_marker

## 历史版本号

- 0.1.0 (2026-08-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/gem_override_marker
- gem 安装: `gem install gem_override_marker`
- Bundler: `gem "gem_override_marker"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/gem_override_marker-0.1.0.gem
- 版本锁定: `gem "gem_override_marker", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
