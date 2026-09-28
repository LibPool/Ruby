# right_agent

**Tag**: web, networking

## 简介

RightAgent provides a foundation for running an agent on a server to interface
in a secure fashion with other agents in the RightScale system using RightNet,
which operates in either HTTP or AMQP mode. When using HTTP, RightAgent
makes requests to RightApi servers and receives requests using long-polling or
WebSockets via the RightNet router. To respond to requests it posts to the
HTTP router. When using AMQP, RightAgent uses RabbitMQ as the message bus and
the RightNet router as the routing node to make requests; to receives requests
routed to it by the RightNet router, it establishes a queue on startup. The
packets are structured to invoke services in the agent represented by actors
and methods. The RightAgent may respond to these requests with a result packet
that the router then routes to the originator.

## 官网

- 主页: https://github.com/rightscale/right_agent
- 文档: https://www.rubydoc.info/gems/right_agent/2.7.2
- RubyGems: https://rubygems.org/gems/right_agent

## 历史版本号

- 2.7.2 (2016-07-26)
- 2.7.0 (2016-05-20)
- 2.6.3 (2016-01-11)
- 2.6.2-x86-mingw32 (2015-10-16)
- 2.6.2 (2015-10-16)
- 2.4.6 (2015-09-25)
- 2.6.1-x86-mingw32 (2015-07-02)
- 2.6.1 (2015-07-02)
- 2.5.1-x86-mingw32 (2015-03-13)
- 2.5.1 (2015-03-13)
- 2.5.0-x86-mingw32 (2015-02-24)
- 2.5.0 (2015-02-24)
- 2.4.5-x86-mingw32 (2015-01-29)
- 2.4.5 (2015-01-29)
- 2.4.4-x86-mingw32 (2014-10-24)
- 2.4.4 (2014-10-24)
- 2.4.3-x86-mingw32 (2014-10-02)
- 2.4.3 (2014-10-02)
- 2.4.2 (2014-08-26)
- 2.4.1 (2014-08-25)
- 2.4.0 (2014-08-22)
- 2.3.8 (2014-08-08)
- 2.3.7 (2014-08-05)
- 2.3.6 (2014-07-25)
- 2.3.5 (2014-07-25)
- 2.3.4 (2014-07-09)
- 2.3.3 (2014-07-08)
- 2.3.2 (2014-06-19)
- 2.3.1 (2014-06-13)
- 2.3.0 (2014-05-27)
- 2.2.1 (2014-05-07)
- 2.2.1-x86-mingw32 (2014-05-07)
- 2.2.0-x86-mingw32 (2014-05-06)
- 2.2.0 (2014-05-06)
- 2.1.5-x86-mingw32 (2014-04-15)
- 2.1.5 (2014-04-15)
- 2.1.4-x86-mingw32 (2014-04-10)
- 2.1.4 (2014-04-10)
- 2.1.3-x86-mingw32 (2014-04-10)
- 2.1.3 (2014-04-10)
- 2.1.2-x86-mingw32 (2014-04-08)
- 2.1.2 (2014-04-08)
- 2.1.1-x86-mingw32 (2014-04-03)
- 2.1.1 (2014-04-03)
- 2.1.0-x86-mingw32 (2014-04-02)
- 2.1.0 (2014-04-02)
- 2.0.8-x86-mingw32 (2014-03-04)
- 2.0.8 (2014-03-04)
- 2.0.7-x86-mingw32 (2014-02-28)
- 2.0.7 (2014-02-28)
- 1.0.1 (2013-11-14)
- 0.17.2 (2013-10-29)
- 0.17.0 (2013-08-07)
- 0.16.2 (2013-07-23)
- 0.10.13 (2013-02-07)
- 0.14.0 (2012-11-05)
- 0.13.5 (2012-10-04)
- 0.10.12 (2012-08-28)
- 0.10.11 (2012-08-21)
- 0.10.10 (2012-06-26)
- 0.10.9 (2012-06-18)
- 0.10.8 (2012-05-15)
- 0.10.6 (2012-05-09)
- 0.10.5 (2012-05-08)
- 0.10.4 (2012-05-06)
- 0.10.3 (2012-05-02)
- 0.10.2 (2012-05-01)
- 0.9.11 (2012-04-16)
- 0.9.9 (2012-04-06)
- 0.9.8 (2012-04-04)
- 0.9.7 (2012-04-04)
- 0.9.6 (2012-04-02)
- 0.9.5 (2012-03-22)
- 0.9.4 (2012-03-14)
- 0.9.3 (2012-03-13)
- 0.6.6 (2011-12-14)
- 0.6.3 (2011-11-21)
- 0.6.2 (2011-11-16)
- 0.6.1 (2011-11-15)
- 0.6.0 (2011-11-12)
- 0.5.10 (2011-11-04)
- 0.5.1 (2011-09-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/right_agent
- gem 安装: `gem install right_agent`
- Bundler: `gem "right_agent"`
- 最新版本: 2.7.2
- 最新版归档: https://rubygems.org/downloads/right_agent-2.7.2.gem
- 版本锁定: `gem "right_agent", "~> 2.7.2"`
- 中央仓库: https://rubygems.org/
