# funit

**Tag**: web, testing, networking, template, tooling, filesystem

## 简介

funit is a unit testing framework for Fortran.

Unit tests are written as Fortran fragments that use a small
set of testing-specific keywords and functions.  funit transforms
these fragments into valid Fortran code, compiles, links, and
runs them against the code under test.

funit is
{opinionated software}[http://www.oreillynet.com/pub/a/network/2005/08/30/ruby-rails-david-heinemeier-hansson.html],
which values convention over configuration. Specifically, funit requires,

* a Fortran 95 compiler,
* tests to be stored along side the code under test, and
* test files to be named appropriately.

## 官网

- 主页: https://rubygems.org/gems/funit
- 源码仓库: https://github.com/kleb/nasarb/tree/master/funit
- 问题追踪: https://github.com/kleb/nasarb/issues

## 历史版本号

- 0.12.4 (2016-02-11)
- 0.12.3 (2016-02-05)
- 0.11.1 (2009-11-02)
- 0.11.0 (2009-11-02)
- 0.10.3 (2009-10-06)
- 0.10.2 (2009-07-25)
- 0.10.1 (2009-07-25)
- 0.10.0 (2009-07-25)
- 0.9.4 (2009-07-25)
- 0.9.3 (2009-07-25)
- 0.9.2 (2009-07-25)
- 0.9.1 (2009-07-25)
- 0.9.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/funit
- gem 安装: `gem install funit`
- Bundler: `gem "funit"`
- 最新版本: 0.12.4
- 最新版归档: https://rubygems.org/downloads/funit-0.12.4.gem
- 版本锁定: `gem "funit", "~> 0.12.4"`
- 中央仓库: https://rubygems.org/
