# resque-roulette

**Tag**: library

## 简介

Usually Resque workers work on queues in the given order (if there is something in the first, work it, otherwise if the there is something in the second, work on it, and so on). This plugin randomizes the order of the queues based on weights, so that a given queue will be the first queue to try based on a probability weight. Given queues A, B, C, D and weights 4, 3, 2, 1, repsectively, A will be first 40% of the time, B 30%, C 20%, and D 10%. In addition, when B is first, A will be second 4/7ths of the time (4 / [4+2+1]), and so on. The project is inspired by resque-fairly, which unfortunately mathematically does not give you this control over the weights.

## 官网

- 主页: https://github.com/trustvox/resque-roulette
- 文档: https://www.rubydoc.info/gems/resque-roulette/1.0.0
- RubyGems: https://rubygems.org/gems/resque-roulette

## 历史版本号

- 1.0.0 (2020-02-21)
- 0.0.2 (2019-01-25)
- 0.0.1 (2019-01-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/resque-roulette
- gem 安装: `gem install resque-roulette`
- Bundler: `gem "resque-roulette"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/resque-roulette-1.0.0.gem
- 版本锁定: `gem "resque-roulette", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
