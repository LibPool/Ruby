# unsort_db_schema_columns

**Tag**: web, database, data

## 简介

Rails 8 (PR #53281) sorts schema.rb columns alphabetically. That breaks
db:schema:load parity with production, Postgres column-alignment padding,
add_column :after/:before, and bulk-import pipelines that depend on
SELECT * column order. This gem prepends ActiveRecord::SchemaDumper to
dump columns in the order the database actually stores them.

## 官网

- 主页: https://github.com/jakeonrails/unsort-db-schema-columns
- 更新日志: https://github.com/jakeonrails/unsort-db-schema-columns/blob/main/README.md
- 问题追踪: https://github.com/jakeonrails/unsort-db-schema-columns/issues
- RubyGems: https://rubygems.org/gems/unsort_db_schema_columns

## 历史版本号

- 0.1.0 (2026-05-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/unsort_db_schema_columns
- gem 安装: `gem install unsort_db_schema_columns`
- Bundler: `gem "unsort_db_schema_columns"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/unsort_db_schema_columns-0.1.0.gem
- 版本锁定: `gem "unsort_db_schema_columns", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
