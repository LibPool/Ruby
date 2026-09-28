# arrolio

**Tag**: testing, template, tooling

## 简介

Arrolio is a paged-media layout engine: it takes a content tree
plus a layout spec (page templates, styles, flows) and produces a
sequence of laid-out pages, which a renderer then emits — by
default to PDF bytes via the sibling `pdfrb` gem.

Arrolio is the middle layer of a three-library stack:

  * `pdfrb`     — pure-Ruby PDF library (bytes <-> model).
  * `arrolio`  — FOP-like paged layout (this gem; depends on pdfrb).
  * `loom`      — multi-target layout compiler (separate gem; emits
                  to Arrolio, CSS, XSL-FO, IDML).

Arrolio itself owns: page templates, threaded flows, Knuth-Plass
line and page breaking, tables, lists, SVG, page-model selection,
running headers/footers, and the rendering pipeline. It does not
own the PDF byte format (Pdfrb does) or any DSL (Loom does).

## 官网

- 主页: https://github.com/arrolio/arrolio
- 更新日志: https://github.com/arrolio/arrolio/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/arrolio/arrolio/issues
- RubyGems: https://rubygems.org/gems/arrolio

## 历史版本号

- 0.1.7 (2026-09-02)
- 0.1.6 (2026-08-31)
- 0.1.5 (2026-08-31)
- 0.1.4 (2026-08-31)
- 0.1.3 (2026-08-30)
- 0.1.2 (2026-08-29)
- 0.1.1 (2026-08-29)
- 0.1.0 (2026-08-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/arrolio
- gem 安装: `gem install arrolio`
- Bundler: `gem "arrolio"`
- 最新版本: 0.1.7
- 最新版归档: https://rubygems.org/downloads/arrolio-0.1.7.gem
- 版本锁定: `gem "arrolio", "~> 0.1.7"`
- 中央仓库: https://rubygems.org/
