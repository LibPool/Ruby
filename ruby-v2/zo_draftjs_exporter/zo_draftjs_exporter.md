# zo_draftjs_exporter

**Tag**: template, tooling, filesystem

## 简介

Draft.js is a framework for building rich text editors. However, it does not support exporting documents at
HTML. This gem is designed to take the raw `ContentState` (output of `convertToRaw`) from Draft.js and convert
it to HTML using Ruby.

This is a Zero One fork of the `draftjs_exporter` gem, published separately as `zo_draftjs_exporter`. It adds
a `block_callback:` hook invoked after each block is rendered, and support for `className` entries in the
`style_map` so inline styles can emit CSS classes alongside inline `style` attributes. It keeps the upstream
`draftjs_exporter` require paths and `DraftjsExporter` namespace, so it cannot be installed alongside the
original gem.

## 官网

- 主页: https://github.com/zero-one-software/draftjs_exporter
- RubyGems: https://rubygems.org/gems/zo_draftjs_exporter

## 历史版本号

- 0.0.7 (2026-09-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/zo_draftjs_exporter
- gem 安装: `gem install zo_draftjs_exporter`
- Bundler: `gem "zo_draftjs_exporter"`
- 最新版本: 0.0.7
- 最新版归档: https://rubygems.org/downloads/zo_draftjs_exporter-0.0.7.gem
- 版本锁定: `gem "zo_draftjs_exporter", "~> 0.0.7"`
- 中央仓库: https://rubygems.org/
