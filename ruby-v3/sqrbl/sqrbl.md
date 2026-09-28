# sqrbl

**Tag**: database, testing, data

## 简介

SQrbL was created to help manage an extremely specific problem:  managing SQL-based database conversions.

In essence, SQrbL is a tool for managing multiple SQL queries using Ruby.  SQrbL borrows some terminology and ideas from ActiveRecord's schema migrations, but where ActiveRecord manages changes to your database schema over time, SQrbL was written to manage the process of transforming your data from one schema to another.  (Of course, you could use SQrbL for the former case as well -- just use it to write DDL queries -- but ActiveRecord has better tools for figuring out which migrations have already been applied.)

## 官网

- 主页: http://sqrbl.rubyforge.org
- RubyGems: https://rubygems.org/gems/sqrbl

## 历史版本号

- 0.2.0 (2009-09-24)
- 0.1.0 (2009-08-07)
- 0.1.1 (2009-08-07)
- 0.1.2 (2009-08-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/sqrbl
- gem 安装: `gem install sqrbl`
- Bundler: `gem "sqrbl"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/sqrbl-0.2.0.gem
- 版本锁定: `gem "sqrbl", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
