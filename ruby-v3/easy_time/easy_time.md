# easy_time

**Tag**: library

## 简介

A class that wraps the Time class and makes it easy to work with most
known time values, including various time strings, automatically
converting them to Time values, and perform tolerant comparisons.
Several time classes, and the String class, are extended with the
".easy_time" method to perform an auto-conversion.  A tolerant comparison
allows for times from differing systems to be compared, even when the
systems are out of sync, using the relationship operators and methods
like "newer?", "older?", "same?" and "between?".  A tolerant comparison
for equality is where the difference of two values is less than the
tolerance value (1 minute by default).  The tolerance can be configured,
even set to zero.  Finally, all of the Time class and instance methods
are available on the EasyTime class and instances.

## 官网

- 主页: https://github.com/aks/easy_time
- RubyGems: https://rubygems.org/gems/easy_time

## 历史版本号

- 1.0.1 (2024-02-27)
- 1.0.0 (2024-02-27)
- 0.2.2 (2024-01-19)
- 0.2.1 (2020-04-27)
- 0.2.0 (2020-04-27)
- 0.1.2 (2020-04-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/easy_time
- gem 安装: `gem install easy_time`
- Bundler: `gem "easy_time"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/easy_time-1.0.1.gem
- 版本锁定: `gem "easy_time", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
