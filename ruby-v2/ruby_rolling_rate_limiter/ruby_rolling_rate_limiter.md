# ruby_rolling_rate_limiter

**Tag**: database

## 简介

Often Redis is used for rate limiting purposes. Usually the rate limit packages available count how many times something happens on a certain second or a certain minute. When the clock ticks to the next minute, rate limit counter is reset back to the zero. This might be problematic if you are looking to limit rates where hits per integration time window is very low. If you are looking to limit to the five hits per minute, in one time window you get just one hit and six in another, even though the average over two minutes is 3.5. This package allows you to implement a correct rolling window of threshold that's backed by ATOMIC storage in Redis meaning you can use this implementation across multiple machines and processes.

## 官网

- 主页: https://github.com/logicsaas/ruby_rolling_rate_limiter
- 文档: https://www.rubydoc.info/gems/ruby_rolling_rate_limiter/0.1.5
- RubyGems: https://rubygems.org/gems/ruby_rolling_rate_limiter

## 历史版本号

- 0.1.5 (2016-04-18)
- 0.1.4 (2016-04-18)
- 0.1.3 (2016-04-14)
- 0.1.1 (2016-04-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruby_rolling_rate_limiter
- gem 安装: `gem install ruby_rolling_rate_limiter`
- Bundler: `gem "ruby_rolling_rate_limiter"`
- 最新版本: 0.1.5
- 最新版归档: https://rubygems.org/downloads/ruby_rolling_rate_limiter-0.1.5.gem
- 版本锁定: `gem "ruby_rolling_rate_limiter", "~> 0.1.5"`
- 中央仓库: https://rubygems.org/
