# rsence

**Tag**: web, cli, database, serialization, filesystem, data

## 简介

RSence is a different and unique development model and software frameworks designed first-hand for real-time web applications. RSence consists of separate, but tigtly integrated data- and user interface frameworks.

RSence could be classified as a thin server - thick client system.

Applications and submobules are installed as indepenent plugin bundles into the plugins folder of a RSence environment, which in itself is a self-contained bundle. A big part of RSence itself is implemented as shared plugin bundles.

The user interface framework of RSence is implemented in high-level user interface widget classes. The widget classes share a common foundation API and access the browser's native API's using an abstracted event- and element layer, which provides exceptional cross-browser compatibility.

The data framework of RSence is a event-driven system, which synchronized shared values between the client and server. It's like a realtime bidirectional form-submission engine that handles data changes intelligently. On the client, changed values trigger events on user interface widgets. On the server, changed values trigger events on value responder methods of server plugin modules. It doesn't matter if the change originates on client or server, it's all synchronized and propagated automatically.

The server framework is implemented as a high-level, modular data-event-driven system, which handles delegation of tasks impossible to implement using a client-only approach.
Client sessions are selectively connected to other client sessions and legacy back-ends via the server by using the data framework.

The client is written in Javascript and the server is written in Ruby. The client also supports CoffeeScript for custom logic. In many cases, no custom client logic is needed; the user interfaces can be defined in tree-like data models. By default, the models are parsed from YAML files, and other structured data formats are possible, including XML, JSON, databases or any custom logic capable of producing similar objects. The server can connect to custom environments and legacy backends accessible on the server, including software written in other languages.

## 官网

- 主页: http://www.rsence.org/
- 源码仓库: http://rsence.org/projects/rsence/repository/revisions/master/entry
- 文档: http://rsence.org/projects/rsence/
- 问题追踪: http://rsence.org/projects/rsence/issues
- RubyGems: https://rubygems.org/gems/rsence

## 历史版本号

- 2.2.5 (2012-07-13)
- 2.2.4 (2012-05-21)
- 2.2.3 (2012-05-14)
- 2.2.2 (2012-04-28)
- 2.2.1 (2012-04-27)
- 2.2.0 (2012-03-31)
- 2.1.11 (2011-03-29)
- 2.1.10 (2011-03-03)
- 2.1.9 (2011-02-19)
- 2.1.8 (2011-01-28)
- 2.1.7 (2011-01-03)
- 2.1.6 (2010-12-15)
- 2.1.5 (2010-12-14)
- 2.1.4 (2010-12-13)
- 2.1.3 (2010-12-12)
- 2.1.2 (2010-12-09)
- 2.1.1 (2010-12-07)
- 2.1.0 (2010-12-01)
- 2.0.9.23 (2010-08-28)
- 2.0.9.22.pre (2010-08-25)
- 2.0.9.21.pre (2010-08-18)
- 2.0.9.20.pre (2010-08-15)
- 2.0.8.19 (2010-07-26)
- 2.0.4.15 (2010-07-16)
- 2.0.3.14 (2010-07-15)
- 2.0.2.13 (2010-07-09)
- 2.0.1.12 (2010-07-07)
- 2.0.0.11 (2010-07-06)
- 2.0.0.10.pre (2010-05-29)
- 2.0.0.9.pre (2010-05-25)
- 2.0.0.8.pre (2010-05-19)
- 2.0.0.7.pre (2010-05-18)
- 2.0.0.6.pre (2010-05-17)
- 2.0.0.5.pre (2010-05-10)
- 2.0.0.4.pre (2010-05-10)
- 2.0.0.3.pre (2010-05-08)
- 2.0.0.2.pre (2010-05-08)
- 2.0.0.1.pre (2010-05-08)
- 2.0.0.0.pre (2010-04-29)
- 2.0.0.pre (2010-04-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/rsence
- gem 安装: `gem install rsence`
- Bundler: `gem "rsence"`
- 最新版本: 2.2.5
- 最新版归档: https://rubygems.org/downloads/rsence-2.2.5.gem
- 版本锁定: `gem "rsence", "~> 2.2.5"`
- 中央仓库: https://rubygems.org/
