# vcdeps

**Tag**: web, cli, serialization, tooling, filesystem, data

## 简介

vcdeps wires Microsoft's vcpkg package manager into mkmf: declare native
dependencies in ext/<gem>/vcpkg.json, call Vcdeps.mkmf! from extconf.rb, and
vcdeps locates (or bootstraps) vcpkg, installs the ports out of tree with the
correct dynamic-CRT triplet, prepends the include/lib paths so they win over
Ruby's own opt-dir, and vendors the runtime DLLs with a generated
Fiddle-preload shim so the built extension actually loads.

It provides a library API (install!/vendor!/baseline!/tool!), the extconf
entry point Vcdeps.mkmf!, and a CLI (vcdeps doctor/where/install/vendor/
baseline/bootstrap). Manifest mode only; builds and caches live under
%LOCALAPPDATA%\vcdeps, never inside the gem. Windows MSVC (mswin) Ruby
only. Pure Ruby — no compiler required to install vcdeps itself.

## 官网

- 主页: https://github.com/main-path/vcdeps
- 更新日志: https://github.com/main-path/vcdeps/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/vcdeps/issues
- RubyGems: https://rubygems.org/gems/vcdeps

## 历史版本号

- 0.1.0 (2026-06-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/vcdeps
- gem 安装: `gem install vcdeps`
- Bundler: `gem "vcdeps"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/vcdeps-0.1.0.gem
- 版本锁定: `gem "vcdeps", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
