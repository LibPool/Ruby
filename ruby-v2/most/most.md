# most

**Tag**: web, cli, testing, networking, tooling

## 简介

Most is a simple academic modular open software tester.  Most, the Core is the main part of the system. Most provides the environment and interface bridges for modules that will implement the basic functionality of the testing system.  In general Most, the Core consists form two main interfaces: the connector and the tester.  The connector interface offers the basic bridge to make an implementation of a module which will act as a controlling interface of the system. It can be a command line interface or it can be a module which will set up a server providing a network access for end users.  The tester interface allows building an implementation of the software validator. By default the Most ships with the tester compliant with the ICPC Validator Standard. The Most system proposes to implement a testing system following this standard, but it is not obligatory. The 3-rd party implementation can vary significantly considering the user preferences.  It is possible to build other interface bridges using the abstract interface classes provided by the Most system to extend the functionality of the modules. For example the implementation of the connector interface in the form of the network server can build a tunnel interface bridge, so that developers can make implementations, for example, of a SSH tunnel in order to provide a secure connection with the testing system.  The default system bundle is shipped with a number of basic interface implementations (modules). Please, consider taking a look on realize notes for the list of supplied modules.

## 官网

- 文档: https://www.rubydoc.info/gems/most/0.7.7
- RubyGems: https://rubygems.org/gems/most

## 历史版本号

- 0.7.7 (2009-10-30)
- 0.7.6 (2009-10-30)
- 0.7.5 (2009-10-28)
- 0.7.4 (2009-10-28)
- 0.7.3 (2009-10-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/most
- gem 安装: `gem install most`
- Bundler: `gem "most"`
- 最新版本: 0.7.7
- 最新版归档: https://rubygems.org/downloads/most-0.7.7.gem
- 版本锁定: `gem "most", "~> 0.7.7"`
- 中央仓库: https://rubygems.org/
