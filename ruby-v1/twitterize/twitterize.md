# twitterize

**Tag**: web, database, testing, filesystem, data

## 简介

Twitterize is a quick and dirty hack I did in a few hours to play with the Twitter API (seriously, there are no tests and I'm sure there is code crude enough in there to make you recant any friendship we might have). It allows you to take any number of RSS feeds and post them to one or more Twitter accounts. An example of this is how various RSS feeds from the New York Times are sent to twitter accounts nytimes, nyt_arts, nyt_biz, etc. This is accomplished via a command-line script that requires a separate configuration file (see below). Since Twitter is a rapidly growing (read somewhat flaky) service, twitterize also uses a database to store twitters to be posted and recover later if twitter is down. This also allows the app to retain feed GUIDs and avoid duplicate posts.

## 官网

- 主页: http://www.zenspider.com/ZSS/Products/twitterize/
- RubyGems: https://rubygems.org/gems/twitterize

## 历史版本号

- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/twitterize
- gem 安装: `gem install twitterize`
- Bundler: `gem "twitterize"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/twitterize-1.0.0.gem
- 版本锁定: `gem "twitterize", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
