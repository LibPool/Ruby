# grx-tensor

**Tag**: library

## 简介

GRX brings PyTorch-style tensor operations to Ruby. Every arithmetic op,
activation, and optimizer step runs through a native C library with
dynamic multi-target SIMD dispatch (AVX2+FMA, SSE, and scalar fallback).
Ruby is the interface — C does the work.

Features: autograd, SGD/Adam optimizers, Linear/Sequential/Dropout/BatchNorm
layers, MSE/BCE/CrossEntropy loss functions, Xavier and He weight init.
Cross-platform: .so on Linux, .dylib on macOS, .dll on Windows.

## 官网

- 主页: https://github.com/Gabo-Razo/grx-tensor
- 更新日志: https://github.com/Gabo-Razo/grx-tensor/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/Gabo-Razo/grx-tensor/issues
- RubyGems: https://rubygems.org/gems/grx-tensor

## 历史版本号

- 0.2.1 (2026-08-30)
- 0.2.0 (2026-08-22)
- 0.1.0 (2026-05-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/grx-tensor
- gem 安装: `gem install grx-tensor`
- Bundler: `gem "grx-tensor"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/grx-tensor-0.2.1.gem
- 版本锁定: `gem "grx-tensor", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
