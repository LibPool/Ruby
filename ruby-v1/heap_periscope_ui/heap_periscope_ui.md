# heap_periscope_ui

**Tag**: web, database, filesystem, data

## 简介

HeapPeriscopeUi is a Rails engine designed to help developers monitor, visualize, and diagnose memory-related issues within their Ruby applications. It functions by listening for UDP packets containing GC profiler reports and heap snapshots, typically transmitted by a companion agent (like `heap_periscope_agent`). The engine efficiently processes this data: GC reports are batched for optimized database insertion, while comprehensive heap snapshots, including detailed object counts by class, are stored transactionally. Furthermore, HeapPeriscopeUi can broadcast incoming metrics via ActionCable for real-time dashboard updates. Its integrated web interface allows users to browse, filter, and analyze the collected profiler reports, facilitating the identification of memory leaks, excessive object allocations, and opportunities for performance optimization.

## 官网

- 主页: https://github.com/codepawpaw/heap_periscope_ui
- 更新日志: https://github.com/codepawpaw/heap_periscope_ui/releases
- RubyGems: https://rubygems.org/gems/heap_periscope_ui

## 历史版本号

- 0.1.0 (2025-08-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/heap_periscope_ui
- gem 安装: `gem install heap_periscope_ui`
- Bundler: `gem "heap_periscope_ui"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/heap_periscope_ui-0.1.0.gem
- 版本锁定: `gem "heap_periscope_ui", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
