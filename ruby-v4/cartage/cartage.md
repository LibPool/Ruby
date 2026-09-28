# cartage

**Tag**: web, networking, devops, data

## 简介

Cartage provides a repeatable means to create a package for a server-side
application that can be used in deployment with a configuration tool like
Ansible, Chef, Puppet, or Salt. The package is created with vendored
dependencies so that it can be deployed in environments with strict access
control rules and without requiring development tool presence on the target
server(s).

This is the last release of cartage. It's been a fun ride, but Docker-based
images are our future at Kinetic Commerce. There is one feature that remains
useful, the release-metadata output. We have created a new, more extensible
format for which we will be creating a gem to manage this. One example of the
implementation can be found at:

https://github.com/KineticCafe/release-metadata-ts

We will also be replacing `cartage-rack` with a new gem supporting this new
format.

## 官网

- 主页: https://github.com/KineticCafe/cartage/
- 文档: http://www.rubydoc.info/github/KineticCafe/cartage/master
- RubyGems: https://rubygems.org/gems/cartage

## 历史版本号

- 2.2.1 (2022-05-09)
- 2.2 (2020-03-19)
- 2.1 (2017-03-16)
- 2.0 (2016-05-31)
- 2.0.rc1 (2016-05-25)
- 1.2 (2015-05-27)
- 1.1.1 (2015-03-26)
- 1.1 (2015-03-26)
- 1.0 (2015-03-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/cartage
- gem 安装: `gem install cartage`
- Bundler: `gem "cartage"`
- 最新版本: 2.2.1
- 最新版归档: https://rubygems.org/downloads/cartage-2.2.1.gem
- 版本锁定: `gem "cartage", "~> 2.2.1"`
- 中央仓库: https://rubygems.org/
