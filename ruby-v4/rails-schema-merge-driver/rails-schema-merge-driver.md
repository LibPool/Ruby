# rails-schema-merge-driver

**Tag**: web, filesystem, data

## 简介

A custom git merge driver that auto-resolves the most common conflict in Rails schema files (db/schema.rb and, with the data_migrate gem, db/data_schema.rb): the define(version: N) line that gets bumped on every migration. Keeps the higher version on conflict and falls back to a normal merge conflict for any other diverging content.

## 官网

- 主页: https://github.com/tmaier/rails-schema-merge-driver
- 文档: https://github.com/tmaier/rails-schema-merge-driver/blob/main/README.md
- 更新日志: https://github.com/tmaier/rails-schema-merge-driver/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/tmaier/rails-schema-merge-driver/issues
- RubyGems: https://rubygems.org/gems/rails-schema-merge-driver

## 历史版本号

- 0.1.1 (2026-04-26)
- 0.1.0 (2026-04-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails-schema-merge-driver
- gem 安装: `gem install rails-schema-merge-driver`
- Bundler: `gem "rails-schema-merge-driver"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/rails-schema-merge-driver-0.1.1.gem
- 版本锁定: `gem "rails-schema-merge-driver", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
