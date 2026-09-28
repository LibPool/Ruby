# flay

**Tag**: filesystem

## 简介

Flay analyzes code for structural similarities. Differences in literal
values, variable, class, method names, whitespace, programming style,
braces vs do/end, etc are all ignored. Making this totally rad.

== Features/Problems:

* Reports differences at any level of code.
* Adds a score multiplier to identical nodes.
* Differences in literal values, variable, class, and method names are ignored.
* Differences in whitespace, programming style, braces vs do/end, etc are ignored.
* Works across files.
  * Add the flay-persistent plugin to work across large/many projects.
* Run --diff to see an N-way diff of the code.
* Provides conservative (default) and --liberal pruning options.
* Provides --fuzzy duplication detection.
* Language independent: Plugin system allows other languages to be flayed.
  * Ships with .rb and .erb.
  * javascript and others will be available separately.
* Includes FlayTask for Rakefiles.
* Uses path_expander, so you can use:
  * dir_arg -- expand a directory automatically
  * @file_of_args -- persist arguments in a file
  * -path_to_subtract -- ignore intersecting subsets of files/directories
* Skips files matched via patterns in .flayignore (subset format of .gitignore).
* Totally rad.

## 官网

- 主页: http://ruby.sadi.st/
- 源码仓库: https://github.com/seattlerb/flay
- 文档: http://docs.seattlerb.org/flay/
- RubyGems: https://rubygems.org/gems/flay

## 历史版本号

- 2.14.4 (2026-04-14)
- 2.14.3 (2026-03-23)
- 2.14.2 (2026-01-07)
- 2.14.1 (2025-12-21)
- 2.14.0 (2025-12-11)
- 2.13.3 (2024-05-22)
- 2.13.2 (2024-02-05)
- 2.13.1 (2023-07-20)
- 2.13.0 (2022-04-09)
- 2.12.1 (2019-10-09)
- 2.12.0 (2018-04-30)
- 2.11.0 (2018-04-05)
- 2.10.0 (2017-07-17)
- 2.9.0 (2017-04-14)
- 2.8.1 (2016-08-24)
- 2.8.0 (2016-05-16)
- 2.7.0 (2016-01-21)
- 2.6.1 (2015-01-30)
- 2.6.0 (2015-01-10)
- 2.5.0 (2014-05-30)
- 2.4.0 (2013-07-24)
- 2.3.1 (2013-07-11)
- 2.3.0 (2013-05-10)
- 2.2.0 (2013-04-10)
- 2.1.0 (2013-02-14)
- 2.0.1 (2012-12-19)
- 2.0.0 (2012-11-02)
- 2.0.0.b1 (2012-08-07)
- 1.4.3 (2011-08-10)
- 1.4.2 (2011-02-19)
- 1.4.1 (2010-09-02)
- 1.4.0 (2009-08-18)
- 1.3.0 (2009-08-05)
- 1.1.0 (2009-07-25)
- 1.0.0 (2009-07-25)
- 1.2.1 (2009-07-25)
- 1.2.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/flay
- gem 安装: `gem install flay`
- Bundler: `gem "flay"`
- 最新版本: 2.14.4
- 最新版归档: https://rubygems.org/downloads/flay-2.14.4.gem
- 版本锁定: `gem "flay", "~> 2.14.4"`
- 中央仓库: https://rubygems.org/
