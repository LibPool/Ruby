# rt_watchdog

**Tag**: web

## 简介

Request Tracker's rt-server.fcgi seems to have a memory leak and will
    continue to consume memory indefinitely. The rt_watchdog daemon will
    monitor the process's memory consumption and whether the process is running
    and restart or start it if it has hung or crashed.

## 官网

- 主页: https://github.com/sidewaysmilk/rt_watchdog
- RubyGems: https://rubygems.org/gems/rt_watchdog

## 历史版本号

- 1.0.0 (2012-01-20)
- 1.0.0.pre2 (2012-01-20)
- 1.0.0.pre.1 (2012-01-20)
- 1.0.0.pre1 (2012-01-20)
- 1.0.0.pre (2012-01-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/rt_watchdog
- gem 安装: `gem install rt_watchdog`
- Bundler: `gem "rt_watchdog"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/rt_watchdog-1.0.0.gem
- 版本锁定: `gem "rt_watchdog", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
