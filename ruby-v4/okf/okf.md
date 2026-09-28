# okf

**Tag**: web, cli, security, serialization, template, tooling, filesystem

## 简介

OKF (Open Knowledge Format) is portable knowledge: Markdown files with YAML
frontmatter that both humans and agents read from one source. This gem is the
Ruby-native way to work with it.

Its companion agent skill authors and curates a bundle. The `okf` command-line
tool validates the result for v0.1 (§9) conformance, lints its curation
quality, and answers questions about it: ranked full-text search, and a
progressive-disclosure map that reads a large bundle a directory at a time
rather than loading it whole. `okf server` opens it as an interactive
knowledge graph and `okf render` bakes that same page into one self-contained
HTML file you can host anywhere. A per-user registry names your bundles, so
every verb reaches them by @slug from any directory and one search can span
them all.

Everything the CLI does also runs in-process through a library API
(OKF::Bundle and friends), and the graph server is a mountable Rack app. It
adds no service to your stack: rack, webrick and minifts are the only runtime
dependencies, and it runs on every Ruby since 2.4.

## 官网

- 主页: https://github.com/serradura/okf
- 更新日志: https://github.com/serradura/okf/blob/main/gems/okf/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/okf

## 历史版本号

- 2.2.0 (2026-08-22)
- 2.1.1 (2026-08-20)
- 2.1.0 (2026-08-17)
- 2.0.0 (2026-08-15)
- 1.13.0 (2026-08-11)
- 1.12.0 (2026-07-24)
- 1.11.0 (2026-07-22)
- 1.10.0 (2026-07-21)
- 1.9.0 (2026-07-19)
- 1.8.0 (2026-07-17)
- 1.7.0 (2026-07-16)
- 1.6.0 (2026-07-16)
- 1.5.0 (2026-07-14)
- 1.4.0 (2026-07-13)
- 1.3.0 (2026-07-13)
- 1.2.0 (2026-07-12)
- 1.1.0 (2026-07-12)
- 1.0.0 (2026-07-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/okf
- gem 安装: `gem install okf`
- Bundler: `gem "okf"`
- 最新版本: 2.2.0
- 最新版归档: https://rubygems.org/downloads/okf-2.2.0.gem
- 版本锁定: `gem "okf", "~> 2.2.0"`
- 中央仓库: https://rubygems.org/
