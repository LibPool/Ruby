# pluginfactory

**Tag**: database, testing, data

## 简介

PluginFactory is a mixin module that turns an including class into a factory for
its derivatives, capable of searching for and loading them by name. This is
useful when you have an abstract base class which defines an interface and basic
functionality for a part of a larger system, and a collection of subclasses
which implement the interface for different underlying functionality.

An example of where this might be useful is in a program which talks to a
database. To avoid coupling it to a specific database, you use a Driver class
which encapsulates your program's interaction with the database behind a useful
interface. Now you can create a concrete implementation of the Driver class for
each kind of database you wish to talk to. If you make the base Driver class a
PluginFactory, too, you can add new drivers simply by dropping them in a
directory and using the Driver's `create` method to instantiate them:

## 官网

- 主页: http://deveiate.org/projects/PluginFactory
- 源码仓库: http://deveiate.org/projects/PluginFactory/browser
- 文档: http://deveiate.org/code/pluginfactory/
- 问题追踪: http://deveiate.org/projects/PluginFactory/query
- RubyGems: https://rubygems.org/gems/pluginfactory

## 历史版本号

- 1.0.8 (2012-02-20)
- 1.0.7 (2010-09-27)
- 1.0.6 (2010-03-23)
- 1.0.5 (2009-11-06)
- 1.0.4 (2009-07-25)
- 1.0.3 (2009-07-25)
- 1.0.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/pluginfactory
- gem 安装: `gem install pluginfactory`
- Bundler: `gem "pluginfactory"`
- 最新版本: 1.0.8
- 最新版归档: https://rubygems.org/downloads/pluginfactory-1.0.8.gem
- 版本锁定: `gem "pluginfactory", "~> 1.0.8"`
- 中央仓库: https://rubygems.org/
