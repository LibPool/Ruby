# ruby-bindgen

**Tag**: testing, serialization, tooling, filesystem

## 简介

ruby-bindgen reads C and C++ headers with libclang and emits Ruby bindings.
It supports three output formats: Rice C++ source for high-fidelity C++ wrappers,
raw FFI for plain C libraries, and CMake build files to compile the generated
extensions. Bindings are driven from a YAML configuration that controls header
matching, symbol filtering, name mapping, and version guards. Battle-tested
against OpenCV (thousands of classes) and PROJ.

## 官网

- 主页: https://github.com/ruby-rice/ruby-bindgen/
- 源码仓库: https://github.com/ruby-rice/ruby-bindgen
- 文档: https://ruby-rice.github.io/ruby-bindgen/
- 更新日志: https://github.com/ruby-rice/ruby-bindgen/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/ruby-rice/ruby-bindgen/issues
- RubyGems: https://rubygems.org/gems/ruby-bindgen

## 历史版本号

- 1.0.0 (2026-05-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruby-bindgen
- gem 安装: `gem install ruby-bindgen`
- Bundler: `gem "ruby-bindgen"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/ruby-bindgen-1.0.0.gem
- 版本锁定: `gem "ruby-bindgen", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
