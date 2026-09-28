# dommy-js-wasmtime

**Tag**: template, tooling

## 简介

A wasmtime-rb host for mruby-wasm-js builds (the Lilac component runtime is the primary example). It reimplements the mruby-wasm-js `js.*` handle-table ABI and the WASI preview1 surface in pure Ruby, routing JS interop into Dommy's `__js_get__/__js_set__/__js_call__/__js_new__` bridge protocol. The wasmtime sibling of dommy-js-quickjs — but instead of running JavaScript it drives Dommy from mruby running inside wasm.

## 官网

- 主页: https://github.com/takahashim/dommy-js-wasmtime
- 更新日志: https://github.com/takahashim/dommy-js-wasmtime/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/dommy-js-wasmtime

## 历史版本号

- 0.1.0 (2026-06-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/dommy-js-wasmtime
- gem 安装: `gem install dommy-js-wasmtime`
- Bundler: `gem "dommy-js-wasmtime"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/dommy-js-wasmtime-0.1.0.gem
- 版本锁定: `gem "dommy-js-wasmtime", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
