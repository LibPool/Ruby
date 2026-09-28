# capybara_error_intel

**Tag**: data

## 简介

Capybara provides excellent error messages for its
                          built in predicate methods: has_selector?, has_text?,
                          has_title? etc.. but when those are used from Page
                          Objects while exposing predicate methods from the
                          PageObjects themselves the error messages are lost
                          and all we get is "expected true, got false".
                          Including this module into your PageObject by adding
                          "include CapybaraErrorIntel::DSL" after
                          "include Capybara::DSL" will return the heuristic
                          error messages.

## 官网

- 主页: https://github.com/dkarter/capybara_error_intel
- 文档: https://www.rubydoc.info/gems/capybara_error_intel/2.0.0
- RubyGems: https://rubygems.org/gems/capybara_error_intel

## 历史版本号

- 2.0.0 (2022-07-06)
- 1.1.1 (2019-09-22)
- 1.1.0 (2018-05-14)
- 1.0.2 (2016-10-28)
- 1.0.1 (2016-10-28)
- 1.0.0 (2016-09-19)
- 0.1.2 (2016-09-19)
- 0.1.1 (2016-09-14)
- 0.1.0 (2016-09-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/capybara_error_intel
- gem 安装: `gem install capybara_error_intel`
- Bundler: `gem "capybara_error_intel"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/capybara_error_intel-2.0.0.gem
- 版本锁定: `gem "capybara_error_intel", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
