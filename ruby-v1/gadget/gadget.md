# gadget

**Tag**: database, filesystem, data

## 简介

# Gadget

Some methods for getting metadata and other deep details from a PostgreSQL database.

## Installation

Add this line to your application's Gemfile:

    gem 'gadget'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install gadget

## Usage

`#tables(conn)`

Returns a list of all tables in the schema reachable through `conn`.

`#columns(conn, tablename=nil)`

Returns a list of all columns in the schema reachable through `conn`.
If `tablename` is given, returns the columns in only that table.

`#foreign_keys(conn, tablename=nil)`

Returns a list of all foreign keys in the schema reachable through `conn`.
If `tablename` is given, returns the foreign keys in only that table.

`#constraints(conn, tablename=nil)`

Returns a list of all constraints in the schema reachable through `conn`.
If `tablename` is given, returns the constraints in only that table.

`#dependencies(conn)`

Returns a structure representing the dependencies between tables in the schema reachable through `conn`.
Table A is defined as dependent on table B if A contains a foreign key reference to B.

`#tables_in_dependency_order(conn)`

Returns a list of all tables in the schema reachable through `conn`, ordered such that any given table
appears later in the list than all of its dependencies.

`#dependency_graph(conn)`

Returns `.dot` script (suitable for feeding into Graphviz) describing the table dependency graph.

`#functions(conn)`

Returns a list of all functions in the schema reachable through `conn`.

`#sequences(conn)`

Returns a list of all sequences in the schema reachable through `conn`.

`#triggers(conn)`

Returns a list of all triggers in the schema reachable through `conn`.

`#types(conn)`

Returns a list of all types in the schema reachable through `conn`.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## 官网

- 文档: https://www.rubydoc.info/gems/gadget/0.7.0
- RubyGems: https://rubygems.org/gems/gadget

## 历史版本号

- 0.7.0 (2016-11-01)
- 0.6.2 (2015-02-05)
- 0.6.1 (2014-09-10)
- 0.6.0 (2014-03-26)
- 0.5.4 (2014-03-25)
- 0.5.2 (2014-02-26)
- 0.5.1 (2014-02-26)
- 0.5.0 (2014-02-26)
- 0.4.1 (2014-02-21)
- 0.4.0 (2014-02-20)
- 0.3.2 (2014-02-20)
- 0.3.1 (2014-02-20)
- 0.3.0 (2014-02-20)
- 0.2.1 (2014-02-19)
- 0.2.0 (2014-02-19)
- 0.1.0 (2014-01-28)
- 0.0.2 (2014-01-27)
- 0.0.1 (2014-01-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/gadget
- gem 安装: `gem install gadget`
- Bundler: `gem "gadget"`
- 最新版本: 0.7.0
- 最新版归档: https://rubygems.org/downloads/gadget-0.7.0.gem
- 版本锁定: `gem "gadget", "~> 0.7.0"`
- 中央仓库: https://rubygems.org/
