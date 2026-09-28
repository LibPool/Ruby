# transaction-simple

**Tag**: testing, serialization, filesystem, data

## 简介

Transaction::Simple provides a generic way to add active transaction support to
objects. The transaction methods added by this module will work with most
objects, excluding those that cannot be Marshal-ed (bindings, procedure
objects, IO instances, or singleton objects).

The transactions supported by Transaction::Simple are not associated with any
sort of data store. They are "live" transactions occurring in memory on the
object itself. This is to allow "test" changes to be made to an object before
making the changes permanent.

Transaction::Simple can handle an "infinite" number of transaction levels
(limited only by memory). If I open two transactions, commit the second, but
abort the first, the object will revert to the original version.

Transaction::Simple supports "named" transactions, so that multiple levels of
transactions can be committed, aborted, or rewound by referring to the
appropriate name of the transaction. Names may be any object except nil.

Transaction groups are also supported. A transaction group is an object wrapper
that manages a group of objects as if they were a single object for the purpose
of transaction management. All transactions for this group of objects should be
performed against the transaction group object, not against individual objects
in the group.

Version 1.4.0 of Transaction::Simple adds a new post-rewind hook so that
complex graph objects of the type in tests/tc_broken_graph.rb can correct
themselves.

Version 1.4.0.1 just fixes a simple bug with #transaction method handling
during the deprecation warning.

Version 1.4.0.2 is a small update for people who use Transaction::Simple in
bundler (adding lib/transaction-simple.rb) and other scenarios where having Hoe
as a runtime dependency (a bug fixed in Hoe several years ago, but not visible
in Transaction::Simple because it has not needed a re-release). All of the
files internally have also been marked as UTF-8, ensuring full Ruby 1.9
compatibility.

## 官网

- 主页: http://trans-simple.rubyforge.org/
- RubyGems: https://rubygems.org/gems/transaction-simple

## 历史版本号

- 1.4.0.2 (2012-06-21)
- 1.4.0 (2009-07-25)
- 1.3.0 (2009-07-25)
- 1.2.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/transaction-simple
- gem 安装: `gem install transaction-simple`
- Bundler: `gem "transaction-simple"`
- 最新版本: 1.4.0.2
- 最新版归档: https://rubygems.org/downloads/transaction-simple-1.4.0.2.gem
- 版本锁定: `gem "transaction-simple", "~> 1.4.0.2"`
- 中央仓库: https://rubygems.org/
