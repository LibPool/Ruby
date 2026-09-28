# archival_record

**Tag**: filesystem

## 简介

*Atomic archiving/unarchiving for ActiveRecord*

acts_as_paranoid and similar plugins/gems work on a record-by-record basis and make it difficult to restore records atomically (or archive them, for that matter).

Because ArchivalRecord's #archive! and #unarchive! methods are in transactions, and every archival record involved gets the same archive number upon archiving, you can easily restore or remove an entire set of records without having to worry about partial deletion or restoration.

Additionally, other plugins generally change how destroy/delete work. ArchivalRecord does not, and thus one can destroy records like normal.

## 官网

- 主页: https://codeberg.org/joelmeador/archival_record/
- 更新日志: https://codeberg.org/joelmeador/archival_record/src/branch/main/CHANGELOG.md
- 问题追踪: https://codeberg.org/joelmeador/archival_record/issues
- RubyGems: https://rubygems.org/gems/archival_record

## 历史版本号

- 4.0.1 (2025-03-25)
- 4.0.0 (2025-03-20)
- 3.0.1 (2024-06-11)
- 3.0.0 (2024-06-11)
- 2.0.2 (2020-08-04)
- 2.0.1 (2020-08-03)
- 2.0.0 (2020-08-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/archival_record
- gem 安装: `gem install archival_record`
- Bundler: `gem "archival_record"`
- 最新版本: 4.0.1
- 最新版归档: https://rubygems.org/downloads/archival_record-4.0.1.gem
- 版本锁定: `gem "archival_record", "~> 4.0.1"`
- 中央仓库: https://rubygems.org/
