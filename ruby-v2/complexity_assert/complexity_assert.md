# complexity_assert

**Tag**: testing, data

## 简介

They are some performance critical pieces of code that will be executed on huge data sets, which we want to make sure will run fast enough. Unfortunately, enforcing this is not easy, often requiring large scale and slow benchmarks. This rspec library (the result of an experiment to learn machine learning) uses linear regression to determine the time complexity (Big O notation, O(x)) of a piece of code and to check that it is at least as good as what we expect. This does not require huge data sets (only a few large ones) and can be written as any unit test (not as fast though).

## 官网

- 主页: https://github.com/philou/complexity-assert
- 文档: https://www.rubydoc.info/gems/complexity_assert/0.1.0
- RubyGems: https://rubygems.org/gems/complexity_assert

## 历史版本号

- 0.1.0 (2017-02-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/complexity_assert
- gem 安装: `gem install complexity_assert`
- Bundler: `gem "complexity_assert"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/complexity_assert-0.1.0.gem
- 版本锁定: `gem "complexity_assert", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
