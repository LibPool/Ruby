# tribble-control

**Tag**: cli

## 简介

Switches the ports of a USB hub -- an ExSYS 16-port managed hub
over its internal FT232 line, or any hub that switches its own
ports, through hub-class requests (FreeBSD for now) -- and for
the boards on it speaks SWD through openocd and reads their
consoles over USB CDC.  Which board sits on which port, and
which ports must never lose power, is read from a
configuration, so the tool switches the bench it is told about
and nothing else.  What a console's lines mean is left to a
tally loaded at run time.

## 官网

- 主页: https://github.com/sdalu/tribble-control
- RubyGems: https://rubygems.org/gems/tribble-control

## 历史版本号

- 0.4.4 (2026-10-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/tribble-control
- gem 安装: `gem install tribble-control`
- Bundler: `gem "tribble-control"`
- 最新版本: 0.4.4
- 最新版归档: https://rubygems.org/downloads/tribble-control-0.4.4.gem
- 版本锁定: `gem "tribble-control", "~> 0.4.4"`
- 中央仓库: https://rubygems.org/
