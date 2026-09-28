# ZenTest

**Tag**: testing, tooling, filesystem

## 简介

ZenTest provides 4 different tools: zentest, unit_diff, autotest, and
multiruby.

zentest scans your target and unit-test code and writes your missing
code based on simple naming rules, enabling XP at a much quicker pace.
zentest only works with Ruby and Minitest or Test::Unit. There is
enough evidence to show that this is still proving useful to users, so
it stays.

unit_diff is a command-line filter to diff expected results from
actual results and allow you to quickly see exactly what is wrong.
Do note that minitest 2.2+ provides an enhanced assert_equal obviating
the need for unit_diff

autotest is a continous testing facility meant to be used during
development. As soon as you save a file, autotest will run the
corresponding dependent tests.

multiruby runs anything you want on multiple versions of ruby. Great
for compatibility checking! Use multiruby_setup to manage your
installed versions.

*NOTE:* The next major release of zentest will not include autotest
(use minitest-autotest instead) and multiruby will use rbenv /
ruby-build for version management.

## 官网

- 主页: https://github.com/seattlerb/zentest
- RubyGems: https://rubygems.org/gems/ZenTest

## 历史版本号

- 4.12.2 (2024-07-03)
- 4.12.1 (2022-01-17)
- 4.12.0 (2019-09-23)
- 4.11.2 (2019-01-02)
- 4.11.1 (2016-06-13)
- 4.11.0 (2014-09-27)
- 4.10.1 (2014-07-07)
- 4.10.0 (2014-04-23)
- 4.9.5 (2013-11-02)
- 4.9.4 (2013-09-21)
- 4.9.3 (2013-08-13)
- 4.9.2 (2013-05-30)
- 4.9.1 (2013-04-18)
- 4.9.0 (2013-02-07)
- 4.8.4 (2013-01-23)
- 4.8.3 (2012-12-07)
- 4.8.2 (2012-07-27)
- 4.8.1 (2012-06-01)
- 4.8.0 (2012-05-04)
- 4.7.0 (2012-03-15)
- 4.6.2 (2011-08-24)
- 4.6.1 (2011-08-12)
- 4.6.0 (2011-07-23)
- 4.5.0 (2011-02-18)
- 4.4.2 (2010-12-10)
- 4.4.1 (2010-12-02)
- 4.4.0 (2010-09-01)
- 4.3.3 (2010-06-17)
- 4.3.2 (2010-06-03)
- 4.3.1 (2010-03-30)
- 4.3.0 (2010-03-28)
- 4.2.1 (2009-12-10)
- 4.2.0 (2009-12-09)
- 3.0.0 (2009-09-10)
- 3.1.0 (2009-08-18)
- 3.2.0 (2009-08-18)
- 3.3.0 (2009-08-18)
- 3.4.0 (2009-08-18)
- 3.4.1 (2009-08-18)
- 3.4.2 (2009-08-18)
- 3.4.3 (2009-08-18)
- 3.5.1 (2009-08-18)
- 3.5.2 (2009-08-18)
- 3.6.0 (2009-08-18)
- 3.6.1 (2009-08-18)
- 3.7.0 (2009-08-18)
- 3.7.1 (2009-08-18)
- 3.7.2 (2009-08-18)
- 3.8.0 (2009-08-18)
- 3.9.0 (2009-08-18)
- 3.9.1 (2009-08-18)
- 3.9.2 (2009-08-18)
- 3.9.3 (2009-08-18)
- 3.10.0 (2009-08-18)
- 3.11.0 (2009-08-18)
- 3.11.1 (2009-08-18)
- 4.0.0 (2009-08-18)
- 4.1.0 (2009-08-18)
- 4.1.1 (2009-08-18)
- 4.1.2 (2009-08-18)
- 4.1.3 (2009-08-18)
- 4.1.4 (2009-08-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/ZenTest
- gem 安装: `gem install ZenTest`
- Bundler: `gem "ZenTest"`
- 最新版本: 4.12.2
- 最新版归档: https://rubygems.org/downloads/ZenTest-4.12.2.gem
- 版本锁定: `gem "ZenTest", "~> 4.12.2"`
- 中央仓库: https://rubygems.org/
