# psx

**Tag**: library

## 简介

A work-in-progress PlayStation 1 emulator written entirely in Ruby.
Implements the MIPS R3000A CPU, GTE, GPU (software rasteriser), DMA,
interrupts, timers, CD-ROM stub, SIO0 controller, and a minimal SPU —
enough to boot the SCPH1001 BIOS into the Memory Card / CD-ROM shell.
Ships an SDL2-backed front-end via the `psx` command. A BIOS image is
not included and must be supplied by the user.

## 官网

- 主页: https://github.com/khasinski/psx
- 更新日志: https://github.com/khasinski/psx/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/khasinski/psx/issues
- RubyGems: https://rubygems.org/gems/psx

## 历史版本号

- 0.1.0 (2026-05-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/psx
- gem 安装: `gem install psx`
- Bundler: `gem "psx"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/psx-0.1.0.gem
- 版本锁定: `gem "psx", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
