# coroutines

**Tag**: library

## 简介

A library for creating and composing producer/transformer/consumer coroutines.
Producers are already provided by Ruby's built-in Enumerator class; this
library provides Transformer and Consumer classes that work analogously. In
particular, they are also based on Fiber and not on threads (as in some other
producer/consumer libraries). Also provides a module Sink, which is analogous
to Enumerable, and Enumerable/Transformer/Sink composition.

## 官网

- 主页: http://nome.github.io/coroutines
- 文档: https://www.rubydoc.info/gems/coroutines/0.2.2
- RubyGems: https://rubygems.org/gems/coroutines

## 历史版本号

- 0.2.2 (2014-10-15)
- 0.2.1 (2014-10-14)
- 0.2.0 (2014-10-12)
- 0.1.1 (2014-10-12)
- 0.1.0 (2014-10-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/coroutines
- gem 安装: `gem install coroutines`
- Bundler: `gem "coroutines"`
- 最新版本: 0.2.2
- 最新版归档: https://rubygems.org/downloads/coroutines-0.2.2.gem
- 版本锁定: `gem "coroutines", "~> 0.2.2"`
- 中央仓库: https://rubygems.org/
