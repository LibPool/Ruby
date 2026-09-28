# pmdtester

**Tag**: testing

## 简介

A regression testing tool ensure that new problems and unexpected behaviors will not be introduced to PMD project after fixing an issue
and new rules work as expected.

== Features/Problems:

The diff report can be generated according to the base and patch branch of PMD
on a list of standard projects (e.g. Spring Framework, Checkstyle, OpenJDK, etc.).

Rule violations and code duplications are compared to report, which are new, removed or changed.

While executing PMD, JDK Flight Recorder (jfr) is enabled and a recording is created. This allows to investigate
performance and memory issues afterwards.

## 官网

- 主页: https://pmd.github.io
- 源码仓库: https://github.com/pmd/pmd-regression-tester
- 问题追踪: https://github.com/pmd/pmd-regression-tester/issues
- RubyGems: https://rubygems.org/gems/pmdtester

## 历史版本号

- 1.7.0 (2026-04-16)
- 1.6.2 (2025-10-24)
- 1.6.1 (2025-09-19)
- 1.6.0 (2025-07-25)
- 1.5.5 (2023-11-16)
- 1.5.4 (2023-05-27)
- 1.5.3 (2022-11-25)
- 1.5.2 (2022-10-20)
- 1.5.1 (2022-05-12)
- 1.5.0 (2022-05-06)
- 1.4.1 (2022-04-12)
- 1.4.0 (2022-03-24)
- 1.3.0 (2021-12-17)
- 1.2.0 (2021-06-20)
- 1.1.2 (2021-04-20)
- 1.1.1 (2021-01-15)
- 1.1.0 (2020-12-05)
- 1.0.1 (2020-07-08)
- 1.0.0 (2020-04-25)
- 1.0.0.pre.beta3 (2018-08-01)
- 1.0.0.pre.beta2 (2018-07-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/pmdtester
- gem 安装: `gem install pmdtester`
- Bundler: `gem "pmdtester"`
- 最新版本: 1.7.0
- 最新版归档: https://rubygems.org/downloads/pmdtester-1.7.0.gem
- 版本锁定: `gem "pmdtester", "~> 1.7.0"`
- 中央仓库: https://rubygems.org/
