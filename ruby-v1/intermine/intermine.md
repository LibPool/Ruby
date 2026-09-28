# intermine

**Tag**: web, cli, database, testing, networking, template, filesystem, data

## 简介

= Webservice Client Library for InterMine Data-Warehouses

This library provides an interface to the InterMine webservices
API. It makes construction and execution of queries more 
straightforward, safe and convenient, and allows for results
to be used directly in Ruby code. As well as traditional row based
access, the library provides an object-orientated record result
format (similar to ActiveRecords), and allows for fast, memory 
efficient iteration of result sets.

== Example

Get all protein domains associated with a set of genes and print their names:

    require "intermine/service"

    Service.new("www.flymine.org/query").
        new_query("Pathway")
        select(:name).
        where("genes.symbol" =&gt; ["zen", "hox", "h", "bib"]).
        each_row { |row| puts row[:name]}

== Who is this for?

InterMine data warehouses are typically constructed to hold
Biological data, and as this library facilitates programmatic
access to these data, this install is primarily aimed at 
bioinformaticians. In particular, users of the following services
may find it especially useful:
 * FlyMine (http://www.flymine.org/query)
 * YeastMine (http://yeastmine.yeastgenome.org/yeastmine)
 * RatMine (http://ratmine.mcw.edu/ratmine)
 * modMine (http://intermine.modencode.org/release-23)
 * metabolicMine (http://www.metabolicmine.org/beta)

== How to use this library:

We have tried to construct an interface to this library that
does not require you to learn an entirely new set of concepts. 
As such, as well as the underlying methods that are common
to all libraries, there is an additional set of aliases and sugar
methods that emulate the DSL style of SQL:

=== SQL style

  service = Service.new("www.flymine.org/query")
  service.model.
     table("Gene").
     select("*", "pathways.*").
     where(:symbol =&gt; "zen").
     order_by(:symbol).
     outerjoin(:pathways).
     each_row do |r|
       puts r
     end

=== Common InterMine interface

  service = Service.new("www.flymine.org/query")
  query = service.new_query("Gene")
  query.add_views("*", "pathways.*")
  query.add_constraint("symbol", "=", "zen")
  query.add_sort_order(:symbol)
  query.add_join(:pathways)
  query.each_row do |r|
    puts r
  end

For more details, see the accompanying documentation and the unit tests
for interface examples. Further documentation is available at www.intermine.org.

== Support

Support is available on our development mailing list: dev@intermine.org

== License

This code is Open Source under the LGPL. Source code for this gem
can be checked out from https://github.com/intermine/intermine-ws-ruby

## 官网

- 主页: http://www.intermine.org
- 源码仓库: https://github.com/intermine/intermine-ws-ruby
- 文档: https://www.rubydoc.info/gems/intermine/1.05.00
- RubyGems: https://rubygems.org/gems/intermine

## 历史版本号

- 1.05.00 (2017-05-04)
- 1.04.00 (2013-07-08)
- 1.03.00 (2013-07-04)
- 1.02.00 (2013-06-27)
- 1.01.01 (2013-06-27)
- 1.01.00 (2013-03-01)
- 1.00.00 (2012-10-08)
- 0.99.03 (2012-01-18)
- 0.99.02 (2011-12-27)
- 0.99.01 (2011-12-12)
- 0.99.00 (2011-12-12)
- 0.98.11 (2011-11-01)
- 0.98.10 (2011-10-27)
- 0.98.09 (2011-10-26)
- 0.98.08 (2011-10-26)
- 0.98.06 (2011-08-03)
- 0.98.05 (2011-08-02)
- 0.98.04 (2011-08-02)
- 0.98.03 (2011-08-01)
- 0.98.02 (2011-08-01)
- 0.98.01 (2011-08-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/intermine
- gem 安装: `gem install intermine`
- Bundler: `gem "intermine"`
- 最新版本: 1.05.00
- 最新版归档: https://rubygems.org/downloads/intermine-1.05.00.gem
- 版本锁定: `gem "intermine", "~> 1.05.00"`
- 中央仓库: https://rubygems.org/
