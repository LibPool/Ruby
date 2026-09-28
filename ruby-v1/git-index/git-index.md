# git-index

**Tag**: database, devops, filesystem, data

## 简介

This tool takes a list of paths and checks them for git repositories. It
writes to a sqlite database a table of repositories found, indexed by both
the first and the second commit hashes on the repository. The rationale is
that these first couple of commits are unlikely to ever change as the
result of a rebase, and thus make a fairly reliable fingerprint of the
identity of the repository. The motivation behind this tool is for use with
Serf and the serf-hander gem to power a slick, simple deployment manger
utiizing a git repo and deploy hooks at the underlying source and trigger.

## 官网

- 主页: https://github.com/wyhaines/git-index
- 问题追踪: https://github.com/wyhaines/git-index/issues
- RubyGems: https://rubygems.org/gems/git-index

## 历史版本号

- 1.0.2 (2018-01-23)
- 1.0.1 (2018-01-22)

## 获取地址

- RubyGems: https://rubygems.org/gems/git-index
- gem 安装: `gem install git-index`
- Bundler: `gem "git-index"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/git-index-1.0.2.gem
- 版本锁定: `gem "git-index", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
