# mockumentary

**Tag**: web, database, testing, data

## 简介

With the happy proliferation of TDD, test suites are getting massive, and developer efficiency is dwindling
    as we wait for our tests to pass. There is a big tradeoff between making unit test more integrationish (and therefore more reliable) vs.
    making them very mocky, unity and fast. Mockumentary is a library for the later. It inspects the ActiveRecord universe and
    makes a series of AR mockeries that approximate model without hitting the database, or making any assertions. The assertions,
    they are still part of the developers job.
    
    Mocumentary has two types of AR mockeries: One is used within the Rails universe. It uses introspection to derive association
    and field information. The second is a static copy built from the first. This static version can be used outside the Rails
    test universe in a suite faster than the speed of Rails environment load time.
    
    Mocking isn't for everyone, so test-drive responsibly.

## 官网

- 主页: http://github.com/baccigalupi/mockumentary
- RubyGems: https://rubygems.org/gems/mockumentary

## 历史版本号

- 0.2.1 (2011-11-29)
- 0.2.0 (2011-10-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/mockumentary
- gem 安装: `gem install mockumentary`
- Bundler: `gem "mockumentary"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/mockumentary-0.2.1.gem
- 版本锁定: `gem "mockumentary", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
