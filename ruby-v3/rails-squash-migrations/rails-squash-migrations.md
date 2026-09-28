# rails-squash-migrations

**Tag**: web, cli, testing, networking, tooling, devops

## 简介

# Squash Migrations

Periodically squash migrations to reduce overhead of the `db:migrate` Rake
task.

## Creating a release

1. Create a new pull request that:

- Bumps the version in `rails-squash-migrations.gemspec`
- Updates `CHANGELOG.md` to include all noteworthy changes, the release
  version, and the release date.

2. After the pull request lands, checkout the most up to date `main` branch and
   build the gem:

```console
$ docker run --rm -it -v $(pwd):$(pwd) -w $(pwd) ruby gem build
```

3. Publish the gem:

   ```console
   $ docker run --rm -it -v $(pwd):$(pwd) -w $(pwd) ruby gem push rails-squash-migrations-X.Y.Z.gem
   ```

4. Create and publish a git tag:

   ```console
   $ git tag X.Y.Z
   $ git push https://github.com/Pioneer-Valley-Books/rails-squash-migrations.git X.Y.Z
   ```

## 官网

- 主页: https://github.com/Pioneer-Valley-Books/rails-squash-migrations
- 文档: https://www.rubydoc.info/gems/rails-squash-migrations/1.0.0
- RubyGems: https://rubygems.org/gems/rails-squash-migrations

## 历史版本号

- 1.0.0 (2026-01-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails-squash-migrations
- gem 安装: `gem install rails-squash-migrations`
- Bundler: `gem "rails-squash-migrations"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/rails-squash-migrations-1.0.0.gem
- 版本锁定: `gem "rails-squash-migrations", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
