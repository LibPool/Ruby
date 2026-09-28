# duration_time

**Tag**: testing, data

## 简介

This module provides a method for calculate the duration time from a date \nlike reg_date, which is usually used for statistics.\n\nUsage:\n\n  # Assume that today is 2013-07-07\n  require 'duration_time' \n  reg_time = Time.new(2011,8,2,0,0,0, "+08:00")\n  # You can use reg_time = Date.parse("2011-08-02") if you have included\n  # gem active_support!\n  duration_time( reg_time ) \n  # => {\n  #  :years=>[2011, 2012, 2013], \n  #  :months=>["2011-08", "2011-09", "2011-10", "2011-11", "2011-12", \n  #     "2012-01", "2012-02", "2012-03", "2012-04", "2012-05", "2012-06", \n  #     "2012-07", "2012-08", "2012-09", "2012-10", "2012-11", "2012-12", \n  #     "2013-01", "2013-02", "2013-03", "2013-04", "2013-05", "2013-06"], \n  #  :quarters=>["2011-09", "2011-12", "2012-03", "2012-06", "2012-09", \n  #     "2012-12", "2013-03", "2013-06"]\n  # }\n\nAnd you can specify default parameter `include_this_month_of_this_year = true`\nif you want to include this month of this year. Default value is `false`.\n

## 官网

- 主页: https://github.com/debbbbie/duration_time
- 文档: https://www.rubydoc.info/gems/duration_time/1.0.1
- RubyGems: https://rubygems.org/gems/duration_time

## 历史版本号

- 1.0.1 (2013-08-12)
- 1.0.0 (2013-08-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/duration_time
- gem 安装: `gem install duration_time`
- Bundler: `gem "duration_time"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/duration_time-1.0.1.gem
- 版本锁定: `gem "duration_time", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
