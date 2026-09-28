# pg_jbuilder

**Tag**: web, database, serialization, networking, template, tooling, data

## 简介

pg_jbuilder is a tool to dump database queries directly to a JSON object or array. It uses PostgreSQL's JSON functions ([array_to_json and row_to_json](http://www.postgresql.org/docs/9.3/static/functions-json.html)) to serialize the JSON completely bypassing ActiveRecord/Arel. This gives a large speed boost compared to serializing the JSON inside of Ruby/Rails. It is perfect for creating JSON APIs with very low response times.

## 官网

- 文档: https://www.rubydoc.info/gems/pg_jbuilder/0.0.1
- RubyGems: https://rubygems.org/gems/pg_jbuilder

## 历史版本号

- 0.0.1 (2015-03-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/pg_jbuilder
- gem 安装: `gem install pg_jbuilder`
- Bundler: `gem "pg_jbuilder"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/pg_jbuilder-0.0.1.gem
- 版本锁定: `gem "pg_jbuilder", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
