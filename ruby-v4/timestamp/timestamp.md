# timestamp

**Tag**: web, networking

## 简介

== Time.timestamp

Defines <tt>Time::timestamp</tt> and <tt>Time::unix_timestamp</tt>.

See the original discussion at {Ruby-Lang}[https://bugs.ruby-lang.org/issues/8096]

:call-seq:
  Time::timestamp  -> Integer

Returns a nanosecond-precision timestamp from the system's monotonic
clock. Note that the resolution of the measured time is system-
dependent (i.e. while the value displayed is always an integer number
of nanoseconds, the values may not necessarily change in increments of
exactly one).

This time value does not correlate to any absolute, real-world time
system; it is only useful for measuring relative (or elapsed) times at
a high granularity.  For example, benchmark measurements.

:call-seq:
  Time::unix_timestamp  -> Integer
  Time::unix_time       -> Integer

Returns the current real-world time as a whole number of seconds since
the Epoch (1-Jan-1970).

:call-seq:
  Time::unix_microtime  -> Float

Returns the current real-world time as a floating-point number of
seconds since the Epoch (1-Jan-1970).

## 官网

- 主页: http://phluid61.github.com/timestamp-gem/
- 源码仓库: https://github.com/phluid61/timestamp-gem
- 文档: https://github.com/phluid61/timestamp-gem#readme
- 问题追踪: https://github.com/phluid61/timestamp-gem/issues
- RubyGems: https://rubygems.org/gems/timestamp

## 历史版本号

- 1.0.2 (2013-07-19)
- 1.0.1 (2013-04-13)
- 1.0.0 (2013-03-25)
- 0.3.0 (2013-03-17)
- 0.2.0 (2013-03-15)
- 0.1.0 (2013-03-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/timestamp
- gem 安装: `gem install timestamp`
- Bundler: `gem "timestamp"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/timestamp-1.0.2.gem
- 版本锁定: `gem "timestamp", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
