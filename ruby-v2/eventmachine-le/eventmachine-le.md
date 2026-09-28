# eventmachine-le

**Tag**: web, testing, networking, devops

## 简介

EventMachine-LE (Live Edition) is a branch of EventMachine (https://github.com/eventmachine/eventmachine).

This branch incorporates interesting pull requests that are not yet included in the mainline EventMachine repository. The maintainers of that version prefer to minimize change in order to keep the stability with already existing EventMachine deployments, which provides an impressive multi-platform base for IPv4 TCP servers (e.g., Web servers) that don't need good UDP or IPv6 support.

This dedication to stability is helpful for production use, but can also lead to ossification. The present "Live Edition" or "Leading Edge" branch has its focus on supporting a somewhat wider use, including new Web servers or protocols beyond the HTTP Web.

To provide even more focus, this branch is currently applying its energy towards Linux and Unix/BSD/OSX environments. Java reactor and pure Ruby reactor are for now removed in this branch, and Windows/Cygwin support is untested. This may very well change later, once interesting pull requests come in.

EventMachine-LE draws from a number of dormant pull requests on the mainline version of EventMachine. New proposals will also directly come to EventMachine-LE and will be included once they are tested.

This is not a "development branch", EventMachine-LE is ready for production, just beyond the focus of mainline EventMachine.

## 官网

- 主页: https://github.com/ibc/EventMachine-LE/
- 文档: https://www.rubydoc.info/gems/eventmachine-le/1.1.7
- RubyGems: https://rubygems.org/gems/eventmachine-le

## 历史版本号

- 1.1.7 (2014-09-10)
- 1.1.6 (2013-10-07)
- 1.1.5 (2013-04-02)
- 1.1.4 (2012-10-09)
- 1.1.4.beta.2 (2012-10-09)
- 1.1.3 (2012-08-28)
- 1.1.2 (2012-07-13)
- 1.1.1 (2012-07-12)
- 1.1.0 (2012-03-13)
- 1.1.0.beta.2 (2012-03-06)
- 1.1.0.beta.1 (2012-03-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/eventmachine-le
- gem 安装: `gem install eventmachine-le`
- Bundler: `gem "eventmachine-le"`
- 最新版本: 1.1.7
- 最新版归档: https://rubygems.org/downloads/eventmachine-le-1.1.7.gem
- 版本锁定: `gem "eventmachine-le", "~> 1.1.7"`
- 中央仓库: https://rubygems.org/
