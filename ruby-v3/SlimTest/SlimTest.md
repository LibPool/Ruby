# SlimTest

**Tag**: testing, filesystem

## 简介

ZenTest provides 4 different tools: zentest, unit_diff, autotest, and
multiruby.

ZenTest scans your target and unit-test code and writes your missing
code based on simple naming rules, enabling XP at a much quicker
pace. ZenTest only works with Ruby and Test::Unit. Nobody uses this
tool anymore but it is the package namesake, so it stays.

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

## 官网

- 主页: https://github.com/seattlerb/zentest
- RubyGems: https://rubygems.org/gems/SlimTest

## 历史版本号

- 4.6.1.1 (2011-08-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/SlimTest
- gem 安装: `gem install SlimTest`
- Bundler: `gem "SlimTest"`
- 最新版本: 4.6.1.1
- 最新版归档: https://rubygems.org/downloads/SlimTest-4.6.1.1.gem
- 版本锁定: `gem "SlimTest", "~> 4.6.1.1"`
- 中央仓库: https://rubygems.org/
