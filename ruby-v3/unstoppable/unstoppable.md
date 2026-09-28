# unstoppable

**Tag**: database, testing, data

## 简介

Problem:
While Cucumber is an awesome tool, for some kinds of tests it's default behaviour becomes an obstacle. Testing large batches of input against a slow error prone system is the source of much frustration. Cucumber will skip remaining steps on failure or error. This is especially problematic if the test input is a dynamic collection, *(e.g. results of a database query). This is opposed to a static collection testing which is solved by a Scenario Outline.

Solution:

We need to step putside Cucumber's default pass/fail/error handling. Capture all failures and errors in collections. Log errors and failures. Generate a pass/fail manifest against the test inputs.

Do not use this for normal BDD style testing, Cucumber's default behaviour is perfect for that.

Public Interface:

This is a works in progress so I expect changes as usage reveals more.

In your cucumber env.rb

Before do |scenario| setup_unstoppable end

After do |scenario| print unstoppable_failures(scenario) print unstoppable_errors(scenario) end

In a step definition wrap any operation that you do not wish to stop execution like so

unstoppable do expect(thing).to be(exected_thing) end

This helper method does the following:

runs executes the block
catches any exception 2a. adds error to errors collection if an error 2b. adds expectation failure to failures collection if error is an RSpec::Expectations::ExpectationNotMetError
logs error/failure

## 官网

- 主页: https://rubygems.org/gems/unstoppable
- 文档: https://www.rubydoc.info/gems/unstoppable/0.1.0

## 历史版本号

- 0.1.0 (2013-12-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/unstoppable
- gem 安装: `gem install unstoppable`
- Bundler: `gem "unstoppable"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/unstoppable-0.1.0.gem
- 版本锁定: `gem "unstoppable", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
