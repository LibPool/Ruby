# remind-rb

**Tag**: tooling, filesystem

## 简介

Remind is a calendar program with a real expression language behind it: a
Hebrew calendar, moon phases, sunrise and sunset, and date arithmetic that
knows about weekdays, holidays and OMITted days. All of it is C, and all of
it is reachable.

remind-rb builds Remind's own sources into a shared library and binds them
with Fiddle, so `moonphase(today())` and `sunrise('2027-06-21')` are Ruby
calls rather than a shell-out and a parse of the output. Dates come back as
Date objects, times as minutes, strings as strings.

The Remind sources are vendored beside the gem, so the library binds the
version it was built against rather than whatever is on the PATH.

## 官网

- 主页: https://dianne.skoll.ca/projects/remind/
- 文档: https://www.rubydoc.info/gems/remind-rb/6.2.10.1
- RubyGems: https://rubygems.org/gems/remind-rb

## 历史版本号

- 6.2.10.1-x86_64-linux (2026-08-19)
- 6.2.10.1-x86_64-linux-musl (2026-08-19)
- 6.2.10.1-x86_64-darwin (2026-08-19)
- 6.2.10.1-arm64-darwin (2026-08-19)
- 6.2.10.1-arm-linux (2026-08-19)
- 6.2.10.1-aarch64-linux (2026-08-19)
- 6.2.10.1-aarch64-linux-musl (2026-08-19)
- 6.2.10.1 (2026-08-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/remind-rb
- gem 安装: `gem install remind-rb`
- Bundler: `gem "remind-rb"`
- 最新版本: 6.2.10.1
- 最新版归档: https://rubygems.org/downloads/remind-rb-6.2.10.1.gem
- 版本锁定: `gem "remind-rb", "~> 6.2.10.1"`
- 中央仓库: https://rubygems.org/
