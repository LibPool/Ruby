# minitest

**Tag**: web, testing, tooling

## 简介

minitest provides a complete suite of testing facilities supporting
TDD, BDD, and benchmarking.

    "I had a class with Jim Weirich on testing last week and we were
     allowed to choose our testing frameworks. Kirk Haines and I were
     paired up and we cracked open the code for a few test
     frameworks...

     I MUST say that minitest is *very* readable / understandable
     compared to the 'other two' options we looked at. Nicely done and
     thank you for helping us keep our mental sanity."

    -- Wayne E. Seguin

minitest/test is a small and incredibly fast unit testing framework.
It provides a rich set of assertions to make your tests clean and
readable.

minitest/spec is a functionally complete spec engine. It hooks onto
minitest/test and seamlessly bridges test assertions over to spec
expectations.

minitest/benchmark is an awesome way to assert the performance of your
algorithms in a repeatable manner. Now you can assert that your newb
co-worker doesn't replace your linear algorithm with an exponential
one!

minitest/pride shows pride in testing and adds coloring to your test
output. I guess it is an example of how to write IO pipes too. :P

minitest/test is meant to have a clean implementation for language
implementors that need a minimal set of methods to bootstrap a working
test suite. For example, there is no magic involved for test-case
discovery.

    "Again, I can't praise enough the idea of a testing/specing
     framework that I can actually read in full in one sitting!"

    -- Piotr Szotkowski

Comparing to rspec:

    rspec is a testing DSL. minitest is ruby.

    -- Adam Hawkins, "Bow Before MiniTest"

minitest doesn't reinvent anything that ruby already provides, like:
classes, modules, inheritance, methods. This means you only have to
learn ruby to use minitest and all of your regular OO practices like
extract-method refactorings still apply.

== Features/Problems:

* minitest/autorun - the easy and explicit way to run all your tests.
* minitest/test - a very fast, simple, and clean test system.
* minitest/spec - a very fast, simple, and clean spec system.
* minitest/benchmark - an awesome way to assert your algorithm's performance.
* minitest/pride - show your pride in testing!
* minitest/test_task - a full-featured and clean rake task generator.
* Incredibly small and fast runner, but no bells and whistles.
* Written by squishy human beings. Software can never be perfect. We will all eventually die.

## 官网

- 主页: https://minite.st/
- 源码仓库: https://github.com/minitest/minitest
- 文档: https://docs.seattlerb.org/minitest
- 更新日志: https://github.com/minitest/minitest/blob/master/History.rdoc
- 问题追踪: https://github.com/minitest/minitest/issues
- RubyGems: https://rubygems.org/gems/minitest

## 历史版本号

