# zpl_render

**Tag**: template

## 简介

A pure-Ruby ZPL II renderer. Parses ^XA..^XZ label formats and rasterizes them at true printer resolution (dots), producing PNG images and print-size PDF documents. Code 128 (^BC, incl. Zebra subset invocation codes and GS1 modes), QR (^BQ), Code 39 (^B3) and Interleaved 2 of 5 (^B2) are generated module-exact so scanners read them reliably. Also supports text fields, field blocks, graphic boxes/circles/diagonals, ^GF images (ASCII hex, Zebra RLE, B64/Z64) and ~DG/^XG stored graphics.

## 官网

- 主页: https://github.com/wqsaali/zpl_render
- 更新日志: https://github.com/wqsaali/zpl_render/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/wqsaali/zpl_render/issues
- RubyGems: https://rubygems.org/gems/zpl_render

## 历史版本号

- 0.2.0 (2026-07-31)
- 0.1.0 (2026-07-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/zpl_render
- gem 安装: `gem install zpl_render`
- Bundler: `gem "zpl_render"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/zpl_render-0.2.0.gem
- 版本锁定: `gem "zpl_render", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
