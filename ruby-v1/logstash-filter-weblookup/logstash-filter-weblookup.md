# logstash-filter-weblookup

**Tag**: web, database, filesystem, data

## 简介

This gem is a Logstash plugin. During filter it takes one or more fields and uses that as input to query additional information. The original purpose is to enrich IP addresses with matching subnet, netname and hostname, but it is generic so that any field can be looked up. The function is similar to the translate filter's dictionary lookup, which supports files and regex. The jdbc_streaming filter plugin is also very useful if the data resides in a database. This plugins features are web based lookups and redis caching, for fast lookups.

## 官网

- 主页: https://github.com/janmg/logstash-filter-weblookup
- 文档: https://www.rubydoc.info/gems/logstash-filter-weblookup/0.1.4
- RubyGems: https://rubygems.org/gems/logstash-filter-weblookup

## 历史版本号

- 0.1.4 (2021-05-21)
- 0.1.3 (2020-01-13)
- 0.1.2 (2019-11-19)
- 0.1.1 (2019-10-31)
- 0.1.0 (2019-05-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/logstash-filter-weblookup
- gem 安装: `gem install logstash-filter-weblookup`
- Bundler: `gem "logstash-filter-weblookup"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/logstash-filter-weblookup-0.1.4.gem
- 版本锁定: `gem "logstash-filter-weblookup", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
