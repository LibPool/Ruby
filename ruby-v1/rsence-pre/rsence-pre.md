# rsence-pre

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
- 文档: https://www.rubydoc.info/gems/rsence-pre/3.0.0.16
- RubyGems: https://rubygems.org/gems/rsence-pre

## 历史版本号

- 3.0.0.16 (2015-03-04)
- 3.0.0.15 (2013-10-11)
- 3.0.0.14 (2013-07-04)
- 3.0.0.12 (2013-06-27)
- 3.0.0.11 (2013-06-16)
- 3.0.0.10 (2013-06-16)
- 3.0.0.9 (2013-06-12)
- 3.0.0.8 (2013-05-28)
- 3.0.0.7 (2013-05-22)
- 3.0.0.6 (2013-05-22)
- 3.0.0.5 (2013-05-20)
- 3.0.0.4 (2013-05-20)
- 3.0.0.3 (2013-05-11)
- 3.0.0.2 (2013-05-10)
- 3.0.0.1 (2013-05-10)
- 3.0.0.0 (2013-05-10)
- 2.3.0.26 (2013-05-07)
- 2.3.0.25 (2013-05-03)
- 2.3.0.24 (2013-04-21)
- 2.3.0.23 (2013-04-10)
- 2.3.0.22 (2013-03-07)
- 2.3.0.21 (2013-03-07)
- 2.3.0.20 (2013-03-01)
- 2.3.0.19 (2013-02-27)
- 2.3.0.18 (2013-02-21)
- 2.3.0.17 (2013-02-21)
- 2.3.0.16 (2013-01-17)
- 2.3.0.15 (2013-01-11)
- 2.3.0.14 (2012-12-03)
- 2.3.0.13 (2012-11-28)
- 2.3.0.12 (2012-11-23)
- 2.3.0.11 (2012-11-16)
- 2.3.0.10 (2012-11-08)
- 2.3.0.9 (2012-11-02)
- 2.3.0.8 (2012-11-02)
- 2.3.0.7 (2012-10-30)
- 2.3.0.6 (2012-10-19)
- 2.3.0.5 (2012-09-10)
- 2.3.0.4 (2012-08-31)
- 2.3.0.3 (2012-08-22)
- 2.3.0.2 (2012-08-08)
- 2.3.0.1 (2012-08-04)
- 2.3.0.0 (2012-07-26)
- 2.2.2.1 (2012-04-27)
- 2.2.2.0 (2012-04-27)
- 2.2.0.38 (2012-02-21)
- 2.2.0.37 (2012-01-27)
- 2.2.0.36 (2012-01-27)
- 2.2.0.35 (2012-01-19)
- 2.2.0.34 (2011-12-30)
- 2.2.0.33 (2011-12-13)
- 2.2.0.31 (2011-12-11)
- 2.2.0.30 (2011-12-09)
- 2.2.0.29 (2011-11-30)
- 2.2.0.28 (2011-11-29)
- 2.2.0.27 (2011-11-25)
- 2.2.0.26 (2011-11-24)
- 2.2.0.25 (2011-11-21)
- 2.2.0.24 (2011-11-03)
- 2.2.0.23 (2011-09-23)
- 2.2.0.22 (2011-09-07)
- 2.2.0.21 (2011-08-20)
- 2.2.0.20 (2011-08-09)
- 2.2.0.19 (2011-08-03)
- 2.2.0.18 (2011-08-02)
- 2.2.0.17 (2011-07-31)
- 2.2.0.16 (2011-07-28)
- 2.2.0.15 (2011-07-27)
- 2.2.0.14 (2011-07-26)
- 2.2.0.13 (2011-07-23)
- 2.2.0.12 (2011-07-13)
- 2.2.0.11 (2011-06-12)
- 2.2.0.10 (2011-06-11)
- 2.2.0.9 (2011-06-10)
- 2.2.0.8 (2011-06-09)
- 2.2.0.7 (2011-05-22)
- 2.2.0.5 (2011-04-01)
- 2.2.0.4 (2011-03-30)
- 2.2.0.3 (2011-03-29)
- 2.2.0.2 (2011-03-11)
- 2.2.0.1 (2011-03-10)
- 2.2.0.0 (2011-03-05)
- 2.1.8.1 (2011-01-20)
- 2.1.8.0 (2011-01-18)
- 2.1.0.21 (2010-12-01)
- 2.1.0.20 (2010-11-29)
- 2.1.0.19 (2010-11-29)
- 2.1.0.18 (2010-11-25)
- 2.1.0.17 (2010-11-25)
- 2.1.0.16 (2010-11-22)
- 2.1.0.15 (2010-11-21)
- 2.1.0.14 (2010-11-17)
- 2.1.0.13 (2010-11-12)
- 2.1.0.12 (2010-10-27)
- 2.1.0.11 (2010-10-25)
- 2.1.0.10 (2010-10-25)
- 2.1.0.9 (2010-10-19)
- 2.1.0.8.pre (2010-09-12)
- 2.1.0.7.pre (2010-09-09)
- 2.1.0.6.pre (2010-09-08)
- 2.1.0.4.pre (2010-09-05)
- 2.1.0.3.pre (2010-09-05)
- 2.1.0.2.pre (2010-09-05)
- 2.1.0.1.pre (2010-09-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/rsence-pre
- gem 安装: `gem install rsence-pre`
- Bundler: `gem "rsence-pre"`
- 最新版本: 3.0.0.16
- 最新版归档: https://rubygems.org/downloads/rsence-pre-3.0.0.16.gem
- 版本锁定: `gem "rsence-pre", "~> 3.0.0.16"`
- 中央仓库: https://rubygems.org/
