# minitest-hooks

**Tag**: database, testing, data

## 简介

minitest-hooks adds around and before_all/after_all/around_all hooks for Minitest.
This allows you do things like run each suite of specs inside a database transaction,
running each spec inside its own savepoint inside that transaction, which can
significantly speed up testing for specs that share expensive database setup code.

## 官网

- 主页: http://github.com/jeremyevans/minitest-hooks
- 源码仓库: https://github.com/jeremyevans/minitest-hooks
- 更新日志: https://github.com/jeremyevans/minitest-hooks/blob/master/CHANGELOG
- 问题追踪: https://github.com/jeremyevans/minitest-hooks/issues
- RubyGems: https://rubygems.org/gems/minitest-hooks

## 历史版本号

- 1.5.4 (2026-05-04)
- 1.5.3 (2025-12-18)
- 1.5.2 (2024-08-14)
- 1.5.1 (2023-07-27)
- 1.5.0 (2018-05-21)
- 1.4.2 (2017-09-12)
- 1.4.1 (2017-07-31)
- 1.4.0 (2015-11-17)
- 1.3.0 (2015-08-17)
- 1.2.0 (2015-07-02)
- 1.1.0 (2015-05-11)
- 1.0.1 (2015-04-27)
- 1.0.0 (2015-04-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/minitest-hooks
- gem 安装: `gem install minitest-hooks`
- Bundler: `gem "minitest-hooks"`
- 最新版本: 1.5.4
- 最新版归档: https://rubygems.org/downloads/minitest-hooks-1.5.4.gem
- 版本锁定: `gem "minitest-hooks", "~> 1.5.4"`
- 中央仓库: https://rubygems.org/
