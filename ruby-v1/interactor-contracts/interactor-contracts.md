# interactor-contracts

**Tag**: library

## 简介

Interactors are a pattern for structuring your business logic into units.
They have a flexible context that they pass between them, which makes them
easy-to-write, but hard-to-understand after you've written them. Much of
this confusion comes from not knowing what the interactor is supposed to
take as input and what it's expected to produce.

Enter contracts. Contracts allow you define, up front, a contract both for
the input of an interactor, known as expectations, and the output of it,
known as promises. Additionally, you can define a handler for what happens
when an interactor violates its contracts, known as a breach.

Declaring these contracts can help define your interface and make it easier
to understand how to use an interactor. They form both documentation and
validation for your business logic.

## 官网

- 主页: https://github.com/michaelherold/interactor-contracts
- 文档: https://www.rubydoc.info/gems/interactor-contracts
- 更新日志: https://github.com/michaelherold/interactor-contracts/blob/master/CHANGELOG.md
- 问题追踪: https://github.com/michaelherold/interactor-contracts/issues
- RubyGems: https://rubygems.org/gems/interactor-contracts

## 历史版本号

- 0.3.0 (2019-10-10)
- 0.2.0 (2019-05-28)
- 0.1.0 (2017-02-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/interactor-contracts
- gem 安装: `gem install interactor-contracts`
- Bundler: `gem "interactor-contracts"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/interactor-contracts-0.3.0.gem
- 版本锁定: `gem "interactor-contracts", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
