# nbk2pdf

**Tag**: cli, database, template, tooling, filesystem, data

## 简介

Reads the `nbk` files a Kindle Scribe writes and renders them as vector PDFs,
complete with the ruled or squared background the notes were written on,
and adds what was written on a PDF on the device to a copy of that PDF.

Includes a reader for the signature container the device wraps its SQLite
database in, a binary Amazon Ion parser, and a decoder for the second-order
delta encoding the firmware stores pen strokes in. Ships the `nbk2pdf`
command line tool.

## 官网

- 文档: https://www.rubydoc.info/gems/nbk2pdf/1.1.0
- RubyGems: https://rubygems.org/gems/nbk2pdf

## 历史版本号

- 1.1.0 (2026-10-21)
- 1.0.1 (2026-10-20)
- 1.0.0 (2026-10-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/nbk2pdf
- gem 安装: `gem install nbk2pdf`
- Bundler: `gem "nbk2pdf"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/nbk2pdf-1.1.0.gem
- 版本锁定: `gem "nbk2pdf", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
