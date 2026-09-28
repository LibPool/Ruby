# sequel_pg_extended_columns

**Tag**: database, data

## 简介

sequel_pg overwrites the inner loop of the Sequel postgres
adapter row fetching code with a C version.  The C version
is significantly faster than the pure ruby version
that Sequel uses by default.

sequel_pg also offers optimized versions of some dataset
methods, as well as adds support for using PostgreSQL
streaming.

## 官网

- 主页: https://github.com/mansoorkhan108/sequel_pg
- 源码仓库: https://github.com/jeremyevans/sequel_pg
- 文档: https://github.com/jeremyevans/sequel_pg/blob/master/README.rdoc
- 更新日志: https://github.com/jeremyevans/sequel_pg/blob/master/CHANGELOG
- 问题追踪: https://github.com/jeremyevans/sequel_pg/issues
- RubyGems: https://rubygems.org/gems/sequel_pg_extended_columns

## 历史版本号

- 1.6.19 (2021-11-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/sequel_pg_extended_columns
- gem 安装: `gem install sequel_pg_extended_columns`
- Bundler: `gem "sequel_pg_extended_columns"`
- 最新版本: 1.6.19
- 最新版归档: https://rubygems.org/downloads/sequel_pg_extended_columns-1.6.19.gem
- 版本锁定: `gem "sequel_pg_extended_columns", "~> 1.6.19"`
- 中央仓库: https://rubygems.org/
