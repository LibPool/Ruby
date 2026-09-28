# oj_windows

**Tag**: web, serialization, networking, tooling

## 简介

oj_windows is a fork of Oj (https://github.com/ohler55/oj) by Peter Ohler, adapted to build with the MSVC (mswin) Ruby toolchain: pthread mutexes replaced with Windows primitives, POSIX headers guarded, and SIMD string scanning enabled under MSVC. It provides the full Oj API (module Oj) and JSON-gem compatibility. Because it defines the same Oj module, it is a replacement for - and cannot be installed alongside - the upstream oj gem. Requires Ruby 3.4+ built with the MSVC toolchain (RubyInstaller/MinGW users should use the upstream oj gem instead).

## 官网

- 主页: https://github.com/tigel-agm/oj_windows
- 文档: https://github.com/tigel-agm/oj_windows/blob/main/README.md
- 更新日志: https://github.com/tigel-agm/oj_windows/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/tigel-agm/oj_windows/issues
- RubyGems: https://rubygems.org/gems/oj_windows

## 历史版本号

- 3.17.2.1 (2026-05-29)
- 3.16.15 (2025-12-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/oj_windows
- gem 安装: `gem install oj_windows`
- Bundler: `gem "oj_windows"`
- 最新版本: 3.17.2.1
- 最新版归档: https://rubygems.org/downloads/oj_windows-3.17.2.1.gem
- 版本锁定: `gem "oj_windows", "~> 3.17.2.1"`
- 中央仓库: https://rubygems.org/
