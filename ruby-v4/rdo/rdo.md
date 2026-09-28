# rdo

**Tag**: web, database, tooling, data

## 简介

== Ruby Data Objects

If you're building something in Ruby that needs access to a database, you may
opt to use an ORM like ActiveRecord, DataMapper or Sequel. But if your needs
don't fit well with an ORM—maybe you're even writing an ORM—then you'll
need some other way of talking to your database.

RDO provides a common interface to a number of RDBMS backends, using a clean
Ruby syntax, while supporting all the functionality you'd expect from a robust
database connection library:

  * Consistent API to connect to various DBMS's
  * Type casting to Ruby types
  * Time zone handling (via the DBMS, not via some crazy time logic in Ruby)
  * Native bind values parameterization of queries, where supported by the DBMS
  * Retrieve query info from executed commands (e.g. affected rows)
  * Access RETURNING values just like any read query
  * Native prepared statements where supported, emulated where not
  * Results given using simple core Ruby data types

== RDBMS Support

Support for each RDBMS is provided in separate gems, so as to minimize the
installation requirements and to facilitate the maintenace of each driver. Many
gems are maintained by separate users who work more closely with those RDBMS's.

Due to the nature of this gem, most of the nitty-gritty code is actually
written in C.

See the official README for full details.

## 官网

- 主页: https://github.com/d11wtq/rdo
- RubyGems: https://rubygems.org/gems/rdo

## 历史版本号

- 0.1.8 (2012-10-28)
- 0.1.7 (2012-10-24)
- 0.1.6 (2012-10-14)
- 0.1.5 (2012-10-11)
- 0.1.4 (2012-10-11)
- 0.1.3 (2012-10-11)
- 0.1.2 (2012-10-11)
- 0.1.1 (2012-10-11)
- 0.1.0 (2012-10-10)
- 0.0.8 (2012-09-30)
- 0.0.7 (2012-09-27)
- 0.0.6 (2012-09-24)
- 0.0.5 (2012-09-24)
- 0.0.4 (2012-09-24)
- 0.0.3 (2012-09-24)
- 0.0.2 (2012-09-24)
- 0.0.1 (2012-09-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/rdo
- gem 安装: `gem install rdo`
- Bundler: `gem "rdo"`
- 最新版本: 0.1.8
- 最新版归档: https://rubygems.org/downloads/rdo-0.1.8.gem
- 版本锁定: `gem "rdo", "~> 0.1.8"`
- 中央仓库: https://rubygems.org/
