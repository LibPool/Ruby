# test_seeds

**Tag**: database, testing, filesystem, data

## 简介

Test Seeds piggy backs on the transaction fixtures functionality. Test Seeds load fixtures into the database in the same way but then start a db transaction for the duration of the test file. Any objects for the common scenarios are then created and inserted into the database. Test Seeds then execute each test case within a context of a db savepoint (or nested db transactions). This allows test seeds to be inserted into the database once and then re-used for each test case that needs it.

## 官网

- 主页: http://github.com/pkmiec/test_seeds
- RubyGems: https://rubygems.org/gems/test_seeds

## 历史版本号

- 0.0.4 (2011-08-19)
- 0.0.3 (2011-08-18)
- 0.0.2 (2011-08-16)
- 0.0.1 (2011-08-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/test_seeds
- gem 安装: `gem install test_seeds`
- Bundler: `gem "test_seeds"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/test_seeds-0.0.4.gem
- 版本锁定: `gem "test_seeds", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
