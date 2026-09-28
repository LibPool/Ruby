# pikuri-pdf

**Tag**: web

## 简介

pikuri-pdf plugs PDF → text extraction into pikuri-core's
+Pikuri::Extractor+ registry. The bundled +Pikuri::Extractors::PDF+
extractor wraps the pure-Ruby pdf-reader gem and extracts lazily:
paged reads (the +read+ tool's windows) parse only the pages the
window needs, so the first page of a 500-page PDF never pays for
the other 499.

Shipped separately from pikuri-core so the core's dependency tree
stays minimal and auditable: pdf-reader and its transitive deps
(Ascii85, afm, hashery, ruby-rc4, ttfunk) ride along only for hosts
that opt into PDF support.

Registration is explicit — +Pikuri::Extractors::PDF.register+ — so
requiring the gem changes nothing by itself; the host script picks
which extractors it wires in. One registration extends the +read+
tool, +web_scrape+, and the pikuri-vectordb indexer simultaneously.

## 官网

- 主页: https://codeberg.org/mvysny/pikuri
- 源码仓库: https://codeberg.org/mvysny/pikuri/src/branch/master
- 更新日志: https://codeberg.org/mvysny/pikuri/src/branch/master/CHANGELOG.md
- 问题追踪: https://codeberg.org/mvysny/pikuri/issues
- RubyGems: https://rubygems.org/gems/pikuri-pdf

## 历史版本号

- 0.1.0 (2026-08-30)
- 0.0.7 (2026-06-11)
- 0.0.6 (2026-06-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/pikuri-pdf
- gem 安装: `gem install pikuri-pdf`
- Bundler: `gem "pikuri-pdf"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pikuri-pdf-0.1.0.gem
- 版本锁定: `gem "pikuri-pdf", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
