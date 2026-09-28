# debride

**Tag**: web, testing, filesystem

## 简介

Analyze code for potentially uncalled / dead methods, now with auto-removal.

== Features/Problems:

* Static analysis of code. Can be easily hooked up to a CI.
* As with all static analysis tools of dynamic languages, can't be 100%.
* Whitelisting known good methods by name or regexp.
* Use --rails for Rails-specific domain knowledge.
* Use debride_rm to brazenly remove all unused methods. BE CAREFUL.
* Use `debride_rails_whitelist` to generate an emperical whitelist from logs.
* Uses path_expander, so you can use:
  * dir_arg -- expand a directory automatically
  * @file_of_args -- persist arguments in a file
  * -path_to_subtract -- ignore intersecting subsets of files/directories

## 官网

- 主页: https://github.com/seattlerb/debride
- 文档: http://docs.seattlerb.org/debride
- RubyGems: https://rubygems.org/gems/debride

## 历史版本号

- 1.15.2 (2026-04-20)
- 1.15.1 (2026-01-26)
- 1.15.0 (2026-01-02)
- 1.14.0 (2025-12-11)
- 1.13.0 (2025-06-11)
- 1.12.0 (2023-05-18)
- 1.11.0 (2023-03-24)
- 1.10.1 (2022-12-03)
- 1.10.0 (2022-12-03)
- 1.9.0 (2022-05-23)
- 1.8.2 (2019-09-25)
- 1.8.1 (2017-11-29)
- 1.8.0 (2017-05-09)
- 1.7.0 (2016-12-01)
- 1.6.0 (2016-05-15)
- 1.5.1 (2015-08-10)
- 1.5.0 (2015-06-15)
- 1.4.0 (2015-05-27)
- 1.3.0 (2015-04-13)
- 1.2.0 (2015-03-27)
- 1.1.0 (2015-03-18)
- 1.0.0 (2015-03-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/debride
- gem 安装: `gem install debride`
- Bundler: `gem "debride"`
- 最新版本: 1.15.2
- 最新版归档: https://rubygems.org/downloads/debride-1.15.2.gem
- 版本锁定: `gem "debride", "~> 1.15.2"`
- 中央仓库: https://rubygems.org/
