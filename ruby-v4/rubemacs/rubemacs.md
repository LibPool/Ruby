# rubemacs

**Tag**: testing

## 简介

This package adds some additional assertions to Test::Unit::Assertions,
including:
* Assertions for all of the comparison operators
  (assert_greater_than, assert_less_than_or_equal_to,
  etc.).  Shorter aliases also are provided for these (assert_gt,
  assert_le, etc.).
* An assertion that verifies that a given block raises a specified exception
  with a specified message (assert_raise_message).
  This allows full testing of error messages.
* An assertion that verifies that a given block contains an assertion that
  fails (assert_fail), which can be used to test new assertions.

## 官网

- 主页: http://rubemacs.rubyforge.org
- RubyGems: https://rubygems.org/gems/rubemacs

## 历史版本号

- 1.0.0 (2009-10-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/rubemacs
- gem 安装: `gem install rubemacs`
- Bundler: `gem "rubemacs"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/rubemacs-1.0.0.gem
- 版本锁定: `gem "rubemacs", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
