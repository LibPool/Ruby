# abstract_feature_branch

**Tag**: database, testing, serialization, tooling, filesystem, data

## 简介

abstract_feature_branch is a Ruby gem that provides a unique variation on the Branch by Abstraction Pattern by Paul Hammant and the Feature Toggles Pattern by Martin Fowler to enhance team productivity and improve software fault tolerance.

It provides the ability to wrap blocks of code with an abstract feature branch name, and then specify in a configuration file which features to be switched on or off.

The goal is to build out upcoming features in the same source code repository branch (i.e. Continuous Integration and Trunk-Based Development), regardless of whether all are completed by the next release date or not, thus increasing team productivity by preventing integration delays. Developers then disable in-progress features until they are ready to be switched on in production, yet enable them locally and in staging environments for in-progress testing.

This gives developers the added benefit of being able to switch a feature off after release should big problems arise for a high risk feature.

abstract_feature_branch additionally supports Domain Driven Design's pattern of Bounded Contexts by allowing developers to configure context-specific feature files if needed.

abstract_feature_branch is one of the simplest and most minimalistic "Feature Flags" Ruby gems out there as it enables you to get started very quickly by simply leveraging YAML files without having to set up a data store if you do not need it (albeit, you also have the option to use Redis as a very fast in-memory data store).

## 官网

- 主页: http://github.com/AndyObtiva/abstract_feature_branch
- 文档: https://www.rubydoc.info/gems/abstract_feature_branch/1.6.0
- RubyGems: https://rubygems.org/gems/abstract_feature_branch

## 历史版本号

- 1.6.0 (2024-01-22)
- 1.5.1 (2023-02-14)
- 1.5.0 (2023-02-12)
- 1.4.0 (2023-02-05)
- 1.3.3 (2023-01-15)
- 1.3.2 (2022-12-12)
- 1.3.1 (2022-12-12)
- 1.3.0 (2022-12-11)
- 1.2.2 (2014-02-23)
- 1.2.1 (2014-01-23)
- 1.2.0 (2014-01-19)
- 1.1.1 (2014-01-14)
- 1.1.0 (2014-01-14)
- 1.0.0 (2013-11-26)
- 0.9.0 (2013-11-26)
- 0.8.0 (2013-11-25)
- 0.7.1 (2013-11-25)
- 0.7.0 (2013-11-25)
- 0.6.4 (2013-11-23)
- 0.6.3 (2013-11-23)
- 0.6.2 (2013-11-23)
- 0.6.1 (2013-11-23)
- 0.6.0 (2013-11-23)
- 0.5.0 (2013-11-22)
- 0.4.0 (2013-11-21)
- 0.3.6 (2013-11-19)
- 0.3.5 (2013-11-19)
- 0.3.4 (2013-11-19)
- 0.3.3 (2012-12-13)
- 0.3.2 (2012-12-13)
- 0.3.1 (2012-12-13)
- 0.3.0 (2012-12-13)
- 0.2.0 (2012-11-25)
- 0.1.0 (2012-11-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/abstract_feature_branch
- gem 安装: `gem install abstract_feature_branch`
- Bundler: `gem "abstract_feature_branch"`
- 最新版本: 1.6.0
- 最新版归档: https://rubygems.org/downloads/abstract_feature_branch-1.6.0.gem
- 版本锁定: `gem "abstract_feature_branch", "~> 1.6.0"`
- 中央仓库: https://rubygems.org/
