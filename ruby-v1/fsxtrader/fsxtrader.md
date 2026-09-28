# fsxtrader

**Tag**: web, testing, networking, template, filesystem

## 简介

== FEATURES/PROBLEMS:  * Order types supported: buy, short, sell and cover * Pulls real-time stock quotes from Yahoo! Finance  == SYNOPSIS:  Fantasy Stock Exchange app on Facebook (by HedgeStop.com): http://apps.facebook.com/hedgestop/  As of this writing, the Fantasy Stock Exchange application on Facebook does not allow one to place stop-limit orders or otherwise automatically trigger a buy/sell or cover/short order based upon specified prices.  FSX Trader, when combined with a periodic cron job, can make these trades for you.  Simply configure your trades in the '~/.fsx_trader.yml' file and they will happen automatically whenever FSX Trader is run AND conditions for making a trade (as specified via the config file) have been met.  Note: fsxtrader of course depends upon the external HTML form variables of the FSX App and Facebook login page.  If these variables have changed, fsxtrader be temporarily broken until the gem can be updated.  A programmatic API into FSX would be ideal, but is currently not yet offered by HedgeStop.  == REQUIREMENTS:

## 官网

- 主页: http://fsxtrader.rubyforge.org
- RubyGems: https://rubygems.org/gems/fsxtrader

## 历史版本号

- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/fsxtrader
- gem 安装: `gem install fsxtrader`
- Bundler: `gem "fsxtrader"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/fsxtrader-1.0.0.gem
- 版本锁定: `gem "fsxtrader", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
