# rails-rebase-migrations

**Tag**: web, cli, database, testing, filesystem, data

## 简介

# Rebase Migrations

Rebase Migrations is a library and command line tool to rebase Rails migrations
to have the latest timestamp.

## Installation

```console
$ bundle add rails-rebase-migrations --group=development,test
```

## Scenario

Two team members, Alice and Bob, are working on the same Rails project and both
are adding new database migrations. Alice realizes her migration depends on
Bob's, but the migration timestamps are out of order. The `rebase-migration`
command line tool can be used to reorder Alice's new migrations to have the
latest timestamp in the sequence.

## Usage

To rebase all new migrations with respect to the `main` git branch:

```console
$ bundle exec rebase-migrations
```

To rebase all new migrations with respect to a different branch:

```console
$ bundle exec rebase-migrations my-branch
```

The command has a `--check` argument that is useful for CI. To check that all
new migrations are the latest in the sequence:

```console
$ bundle exec rebase-migrations --check
```

It will exit with status code 1 if the check fails. The `--check` form also
accepts a branch argument.

### Skipping Migrations

To skip a specific migration files from the `--check` include `_skip_rebase` in
its filename.

## 官网

- 主页: https://github.com/Pioneer-Valley-Books/rebase-migrations
- 文档: https://www.rubydoc.info/gems/rails-rebase-migrations/1.5.0
- RubyGems: https://rubygems.org/gems/rails-rebase-migrations

## 历史版本号

- 1.5.0 (2026-02-05)
- 1.4.0 (2025-06-16)
- 1.3.0 (2024-11-13)
- 1.2.0 (2024-03-14)
- 1.1.0 (2024-03-04)
- 1.0.1 (2022-10-28)
- 1.0.0 (2022-10-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails-rebase-migrations
- gem 安装: `gem install rails-rebase-migrations`
- Bundler: `gem "rails-rebase-migrations"`
- 最新版本: 1.5.0
- 最新版归档: https://rubygems.org/downloads/rails-rebase-migrations-1.5.0.gem
- 版本锁定: `gem "rails-rebase-migrations", "~> 1.5.0"`
- 中央仓库: https://rubygems.org/
