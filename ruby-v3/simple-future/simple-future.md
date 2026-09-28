# simple-future

**Tag**: library

## 简介

SimpleFuture is class that simplifies coarse-grained concurrency using
    processes instead of threads.

    Each instance represents the future result of a block that is passed
    to it.  The block is evaluated in a forked child process and its result
    is returned to the SimpleFuture object.  This only works on Ruby
    implementations that provide Process.fork().

## 官网

- 主页: https://github.com/suetanvil/simple-future
- 文档: https://www.rubydoc.info/gems/simple-future/1.0.0
- RubyGems: https://rubygems.org/gems/simple-future

## 历史版本号

- 1.0.0 (2018-01-18)
- 1.0.0.pre3 (2018-01-17)
- 1.0.0.pre2 (2018-01-17)
- 1.0.0.pre1 (2018-01-16)
- 1.0.0.pre (2018-01-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/simple-future
- gem 安装: `gem install simple-future`
- Bundler: `gem "simple-future"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/simple-future-1.0.0.gem
- 版本锁定: `gem "simple-future", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
