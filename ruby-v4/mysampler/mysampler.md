# mysampler

**Tag**: database, testing, filesystem, data

## 简介

MySampler is a tool written in ruby to poll SHOW GLOBAL STATUS in MySQL and output the values to either a CSV or graphite/carbon. The interval at which the polling occurs can be specified and the output can be either the absolute or relative values, so you can see change over time. If logging to CSV, the a date stamp is appended to the CSV file and it is rotated hourly (to be configurable later).

## 官网

- 主页: https://github.com/9minutesnooze/mysampler
- 文档: https://www.rubydoc.info/gems/mysampler/0.0.2
- RubyGems: https://rubygems.org/gems/mysampler

## 历史版本号

- 0.0.2 (2014-04-29)
- 0.0.1 (2014-04-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/mysampler
- gem 安装: `gem install mysampler`
- Bundler: `gem "mysampler"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/mysampler-0.0.2.gem
- 版本锁定: `gem "mysampler", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
