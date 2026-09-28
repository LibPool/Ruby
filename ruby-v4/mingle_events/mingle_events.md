# mingle_events

**Tag**: web, networking, template

## 简介

Mingle 3.3 introduced a new Events API in the form of an "Atom feed":http://www.thoughtworks-studios.com/mingle/3.3/help/mingle_api_events.html. The Mingle team and ThoughtWorks Studios are big believers in the use of Atom for exposing events. Atom is a widely used standard, and this event API style puts the issue of robust event delivery in the hands of the consumer, where it belongs. In fact, we'd argue this is the only feasible means of robust, scalable event delivery, short of spending hundreds of thousands or millions of dollars on enterprise buses and such. Atom-delivered events are cheap, scalable, standards-based, and robust.

    However, we do accept that asking integrators wishing to consume events to implement polling is not ideal. Writing polling consumers can be tedious. And this tedium gets in the way of writing sweet Mingle integrations. We are addressing this by publishing libraries such as this, which if effective, fully hide the mechanics of event polling from the consumer. The consumer only need worry about the processing of events. Said processing is modeled in the style of 'pipes and filters.'

## 官网

- 主页: https://github.com/ThoughtWorksStudios/mingle_events
- 文档: https://www.rubydoc.info/gems/mingle_events/0.2.3
- RubyGems: https://rubygems.org/gems/mingle_events

## 历史版本号

- 0.2.3 (2015-09-10)
- 0.2.1 (2015-03-11)
- 0.2.0 (2015-03-10)
- 0.1.9 (2015-02-08)
- 0.1.8 (2015-02-08)
- 0.1.7 (2013-09-12)
- 0.1.5 (2013-07-24)
- 0.1.4 (2013-07-24)
- 0.1.3 (2011-09-22)
- 0.1.1 (2011-09-20)
- 0.1.0 (2011-09-17)
- 0.0.7 (2011-09-02)
- 0.0.6 (2011-08-12)
- 0.0.4 (2011-08-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/mingle_events
- gem 安装: `gem install mingle_events`
- Bundler: `gem "mingle_events"`
- 最新版本: 0.2.3
- 最新版归档: https://rubygems.org/downloads/mingle_events-0.2.3.gem
- 版本锁定: `gem "mingle_events", "~> 0.2.3"`
- 中央仓库: https://rubygems.org/
