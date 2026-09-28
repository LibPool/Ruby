# rtm-rails

**Tag**: web, cli, database, testing, networking, template, filesystem, data

## 简介

==== Topic Maps for Rails (rtm-rails)
RTM-Rails is the Rails-Adapter for Ruby Topic Maps. It allows simple configuration of topicmaps in config/topicmaps.yml.

==== Overview
From a developer's perspective, RTM is a schema-less database management system.
The Topic Maps standard (described below) on which RTM is based provides a way of creating a self-describing schema just by using it.
You can use RTM as a complement data storage to ActiveRecord in your Rails apps.

==== Quickstart - existing Rails project
 jruby script/generate topicmaps

Run the command above after installing rtm-rails. This will create
* a minimal default configuration: config/topicmaps.yml and
* a file with more examples and explanations config/topicmaps.example.yml
* a file README.topicmaps.txt which contains more information how to use it and where to find more information
* an initializer to load the topicmaps at startup
* a rake task to migrate the topic maps backends
in your rails application.

==== Quickstart - new Rails project

For a new Rails application these are the complete initial steps:
 jruby -S rails my_topicmaps_app
 cd my_topicmaps_app
 jruby -S script/generate jdbc
 jruby -S script/generate topicmaps
 # The following lines are necessary because Rails does not have a template
 # for the H2 database and Ontopia does not support the Rails default SQLite3.
 sed -e "s/sqlite3/h2/" config/database.yml > config/database.yml.h2
 mv config/database.yml.h2 config/database.yml
 # Prepare the database and then check if all is OK
 jruby -S rake topicmaps:migrate_backends
 jruby -S rake topicmaps:check

==== Usage inside the application

When everything is fine, let's create our first topic:
 jruby -S script/console
 TM[:example].get!("http://example.org/my/first/topic")
 # and save the topic map
 TM[:example].commit

Access the configured topic maps anywhere in your application like this:
 TM[:example]

To retrieve all topics, you can do
 TM[:example].topics

To retrieve a specific topic by its subject identifier:
 TM[:example].get("http://example.org/my/topic")

Commit the changes to the database permanently:
 TM[:example].commit

... or abort the transaction:
 TM[:example].abort

More information can be found on http://rtm.topicmapslab.de/

==== Minimal configuration
 default:
   topicmaps:
     example: http://rtm.topicmapslab.de/example1/

The minimal configuration creates a single topic map, named :example with the locator given.
This topic map will be persisted in the same database as your ActiveRecord connection if not specified otherwise.
The default backend is OntopiaRDBMS (from the rtm-ontopia gem).
A more complete configuration can be found in config/topicmaps.example.yml after running "jruby script/generate topicmaps".
It also includes how to specifiy multiple connections to different data stores and so on.

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

==== License
Copyright 2009 Topic Maps Lab, University of Leipzig.
Apache License, Version 2.0

## 官网

- 主页: http://rtm.topicmapslab.de/
- RubyGems: https://rubygems.org/gems/rtm-rails

## 历史版本号

- 0.3.1 (2010-09-30)
- 0.3.0 (2010-04-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/rtm-rails
- gem 安装: `gem install rtm-rails`
- Bundler: `gem "rtm-rails"`
- 最新版本: 0.3.1
- 最新版归档: https://rubygems.org/downloads/rtm-rails-0.3.1.gem
- 版本锁定: `gem "rtm-rails", "~> 0.3.1"`
- 中央仓库: https://rubygems.org/
