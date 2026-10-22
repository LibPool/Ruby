# kettle-paths

**Tag**: filesystem

## 简介

Path helpers that compare two filesystem paths by identity (inode / file
index) rather than by string, so a directory spelled two valid ways still
compares equal: symlinked ancestors (/home/x vs /var/home/x) and Windows
8.3 short names (RUNNER~1 vs runneradmin). Pure Ruby, no dependencies, so it
can be shared across MIT and AGPL tooling.

## 官网

- 主页: https://github.com/pboling/kettle-paths
- 源码仓库: https://github.com/pboling/kettle-paths/tree/v0.1.1
- 文档: https://www.rubydoc.info/gems/kettle-paths/0.1.1
- 更新日志: https://github.com/pboling/kettle-paths/blob/v0.1.1/CHANGELOG.md
- 问题追踪: https://github.com/pboling/kettle-paths/issues
- RubyGems: https://rubygems.org/gems/kettle-paths

## 历史版本号

- 0.1.1 (2026-10-15)
- 0.1.0 (2026-10-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/kettle-paths
- gem 安装: `gem install kettle-paths`
- Bundler: `gem "kettle-paths"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/kettle-paths-0.1.1.gem
- 版本锁定: `gem "kettle-paths", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
