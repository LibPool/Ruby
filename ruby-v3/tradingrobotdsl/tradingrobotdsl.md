# tradingrobotdsl

**Tag**: web, testing

## 简介

This is an alpha test quality release. I specifically DO NOT recommend that it be used for live trading under any circumstances. It has not been tested. I am releasing it in the hopes that the many eyes of the community will help with enhancing it, so that we all will have a robust and reliable library to use.  == FEATURES/PROBLEMS:  * get quotes from opentick servers * simple average indicator realized :) * order placement (buy/sell) doesn't work  == SYNOPSIS:  robot do   login 'test_opentick', '123123' history :duration =&gt; 300, :from =&gt; Time.now-10*24*3600, :to =&gt; Time.now query MSFT do   if (avg MSFT, 9)/(avg MSFT, 25) - 1 &gt; 0.5   puts &quot;buy MSFT&quot; end   if (avg MSFT, 9)/(avg MSFT, 25) - 1 &lt; - 0.5   puts &quot;sell MSFT&quot; end   end # query   end # robot

## 官网

- 主页: http://www.tradeindexfuture.com
- RubyGems: https://rubygems.org/gems/tradingrobotdsl

## 历史版本号

- 0.0.2 (2009-07-25)
- 0.0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/tradingrobotdsl
- gem 安装: `gem install tradingrobotdsl`
- Bundler: `gem "tradingrobotdsl"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/tradingrobotdsl-0.0.2.gem
- 版本锁定: `gem "tradingrobotdsl", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
