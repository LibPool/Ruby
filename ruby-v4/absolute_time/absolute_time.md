# absolute_time

**Tag**: testing

## 简介

This gem provides a monotonically increasing timer to permit safe measurement of time intervals.

Using Time.now for measuring intervals is not reliable (and sometimes unsafe) because the
system clock may be stepped forwards or backwards between the two measurements, or may be
running slower or faster than real time in order to effect clock synchronization with UTC.

The module uses OS-specific functions such as mach_absolute_time() and clock_gettime() to
access the system tick counter.  The time values returned by this module cannot be interpreted
as real time clock values; they are only useful for comparison with another time value from
this module.

## 官网

- 主页: https://github.com/bwbuchanan/absolute_time
- 源码仓库: https://github.com/bwbuchanan/absolute_time/
- 文档: http://rubydoc.info/github/bwbuchanan/absolute_time/master/AbsoluteTime
- 问题追踪: https://github.com/bwbuchanan/absolute_time/issues
- RubyGems: https://rubygems.org/gems/absolute_time

## 历史版本号

- 1.0.0 (2013-02-06)
- 0.1.0 (2011-09-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/absolute_time
- gem 安装: `gem install absolute_time`
- Bundler: `gem "absolute_time"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/absolute_time-1.0.0.gem
- 版本锁定: `gem "absolute_time", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
