# minitest-parallel_fork

**Tag**: testing

## 简介

minitest-parallel_fork adds fork-based parallelization to Minitest.  Each test/spec
suite is run in one of the forks, allowing this to work correctly when using
before_all/after_all/around_all hooks provided by minitest-hooks.  Using separate
processes via fork can significantly improve spec performance when using MRI,
and can work in cases where Minitest's default thread-based parallelism do not work,
such as when specs modify the constant namespace.

## 官网

- 主页: http://github.com/jeremyevans/minitest-parallel_fork
- 源码仓库: https://github.com/jeremyevans/minitest-parallel_fork
- 更新日志: https://github.com/jeremyevans/minitest-parallel_fork/blob/master/CHANGELOG
- 问题追踪: https://github.com/jeremyevans/minitest-parallel_fork/issues
- RubyGems: https://rubygems.org/gems/minitest-parallel_fork

## 历史版本号

- 2.1.1 (2025-12-18)
- 2.1.0 (2025-07-02)
- 2.0.0 (2023-11-08)
- 1.3.1 (2023-09-25)
- 1.3.0 (2022-07-05)
- 1.2.0 (2021-08-16)
- 1.1.2 (2018-07-05)
- 1.1.1 (2018-05-07)
- 1.1.0 (2018-04-19)
- 1.0.2 (2017-02-27)
- 1.0.1 (2017-01-05)
- 1.0.0 (2015-05-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/minitest-parallel_fork
- gem 安装: `gem install minitest-parallel_fork`
- Bundler: `gem "minitest-parallel_fork"`
- 最新版本: 2.1.1
- 最新版归档: https://rubygems.org/downloads/minitest-parallel_fork-2.1.1.gem
- 版本锁定: `gem "minitest-parallel_fork", "~> 2.1.1"`
- 中央仓库: https://rubygems.org/
