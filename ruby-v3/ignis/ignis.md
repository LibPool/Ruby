# ignis

**Tag**: tooling

## 简介

Ignis is the foundation of a CUDA-backed deep-learning ecosystem for Ruby that
actually targets native Windows. It provides a GPU n-dimensional array
(Ignis::NDArray), CUDA memory/device management, a runtime kernel compiler
(NVRTC) with a batteries-included kernel library, fp16/bf16 conversion, and
cuBLAS GEMM. Kernels are compiled at runtime and libraries are bound via FFI —
there are NO C extensions, so installation needs no compiler or devkit (the
usual Windows native-gem killer). Requires an NVIDIA GPU + CUDA toolkit/runtime.

## 官网

- 主页: https://github.com/tigel-agm/Ignis
- RubyGems: https://rubygems.org/gems/ignis

## 历史版本号

- 0.0.1 (2026-05-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/ignis
- gem 安装: `gem install ignis`
- Bundler: `gem "ignis"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/ignis-0.0.1.gem
- 版本锁定: `gem "ignis", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
