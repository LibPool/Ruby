# ekylibre-ofx-parser

**Tag**: web, testing, networking, template, tooling

## 简介

== DESCRIPTION:

ofx-parser is a ruby library to parse a realistic subset of the lengthy OFX 1.x specification.

== FEATURES/PROBLEMS:

* Reads OFX responses - i.e. those downloaded from financial institutions and
  puts it into a usable object graph.
* Supports the 3 main message sets: banking, credit card and investment
  accounts, as well as the required 'sign on' set.
* Knows about SIC codes - if your institution provides them.
  See http://www.eeoc.gov/stats/jobpat/siccodes.html
* Monetary amounts can be retrieved either as a raw string, or in pennies.
* Supports OFX timestamps.

## 官网

- 主页: https://github.com/ekylibre/ofx-parser
- 文档: https://www.rubydoc.info/gems/ekylibre-ofx-parser/1.2.2
- RubyGems: https://rubygems.org/gems/ekylibre-ofx-parser

## 历史版本号

- 1.2.2 (2017-06-06)
- 1.2.1 (2017-06-06)
- 1.2.0 (2017-05-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/ekylibre-ofx-parser
- gem 安装: `gem install ekylibre-ofx-parser`
- Bundler: `gem "ekylibre-ofx-parser"`
- 最新版本: 1.2.2
- 最新版归档: https://rubygems.org/downloads/ekylibre-ofx-parser-1.2.2.gem
- 版本锁定: `gem "ekylibre-ofx-parser", "~> 1.2.2"`
- 中央仓库: https://rubygems.org/
