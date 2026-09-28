# startat

**Tag**: testing

## 简介

StartAt is a simple class for future code execution.  It is designed
to execute a block of code at a specific point in time in the future.

StartAt works by spawning a new thread, determining how long it must wait (in 
seconds) until the future date and time is reached, calling sleep with the
exact number of seconds to wait, and then executing the code block.

StartAt was derived from a script written to post schedule information to
Twitter for a symposium. The schedule robot posted event details exactly
five minutes in advance of the event.

## 官网

- 主页: http://startat.rubyforge.org/
- RubyGems: https://rubygems.org/gems/startat

## 历史版本号

- 0.1.0 (2009-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/startat
- gem 安装: `gem install startat`
- Bundler: `gem "startat"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/startat-0.1.0.gem
- 版本锁定: `gem "startat", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
