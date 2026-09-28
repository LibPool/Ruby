# jsonapi-query_builder

**Tag**: web, database, serialization, tooling

## 简介

`Jsonapi::QueryBuilder` serves the purpose of adding the json api query related SQL conditions to the already scoped collection, usually used in controller index actions.

With the query builder we can easily define logic for query filters, attributes by which we can sort, and delegate pagination parameters to the underlying paginator. Included relationships are automatically included via the `ActiveRecord::QueryMethods#includes`, to prevent N+1 query problems.

## 官网

- 主页: https://github.com/infinum/jsonapi-query_builder
- 更新日志: https://github.com/infinum/jsonapi-query_builder/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/jsonapi-query_builder

## 历史版本号

- 0.4.0 (2025-11-03)
- 0.3.0 (2021-12-07)
- 0.2.1 (2021-10-04)
- 0.2.0 (2021-09-29)
- 0.1.9 (2021-05-07)
- 0.1.8 (2021-01-25)
- 0.1.7 (2021-01-19)
- 0.1.6.pre (2020-09-01)
- 0.1.5.pre (2020-08-31)
- 0.1.4.pre (2020-08-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/jsonapi-query_builder
- gem 安装: `gem install jsonapi-query_builder`
- Bundler: `gem "jsonapi-query_builder"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/jsonapi-query_builder-0.4.0.gem
- 版本锁定: `gem "jsonapi-query_builder", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
