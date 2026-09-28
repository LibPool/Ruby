# winreg

**Tag**: web, template, data

## 简介

winreg is a native extension exposing the Win32 registry through a typed,
hard-to-misuse Ruby API: strict typed readers and writers for REG_SZ,
REG_EXPAND_SZ (never auto-expanded), REG_MULTI_SZ (correct double-NUL wire
format), REG_DWORD/REG_QWORD (range-checked), and REG_BINARY, with raw
escape hatches for adversarial data; default-value access; 32/64-bit
registry views as a first-class option applied consistently to child
operations; least-privilege KEY_READ defaults; and RegNotifyChangeKeyValue
change watching (thread-agnostic registrations, rearm-before-deliver) that
blocks cooperatively under a Fiber scheduler and releases the GVL standalone.
Windows MSVC (mswin) Ruby only.

## 官网

- 主页: https://github.com/main-path/winreg
- 更新日志: https://github.com/main-path/winreg/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/winreg/issues
- RubyGems: https://rubygems.org/gems/winreg

## 历史版本号

- 0.1.0 (2026-06-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/winreg
- gem 安装: `gem install winreg`
- Bundler: `gem "winreg"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/winreg-0.1.0.gem
- 版本锁定: `gem "winreg", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
