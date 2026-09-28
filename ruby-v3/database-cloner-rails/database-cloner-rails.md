# database-cloner-rails

**Tag**: web, database, testing, filesystem, data

## 简介

database-cloner-rails provides two rake tasks for moving database records between
Rails environments. `rake database:download` dumps all ActiveRecord model records
to plain Ruby files (Model.create(...) statements). `rake database:upload` replays
those files to restore records in the target database.

Useful for seeding a staging environment from production data, creating snapshots
before destructive migrations, or sharing realistic test data across a team.

Supports optional MODELS filtering: `rake database:download MODELS=users,posts`
to dump only specific tables. The dump directory is created automatically.

## 官网

- 主页: https://github.com/abhsss96/database-cloner-rails
- 更新日志: https://github.com/abhsss96/database-cloner-rails/releases
- 问题追踪: https://github.com/abhsss96/database-cloner-rails/issues
- RubyGems: https://rubygems.org/gems/database-cloner-rails

## 历史版本号

- 1.1.1 (2026-05-31)
- 1.1.0 (2026-05-31)
- 1.0.1 (2026-05-31)
- 1.0 (2014-12-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/database-cloner-rails
- gem 安装: `gem install database-cloner-rails`
- Bundler: `gem "database-cloner-rails"`
- 最新版本: 1.1.1
- 最新版归档: https://rubygems.org/downloads/database-cloner-rails-1.1.1.gem
- 版本锁定: `gem "database-cloner-rails", "~> 1.1.1"`
- 中央仓库: https://rubygems.org/
