# draft_punk

**Tag**: database, testing, networking, data

## 简介

DraftPunk allows editing of a draft version of an ActiveRecord model and its associations.

When it's time to edit, a draft version is created in the same table as the object. You can specify which associations should also be edited and stored with that draft version. All associations are stored in their native table.

When it's time to publish, any attributes changed on your draft object persist to the original object. All associated objects behave the same way. Any associated have_many objects which are deleted on the draft are deleted on the original object.

This gem doesn't rely on a versioning gem and doesn't store incremental diffs of the model. It simply works with your existing database (plus one new column on your original object).

## 官网

- 主页: https://github.com/stevehodges/draftpunk
- 文档: https://www.rubydoc.info/gems/draft_punk/0.3.1
- RubyGems: https://rubygems.org/gems/draft_punk

## 历史版本号

- 0.3.1 (2018-12-04)
- 0.3.0 (2018-09-28)
- 0.2.8 (2018-08-28)
- 0.2.7 (2017-03-31)
- 0.2.6 (2016-12-09)
- 0.2.5 (2016-10-18)
- 0.2.4 (2016-10-04)
- 0.2.3 (2016-05-31)
- 0.2.2 (2016-01-22)
- 0.2.1 (2016-01-19)
- 0.1.0 (2016-01-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/draft_punk
- gem 安装: `gem install draft_punk`
- Bundler: `gem "draft_punk"`
- 最新版本: 0.3.1
- 最新版归档: https://rubygems.org/downloads/draft_punk-0.3.1.gem
- 版本锁定: `gem "draft_punk", "~> 0.3.1"`
- 中央仓库: https://rubygems.org/
