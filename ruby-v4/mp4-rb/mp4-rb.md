# mp4-rb

**Tag**: web, database, filesystem, data

## 简介

A learning-oriented Ruby library for parsing ISO/IEC 14496-12 MP4 containers
and turning them into adaptive-streaming assets. Parses every atom with BinData,
memoises the sample table into a pluggable cache (memory or SQLite), cuts each
track into keyframe-aligned fMP4 segments, and emits both DASH (MPD) manifests
and HLS (m3u8) master + media playlists that reference the same segment bytes.
Also includes a full MP4 remux path (regenerated moov from the cache) and an
XLSX per-sample analysis workbook. Read the code, run the demo, learn how MP4
works under the hood. Not production software.

## 官网

- 主页: https://github.com/edgarMeinart/mp4-rb
- 文档: https://github.com/edgarMeinart/mp4-rb#readme
- 问题追踪: https://github.com/edgarMeinart/mp4-rb/issues
- RubyGems: https://rubygems.org/gems/mp4-rb

## 历史版本号

- 0.1.0 (2026-07-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/mp4-rb
- gem 安装: `gem install mp4-rb`
- Bundler: `gem "mp4-rb"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/mp4-rb-0.1.0.gem
- 版本锁定: `gem "mp4-rb", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
