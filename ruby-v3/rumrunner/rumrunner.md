# rumrunner

**Tag**: cli, testing, tooling, devops, filesystem

## 简介

Rum Runner is a Rake-based utility for building multi-stage Dockerfiles.

Users can pair a multi-stage Dockerfile with a Rumfile that uses a
Rake-like DSL to customize each stage's build options and dependencies.

The `rum` executable allows users to easily invoke builds, shell-into
specific stages for debugging, and export artifacts from built containers.

Rum Runner has the following features:
* Fully compatible with Rake
* Rake-like DSL/CLI that enable simple annotation and execution of builds
* Rumfiles are completely defined in standard Ruby syntax, like Rakefiles
* Users can chain Docker build stages with prerequisites
* Artifacts can be exported from stages
* Shell tasks are automatically provided for every stage
* Stage, artifact, and shell, steps can be customized

## 官网

- 主页: https://github.com/amancevice/rumrunner.git
- 文档: https://www.rubydoc.info/gems/rumrunner/0.5.0
- RubyGems: https://rubygems.org/gems/rumrunner

## 历史版本号

- 0.5.0 (2019-12-10)
- 0.4.3 (2019-10-03)
- 0.4.2 (2019-09-23)
- 0.4.1 (2019-08-13)
- 0.4.0 (2019-08-10)
- 0.3.4 (2019-08-10)
- 0.3.2 (2019-08-03)
- 0.3.1 (2019-07-28)
- 0.3.0 (2019-07-26)
- 0.2.6 (2019-07-26)
- 0.2.5 (2019-07-24)
- 0.2.4 (2019-07-23)
- 0.2.3 (2019-07-22)
- 0.2.2 (2019-07-22)
- 0.2.1 (2019-07-21)
- 0.2.0 (2019-07-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/rumrunner
- gem 安装: `gem install rumrunner`
- Bundler: `gem "rumrunner"`
- 最新版本: 0.5.0
- 最新版归档: https://rubygems.org/downloads/rumrunner-0.5.0.gem
- 版本锁定: `gem "rumrunner", "~> 0.5.0"`
- 中央仓库: https://rubygems.org/
