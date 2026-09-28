# rtm

**Tag**: web, database, testing, networking, template, filesystem, data

## 简介

==== Ruby Topic Maps (RTM)
RTM is a Topic Maps engine written in Ruby. See http://rtm.topicmapslab.de/ for instructions.
Several backends and extensions are available as separate gems.

==== Overview
From a developer's perspective, RTM is a schema-less database management system.
The Topic Maps standard (described below) on which RTM is based provides a way of creating a self-describing schema just by using it.

==== Quickstart
 require 'rtm'
 connection = RTM.connect # uses the default Ontopia in-memory backend
 topic_map = connection.create "http://example.org/my_topic_map/"
 some_topic = topicmap.get!("identifier_of_the_topic")
 some_topic["-"] = "default name for the topic"
 topic_map.to_xtm("my_xtm_file.xtm")

==== Topic Maps
Topic Maps is an international industry standard (ISO13250) for interchangeably representing information
about the structure of information resources used to define topics, and the relationships between topics.
A set of one or more interrelated documents that employs the notation defined by this International Standard is called a topic map.
A topic map defines a multidimensional topic space - a space in which the locations are topics,
and in which the distances between topics are measurable in terms of the number of intervening topics
which must be visited in order to get from one topic to another, and the kinds of relationships that define
the path from one topic to another, if any, through the intervening topics, if any.
In addition, information objects can have properties, as well as values for those properties, assigned to them.
The Topic Maps Data Model which is used in this implementation can be found on http://www.isotopicmaps.org/sam/sam-model/.

==== Backends
* rtm-ontopia: JRuby only, recommended, uses Ontopia: http://code.google.com/p/ontopia/
* rtm-tinytim: JRuby only, uses TinyTiM: http://tinytim.sourceforge.net/
* rtm-activerecord: uses a custom ActiveRecord schema

==== Extensions
* rtm-tmql: Adds support for the Topic Maps Query Language (TMQL), http://isotopicmaps.org/tmql/
* rtm-tmcl: Adds support for the Topic Maps Constraint Language (TMCL), http://isotopicmaps.org/tmcl/

==== License
Copyright 2009 Topic Maps Lab, University of Leipzig.
Apache License, Version 2.0

## 官网

- 主页: http://rtm.topicmapslab.de/
- 源码仓库: http://code.topicmapslab.de/rtm/
- 文档: http://rtm.topicmapslab.de/docs/
- 问题追踪: http://projects.topicmapslab.de/projects/rtm
- RubyGems: https://rubygems.org/gems/rtm

## 历史版本号

- 0.3.1 (2010-09-30)
- 0.3.0 (2010-04-14)
- 0.2.1 (2010-02-21)
- 0.2.0 (2010-02-05)
- 0.1.5 (2009-07-25)
- 0.1.4 (2009-07-25)
- 0.1.3 (2009-07-25)
- 0.1.1 (2009-07-25)
- 0.1.0 (2009-07-25)
- 0.2 (2009-07-25)
- 0.1.6 (2009-07-25)
- 0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/rtm
- gem 安装: `gem install rtm`
- Bundler: `gem "rtm"`
- 最新版本: 0.3.1
- 最新版归档: https://rubygems.org/downloads/rtm-0.3.1.gem
- 版本锁定: `gem "rtm", "~> 0.3.1"`
- 中央仓库: https://rubygems.org/
