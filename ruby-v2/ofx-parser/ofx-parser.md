# ofx-parser

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

- 主页: http://ofx-parser.rubyforge.org/
- RubyGems: https://rubygems.org/gems/ofx-parser

## 历史版本号

- 1.1.0 (2011-12-12)
- 1.0.1 (2009-07-25)
- 1.0.0 (2009-07-25)
- 1.0.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/ofx-parser
- gem 安装: `gem install ofx-parser`
- Bundler: `gem "ofx-parser"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/ofx-parser-1.1.0.gem
- 版本锁定: `gem "ofx-parser", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
