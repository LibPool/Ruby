# rbenchmarker

**Tag**: web, testing, networking, template

## 简介

Rbenchmarker is a gem that allows you to automatically benchmark the execution time of a method defined in a Ruby class and module. Benchmark module (https://docs.ruby-lang.org/ja/latest/class/Benchmark.html) is used inside Rbenchmarker, and bm method is automatically applied to all target methods.
However, ｍethod itself to which Rbenchmarker is applied remains unchanged, takes the same arguments as before, and returns the same return value as before.
So you don't have to change the methods yourself, and you don't have to benchmark the methods one by one. Just launch the application as before and will automatically benchmark all targeted methods!

## 官网

- 主页: https://github.com/shibatadaiki/Rbenchmarker
- 源码仓库: https://github.com/shibatadaiki/Rbenchmarker/
- 更新日志: https://github.com/shibatadaiki/Rbenchmarker/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/rbenchmarker

## 历史版本号

- 0.1.1 (2021-02-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/rbenchmarker
- gem 安装: `gem install rbenchmarker`
- Bundler: `gem "rbenchmarker"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/rbenchmarker-0.1.1.gem
- 版本锁定: `gem "rbenchmarker", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
