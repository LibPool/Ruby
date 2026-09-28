# germinator

**Tag**: web, database, devops, filesystem, data

## 简介

Rails allows incremental database migrations, but only provides a single seed file (non-incremental) that causes problems when you try to run it during each application deploy. Germinate provides a process very similar to the Rails database migrations that allows you to ensure that a data seed only gets run once in each environment. It also provides a way to limit which Rails environments are allowed to run particular seeds, which helps protect data in sensitive environments (e.g. Production).

## 官网

- 文档: https://www.rubydoc.info/gems/germinator/2.1.1
- RubyGems: https://rubygems.org/gems/germinator

## 历史版本号

- 2.1.1 (2024-11-05)
- 2.1.0 (2024-03-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/germinator
- gem 安装: `gem install germinator`
- Bundler: `gem "germinator"`
- 最新版本: 2.1.1
- 最新版归档: https://rubygems.org/downloads/germinator-2.1.1.gem
- 版本锁定: `gem "germinator", "~> 2.1.1"`
- 中央仓库: https://rubygems.org/
