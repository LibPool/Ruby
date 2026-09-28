# scrapetor

**Tag**: web, security, serialization, networking, template, tooling, filesystem, data

## 简介

Scrapetor is a Ruby HTML parsing + scraping toolkit. The parser is a native C arena DOM with structural indexes built at parse time and NEON SIMD scanners in the SAX hot loop. A streaming extraction engine compiles the schema DSL into a single forward pass — no DOM materialised, one Ruby boundary crossing per document. On builds where libcurl is available, Scrapetor::Fetcher adds an HTTP/2-capable fetch layer with per-thread connection cache, shared DNS + TLS session pool, in-process gzip / deflate / brotli / zstd decoding, iconv charset transcoding, retry + exponential backoff, ETag / Last-Modified disk cache with bulk revalidation, per-host throttle, cookie jar, basic + bearer auth, proxy, and three bulk concurrency models (parallel_fetch / multi_fetch / streaming multi_each). Scrapetor::Session ties the cookie / auth / throttle / retry policies together. Also ships robots.txt + sitemap.xml parsers, a bounded-memory streaming HTML parser, and structured-data extractors (JSON-LD, OpenGraph, Schema.org, Microdata, RDFa, Twitter Cards). The Net::HTTP-based Scrapetor.fetch is preserved as the no-libcurl fallback.

## 官网

- 主页: http://scrapetor.org
- 源码仓库: https://github.com/Alaa-abdulridha/scrapetor
- 文档: http://scrapetor.org/docs
- 更新日志: https://github.com/Alaa-abdulridha/scrapetor/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/Alaa-abdulridha/scrapetor/issues
- RubyGems: https://rubygems.org/gems/scrapetor

## 历史版本号

- 0.2.0 (2026-05-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/scrapetor
- gem 安装: `gem install scrapetor`
- Bundler: `gem "scrapetor"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/scrapetor-0.2.0.gem
- 版本锁定: `gem "scrapetor", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
