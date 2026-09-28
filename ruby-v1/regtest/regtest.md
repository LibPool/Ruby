# regtest

**Tag**: testing, filesystem, data

## 简介

This library supports a very simple way to do regression testing with Ruby. It
is not limited to Ruby projects you can use it also in other contexts where you
can extract data with Ruby.

You write Ruby scripts with samples. Run these and get the sample results as
results files besides your scripts. Check both the scripts and the results
files in you Source Code Management System (SCM). When you run the scrips on a
later (or even previous) version of your code a simple diff show you if and how
the changes in your code or environment impact the results of your samples.

This is not a replacement for unit testing but a complement: You can produce a
lot of samples with a small amount of Ruby code (e.g. a large number of
combinations of data).

## 官网

- 主页: https://github.com/janfri/regtest
- 文档: https://www.rubydoc.info/gems/regtest/2.5.0
- RubyGems: https://rubygems.org/gems/regtest

## 历史版本号

- 2.5.0 (2024-11-23)
- 2.4.1 (2024-09-14)
- 2.4.0 (2024-09-13)
- 2.3.0 (2024-09-12)
- 2.2.1 (2021-02-24)
- 2.2.0 (2019-12-20)
- 2.1.1 (2019-03-26)
- 2.1.0 (2019-03-04)
- 2.0.0 (2017-09-22)
- 2.0.0.pre (2017-09-12)
- 1.1.0 (2017-08-29)
- 1.0.0 (2017-08-19)
- 0.5.3 (2016-01-06)
- 0.5.2 (2016-01-06)
- 0.5.0 (2015-10-13)
- 0.4.0 (2014-03-18)
- 0.3.0 (2014-02-07)
- 0.2.0 (2014-01-30)
- 0.1.0 (2014-01-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/regtest
- gem 安装: `gem install regtest`
- Bundler: `gem "regtest"`
- 最新版本: 2.5.0
- 最新版归档: https://rubygems.org/downloads/regtest-2.5.0.gem
- 版本锁定: `gem "regtest", "~> 2.5.0"`
- 中央仓库: https://rubygems.org/
