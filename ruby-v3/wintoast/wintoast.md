# wintoast

**Tag**: web, cli, testing, serialization, tooling

## 简介

wintoast pops native Windows toast notifications from plain Ruby scripts using
the WinRT notification API that ships with Windows — no Windows App SDK, no
packaging, no COM activation server, no elevation — and drives progress on the
taskbar button (ITaskbarList3) and the Windows Terminal tab (OSC 9;4) at the
same time, so progress shows up under classic conhost AND modern terminals.

API: Wintoast.toast (title/body/attribution, app logo + hero images, system
sounds, duration, scenario, expiration, tag/group), Wintoast.register! /
unregister! (opt-in, reversible, per-user HKCU AppUserModelId branding — no
shortcut, no admin), Wintoast.progress / progress_clear, and
Wintoast::Payload.build for inspecting the exact toast XML. Windows MSVC
(mswin) Ruby only.

## 官网

- 主页: https://github.com/main-path/wintoast
- 更新日志: https://github.com/main-path/wintoast/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/wintoast/issues
- RubyGems: https://rubygems.org/gems/wintoast

## 历史版本号

- 0.1.0 (2026-06-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/wintoast
- gem 安装: `gem install wintoast`
- Bundler: `gem "wintoast"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/wintoast-0.1.0.gem
- 版本锁定: `gem "wintoast", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
