# logstash-input-multirss

**Tag**: web, serialization, networking

## 简介

This plugin get the feed rss content (being able to use keywords to get the feed) , the params are: 
                      1) multi_feed => [array] URI parent with more rss links inside , something like this: http://rss.elmundo.es/rss/  
                      2) one_feed => [array] (optionally) childs URIS with XML content inside , something like this: http://estaticos.elmundo.es/elmundo/rss/portada.xml 
                      3) blacklist => [array] (optionally) strings , links, text ... what you dont want explored
                      4) Interval => [int] Set the Stoppable_sleep interval for the pipe
                      5) keywords => [array] if you use this parameter will only compile those news that contain in any of its attributes a word from this array

## 官网

- 主页: https://github.com/felixramirezgarcia/logstash-input-multirss
- 文档: https://www.rubydoc.info/gems/logstash-input-multirss/1.2.0
- RubyGems: https://rubygems.org/gems/logstash-input-multirss

## 历史版本号

- 1.2.0 (2018-09-06)
- 1.1.0 (2018-08-27)
- 1.0.5 (2018-08-24)
- 1.0.4 (2018-08-24)
- 1.0.3 (2018-08-17)
- 1.0.2 (2018-08-17)
- 1.0.1 (2018-08-16)
- 1.0.0 (2018-08-14)
- 0.1.1 (2018-08-07)
- 0.1.0 (2018-08-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/logstash-input-multirss
- gem 安装: `gem install logstash-input-multirss`
- Bundler: `gem "logstash-input-multirss"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/logstash-input-multirss-1.2.0.gem
- 版本锁定: `gem "logstash-input-multirss", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
