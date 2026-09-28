# okf-tui

**Tag**: cli, testing, template, filesystem

## 简介

okf-tui is a full-screen terminal UI over OKF (Open Knowledge Format) bundles.
It reads a bundle in the order the spec intends — index.md, log.md, then each
directory — renders concept bodies as markdown, and finds within them. It
browses and configures the per-user bundle registry, switches the active
bundle, and searches every bundle in scope through one shared index, so the
scores compare between them. It shows each bundle's standing (conformance and
curation) wherever the bundle is named, and its knowledge graph as a set of
facets to narrow by or follow into the file. It invents no analysis: the okf
gem's pure core answers every question on screen.

## 官网

- 主页: https://github.com/serradura/okf
- 更新日志: https://github.com/serradura/okf/blob/main/gems/okf-tui/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/okf-tui

## 历史版本号

- 1.1.0 (2026-08-22)
- 1.0.1 (2026-08-20)
- 1.0.0 (2026-08-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/okf-tui
- gem 安装: `gem install okf-tui`
- Bundler: `gem "okf-tui"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/okf-tui-1.1.0.gem
- 版本锁定: `gem "okf-tui", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
