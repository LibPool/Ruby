# winproc

**Tag**: cli

## 简介

winproc is a native extension for controlling Windows processes the way the
OS intends: argv-array spawning with exact quoting and per-handle inheritance
(PROC_THREAD_ATTRIBUTE_HANDLE_LIST), job objects with kill-on-close so a
spawned tree can never outlive you (even across a crash), atomic job
placement at creation, ConPTY pseudoconsoles for real interactive terminal
I/O, and elevation helpers (elevated?/admin?, ShellExecuteEx "runas",
scoped token privileges). Blocking waits release the GVL and cooperate with
a fiber scheduler. Windows MSVC (mswin) Ruby only.

## 官网

- 主页: https://github.com/main-path/winproc
- 更新日志: https://github.com/main-path/winproc/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/winproc/issues
- RubyGems: https://rubygems.org/gems/winproc

## 历史版本号

- 0.1.0 (2026-06-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/winproc
- gem 安装: `gem install winproc`
- Bundler: `gem "winproc"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/winproc-0.1.0.gem
- 版本锁定: `gem "winproc", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
