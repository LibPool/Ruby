# fastlane-plugin-retry_tests

**Tag**: testing, serialization, filesystem

## 简介

This fastlane plugin includes the following actions:
    1) multi_scan: uses scan to run Xcode tests, optionally in batches, a given number of times: only re-testing failing tests.
    2) suppress_tests_from_junit: uses a junit xml report file to suppress either passing or failing tests in an Xcode Scheme.
    3) suppress_tests: suppresses specific tests in a specific or all Xcode Schemes in a given project.
    4) suppressed_tests: retrieves a list of tests that are suppressed in a specific or all Xcode Schemes in a project.
    5) tests_from_junit: retrieves the failing and passing tests as reported in a junit xml file.
    6) tests_from_xctestrun: retrieves all of the tests from xctest bundles referenced by the xctestrun file
    7) collate_junit_reports: collects and correctly organizes junit reports from multiple test passes.

## 官网

- 主页: https://github.com/kouzoh/fastlane-plugin-retry_tests
- 文档: https://www.rubydoc.info/gems/fastlane-plugin-retry_tests/2.3.7
- RubyGems: https://rubygems.org/gems/fastlane-plugin-retry_tests

## 历史版本号

- 2.3.7 (2018-04-19)
- 1.3.7 (2018-04-19)
- 1.3.6 (2018-04-18)
- 1.3.5 (2018-04-18)
- 1.3.4 (2018-04-18)
- 1.3.3 (2018-04-18)
- 1.3.2 (2018-04-18)
- 1.3.1 (2018-04-18)
- 1.3.0 (2018-04-18)
- 1.2.9 (2018-04-18)
- 1.2.8 (2018-04-18)
- 1.2.7 (2018-04-18)
- 1.2.6 (2018-03-20)
- 1.2.5 (2018-03-20)
- 1.2.4 (2018-03-20)
- 1.2.3 (2018-03-20)
- 1.1.7 (2018-03-19)
- 1.1.6 (2018-03-19)
- 1.1.5 (2018-03-19)
- 1.1.4 (2018-03-15)
- 1.1.3 (2018-03-15)
- 1.1.2 (2018-03-15)
- 1.1.0 (2018-03-15)
- 1.0.9 (2018-03-14)
- 1.0.8 (2018-03-14)
- 1.0.7 (2018-03-14)
- 1.0.6 (2018-03-13)
- 1.0.5 (2018-03-12)
- 1.0.4 (2018-03-12)
- 1.0.3 (2018-03-12)
- 1.0.2 (2018-03-09)
- 1.0.1 (2018-03-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/fastlane-plugin-retry_tests
- gem 安装: `gem install fastlane-plugin-retry_tests`
- Bundler: `gem "fastlane-plugin-retry_tests"`
- 最新版本: 2.3.7
- 最新版归档: https://rubygems.org/downloads/fastlane-plugin-retry_tests-2.3.7.gem
- 版本锁定: `gem "fastlane-plugin-retry_tests", "~> 2.3.7"`
- 中央仓库: https://rubygems.org/
