# winloop

**Tag**: networking, tooling

## 简介

winloop is a Ruby Fiber::Scheduler built on Win32 I/O Completion Ports. It
makes ordinary socket I/O, sleeps, timeouts and Mutex/Queue/Thread#join run
cooperatively on a single thread — the async-runtime story that has always
been weak on Windows, done the way libuv/mio/wepoll do it: readiness over an
IOCP via \Device\Afd polling, with recv/send driven by the completion port.
Requires a native Windows MSVC (mswin) build of Ruby.

## 官网

- 主页: https://github.com/main-path/winloop
- 更新日志: https://github.com/main-path/winloop/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/main-path/winloop/issues
- RubyGems: https://rubygems.org/gems/winloop

## 历史版本号

- 0.2.0 (2026-06-28)
- 0.1.0 (2026-05-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/winloop
- gem 安装: `gem install winloop`
- Bundler: `gem "winloop"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/winloop-0.2.0.gem
- 版本锁定: `gem "winloop", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
