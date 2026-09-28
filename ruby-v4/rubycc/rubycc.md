# rubycc

**Tag**: testing, serialization, tooling, data

## 简介

rubycc builds Ruby C extensions on a machine that has no gcc, no binutils, no make
and no shell. It is a C11-subset compiler, an assembler-free ELF writer, a linker,
an ar, a make, a pkg-config shim and a preprocessor, written in Ruby, plus the libc
headers a build needs -- so a distroless image with no libc development package
still compiles ruby.h.

Targets x86-64 and AArch64 Linux (ELF64) against glibc and musl. Generated code is
unoptimized: the point is that the extension builds and its own test suite passes,
which is the level at which every gem recorded in data/verified_gems.json was
verified. See the README for the verified gems, the measured limits, and what is
out of scope.

## 官网

- 主页: https://github.com/nuna/rubycc
- 文档: https://github.com/nuna/rubycc/blob/master/README.md
- 更新日志: https://github.com/nuna/rubycc/blob/master/CHANGELOG.md
- 问题追踪: https://github.com/nuna/rubycc/issues
- RubyGems: https://rubygems.org/gems/rubycc

## 历史版本号

- 1.1.0 (2026-09-12)
- 1.0.0 (2026-08-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/rubycc
- gem 安装: `gem install rubycc`
- Bundler: `gem "rubycc"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/rubycc-1.1.0.gem
- 版本锁定: `gem "rubycc", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
