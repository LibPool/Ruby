# paper_trail-bulk_writes

**Tag**: library

## 简介

Bulk ActiveRecord writes skip callbacks, so PaperTrail records nothing. This gem adds
audited_update_all, audited_delete_all and audited_insert_all, which run the bulk write
and insert one version row per record in the same transaction, honouring the model's
only:, ignore:, skip:, meta: and versions: options. Ships a RuboCop cop that flags
bare bulk writes on audited models.

## 官网

- 主页: https://github.com/Sam-Robin/paper_trail-bulk_writes
- 更新日志: https://github.com/Sam-Robin/paper_trail-bulk_writes/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/paper_trail-bulk_writes

## 历史版本号

- 0.3.0 (2026-10-09)
- 0.2.0 (2026-09-30)
- 0.1.0 (2026-09-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/paper_trail-bulk_writes
- gem 安装: `gem install paper_trail-bulk_writes`
- Bundler: `gem "paper_trail-bulk_writes"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/paper_trail-bulk_writes-0.3.0.gem
- 版本锁定: `gem "paper_trail-bulk_writes", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
