# bulk_destroyer

**Tag**: library

## 简介

BulkDestroyer destroys a relation (and its dependent: :destroy tree) while firing every
destroy callback on every record, but issues one SELECT per association per level and one
DELETE per table per level instead of one DELETE per row. Works on any ActiveRecord adapter.

## 官网

- 主页: https://github.com/rneelakantan/bulk_destroyer
- 更新日志: https://github.com/rneelakantan/bulk_destroyer/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/rneelakantan/bulk_destroyer/issues
- RubyGems: https://rubygems.org/gems/bulk_destroyer

## 历史版本号

- 0.1.0 (2026-10-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/bulk_destroyer
- gem 安装: `gem install bulk_destroyer`
- Bundler: `gem "bulk_destroyer"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/bulk_destroyer-0.1.0.gem
- 版本锁定: `gem "bulk_destroyer", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
