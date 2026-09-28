# mulligan

**Tag**: library

## 简介

Allows you to decouple the code implementing a exception-handling strategy from the code which decides which strategy to use.

In other words, when you handle a Mulligan::Condition in your rescue clause, you can choose from a set of strategies (called "restarts") exposed by the exception to take the stack back to where #raise was called, execute your strategy, and pretend that the exception was never raised.

## 官网

- 主页: http://michaeljbishop.github.io/mulligan
- 文档: https://www.rubydoc.info/gems/mulligan/0.4.2
- RubyGems: https://rubygems.org/gems/mulligan

## 历史版本号

- 0.4.2 (2014-03-14)
- 0.4.1 (2014-03-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/mulligan
- gem 安装: `gem install mulligan`
- Bundler: `gem "mulligan"`
- 最新版本: 0.4.2
- 最新版归档: https://rubygems.org/downloads/mulligan-0.4.2.gem
- 版本锁定: `gem "mulligan", "~> 0.4.2"`
- 中央仓库: https://rubygems.org/
