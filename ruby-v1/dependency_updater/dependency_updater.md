# dependency_updater

**Tag**: testing, filesystem

## 简介

This tool
1. create's a new branch
2. runs 'bundle update'
3. find's the latest patch-level version of Ruby and updates files that reference the version
4a. commit's the updates and pushes to gitlab, creating a new merge request
4b. delete's the branch if no updates were made

## 官网

- 主页: https://gitlab.med.upenn.edu/infrastructure/dependency-updater.git
- 文档: https://www.rubydoc.info/gems/dependency_updater/0.1.1
- RubyGems: https://rubygems.org/gems/dependency_updater

## 历史版本号

- 0.1.1 (2021-04-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/dependency_updater
- gem 安装: `gem install dependency_updater`
- Bundler: `gem "dependency_updater"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/dependency_updater-0.1.1.gem
- 版本锁定: `gem "dependency_updater", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