- 6.0.6 (2026-05-01)
- 6.0.5 (2026-04-20)
- 6.0.4 (2026-04-14)
- 6.0.3 (2026-04-01)
- 6.0.2 (2026-02-23)
- 6.0.1 (2025-12-26)
- 6.0.0 (2025-12-17)
- 6.0.0.a1 (2025-12-16)
- 5.27.0 (2025-12-11)
- 5.26.2 (2025-11-18)
- 5.26.1 (2025-11-08)
- 5.26.0 (2025-10-08)
- 5.25.5 (2025-03-12)
- 5.25.4 (2024-12-04)
- 5.25.3 (2024-12-03)
- 5.25.2 (2024-11-21)
- 5.25.1 (2024-08-16)
- 5.25.0 (2024-08-14)
- 5.24.1 (2024-06-29)
- 5.24.0 (2024-06-19)
- 5.23.1 (2024-05-22)
- 5.23.0 (2024-05-15)
- 5.22.3 (2024-03-13)
- 5.22.2 (2024-02-07)
- 5.22.1 (2024-02-07)
- 5.22.0 (2024-02-05)
- 5.21.2 (2024-01-18)
- 5.21.1 (2024-01-12)
- 5.21.0 (2024-01-11)
- 5.20.0 (2023-09-06)
- 5.19.0 (2023-07-26)
- 5.18.1 (2023-06-16)
- 5.18.0 (2023-03-04)
- 5.17.0 (2023-01-01)
- 5.16.3 (2022-08-17)
- 5.16.2 (2022-07-03)
- 5.16.1 (2022-06-20)
- 5.16.0 (2022-06-15)
- 5.15.0 (2021-12-15)
- 5.14.4 (2021-02-24)
- 5.14.3 (2021-01-06)
- 5.14.2 (2020-09-01)
- 5.14.1 (2020-05-16)
- 5.14.0 (2020-01-12)
- 5.13.0 (2019-10-30)
- 5.12.2 (2019-09-29)
- 5.12.1 (2019-09-28)
- 5.12.0 (2019-09-22)
- 5.11.3 (2018-01-26)
- 5.11.2 (2018-01-25)
- 5.11.1 (2018-01-02)
- 5.11.0 (2018-01-01)
- 5.11.0b1 (2017-12-21)
- 5.10.3 (2017-07-21)
- 5.10.2 (2017-05-09)
- 5.10.1 (2016-12-02)
- 5.10.0 (2016-12-01)
- 5.9.1 (2016-09-26)
- 5.8.5 (2016-09-26)
- 5.9.0 (2016-05-16)
- 5.8.4 (2016-01-21)
- 5.8.3 (2015-11-17)
- 5.8.2 (2015-10-26)
- 5.8.1 (2015-09-23)
- 5.8.0 (2015-08-06)
- 5.7.0 (2015-05-27)
- 5.6.1 (2015-04-27)
- 5.6.0 (2015-04-13)
- 5.5.1 (2015-01-10)
- 5.5.0 (2014-12-12)
- 5.4.3 (2014-11-11)
- 5.4.2 (2014-09-26)
- 5.4.1 (2014-08-28)
- 5.4.0 (2014-07-07)
- 5.3.5 (2014-06-18)
- 5.3.4 (2014-05-15)
- 5.3.3 (2014-04-14)
- 5.3.2 (2014-04-02)
- 5.3.1 (2014-03-14)
- 5.3.0 (2014-02-26)
- 5.2.3 (2014-02-11)
- 5.2.2 (2014-01-22)
- 5.2.1 (2014-01-08)
- 5.2.0 (2013-12-14)
- 5.1.0 (2013-12-06)
- 5.0.8 (2013-09-21)
- 5.0.7 (2013-09-05)
- 5.0.6 (2013-06-28)
- 4.7.5 (2013-06-22)
- 5.0.5 (2013-06-21)
- 5.0.4 (2013-06-07)
- 5.0.3 (2013-05-30)
- 5.0.2 (2013-05-20)
- 5.0.1 (2013-05-15)
- 5.0.0 (2013-05-10)
- 4.7.4 (2013-05-01)
- 4.7.3 (2013-04-21)
- 4.7.2 (2013-04-18)
- 4.7.1 (2013-04-10)
- 4.7.0 (2013-03-18)
- 4.6.2 (2013-02-28)
- 4.6.1 (2013-02-15)
- 4.6.0 (2013-02-07)
- 4.5.0 (2013-01-23)
- 4.4.0 (2013-01-08)
- 4.3.3 (2012-12-07)
- 4.3.2 (2012-11-28)
- 4.3.1 (2012-11-23)
- 4.3.0 (2012-11-17)
- 4.2.0 (2012-11-02)
- 4.1.0 (2012-10-05)
- 4.0.0 (2012-09-29)
- 3.5.0 (2012-09-21)
- 3.4.0 (2012-09-05)
- 3.3.0 (2012-07-27)
- 3.2.0 (2012-06-26)
- 3.1.0 (2012-06-13)
- 3.0.1 (2012-05-24)
- 3.0.0 (2012-05-09)
- 2.12.1 (2012-04-11)
- 2.12.0 (2012-04-04)
- 2.11.4 (2012-03-21)
- 2.11.3 (2012-03-01)
- 2.11.2 (2012-02-15)
- 2.11.1 (2012-02-01)
- 2.11.0 (2012-01-25)
- 2.10.1 (2012-01-18)
- 2.10.0 (2011-12-21)
- 2.9.1 (2011-12-14)
- 2.9.0 (2011-12-08)
- 2.8.1 (2011-11-17)
- 2.8.0 (2011-11-09)
- 2.7.0 (2011-10-26)
- 2.6.2 (2011-10-19)
- 2.6.1 (2011-09-28)
- 2.6.0 (2011-09-13)
- 2.5.1 (2011-08-27)
- 2.5.0 (2011-08-19)
- 2.4.0 (2011-08-10)
- 2.3.1 (2011-06-23)
- 2.3.0 (2011-06-18)
- 2.2.2 (2011-06-01)
- 2.2.1 (2011-06-01)
- 2.2.0 (2011-06-01)
- 2.1.0 (2011-04-11)
- 2.0.2 (2010-12-25)
- 2.0.1 (2010-12-15)
- 2.0.0 (2010-11-11)
- 1.7.2 (2010-09-23)
- 1.7.1 (2010-09-01)
- 1.7.0 (2010-07-16)
- 1.6.0 (2010-03-28)
- 1.5.0 (2010-01-06)
- 1.4.0 (2009-08-05)
- 1.4.1 (2009-08-05)
- 1.4.2 (2009-08-05)
- 1.3.1 (2009-07-25)
- 1.3.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/minitest
- gem 安装: `gem install minitest`
- Bundler: `gem "minitest"`
- 最新版本: 6.0.6
- 最新版归档: https://rubygems.org/downloads/minitest-6.0.6.gem
- 版本锁定: `gem "minitest", "~> 6.0.6"`
- 中央仓库: https://rubygems.org/
