# kaitai-struct-visualizer

**Tag**: web, networking, template, tooling, filesystem, data

## 简介

Kaitai Struct is a declarative language used for describe various binary data structures, laid out in files or in memory: i.e. binary file formats, network stream packet formats, etc.

The main idea is that a particular format is described in Kaitai Struct language (.ksy file) and then can be compiled with ksc into source files in one of the supported programming languages. These modules will include a generated code for a parser that can read described data structure from a file / stream and give access to it in a nice, easy-to-comprehend API.

This package is a visualizer tool for .ksy files. Given a particular binary file and .ksy file(s) that describe its format, it can visualize internal data structures in a tree form and a multi-level highlight hex viewer.

## 官网

- 主页: https://kaitai.io/
- 源码仓库: https://github.com/kaitai-io/kaitai_struct_visualizer
- 问题追踪: https://github.com/kaitai-io/kaitai_struct_visualizer/issues
- RubyGems: https://rubygems.org/gems/kaitai-struct-visualizer

## 历史版本号

- 0.11 (2025-09-19)
- 0.7 (2017-12-08)
- 0.5 (2016-11-15)
- 0.4 (2016-08-09)
- 0.3 (2016-04-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/kaitai-struct-visualizer
- gem 安装: `gem install kaitai-struct-visualizer`
- Bundler: `gem "kaitai-struct-visualizer"`
- 最新版本: 0.11
- 最新版归档: https://rubygems.org/downloads/kaitai-struct-visualizer-0.11.gem
- 版本锁定: `gem "kaitai-struct-visualizer", "~> 0.11"`
- 中央仓库: https://rubygems.org/
