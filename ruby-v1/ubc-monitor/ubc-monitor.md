# ubc-monitor

**Tag**: web, filesystem

## 简介

ubc_monitor monitors resource usage in virtual servers run by OpenVz.  Monitor /proc/user_beancounters and send an email to the systems administrator if failcnt has increased since last time ubc_monitor was run.  ubc_monitor uses a file (by default ~/.ubc_monitor) to keep track of user_beancounter fail counts. When running without this file (such as the first run) any fail count except 0 will be reported.

## 官网

- 主页: http://www.cjohansen.no/projects/ubc_monitor
- RubyGems: https://rubygems.org/gems/ubc-monitor

## 历史版本号

- 1.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/ubc-monitor
- gem 安装: `gem install ubc-monitor`
- Bundler: `gem "ubc-monitor"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/ubc-monitor-1.1.0.gem
- 版本锁定: `gem "ubc-monitor", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
