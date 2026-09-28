# winlog

**Tag**: template

## 简介

winlog emits Windows ETW TraceLogging events from Ruby with no manifest, no
message DLL, no registry writes, and no elevation: register a provider by
name (standard ETW name-hashed GUID), then log runtime-dynamic events with
typed fields (UTF-8 text, binary, int64, double, boolean) plus levels,
keywords, opcodes, and explicit activity IDs for correlation. Events are
self-describing and decode in WPA, PerfView, and the inbox logman/tracerpt
with zero setup; when no session is listening, a log call is gated in native
code before field processing and costs about one Ruby method call. Built on
Microsoft's MIT-licensed TraceLoggingDynamic.h (vendored). Emit-only: events
go to ETW sessions, not the Windows Event Log. Windows MSVC (mswin) Ruby only.

## 官网

- 主页: https://github.com/main-path/winlog
- 更新日志: https://github.com/main-path/winlog/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/winlog/issues
- RubyGems: https://rubygems.org/gems/winlog

## 历史版本号

- 0.1.0 (2026-06-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/winlog
- gem 安装: `gem install winlog`
- Bundler: `gem "winlog"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/winlog-0.1.0.gem
- 版本锁定: `gem "winlog", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
