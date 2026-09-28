# mtime_cache

**Tag**: tooling, filesystem

## 简介

mtime_cache creates a cache of file modification times, based on a glob pattern.
If a cache exists it updates unchanged files (unchanged based on MD5 hash) with
the time from the cache.

This is useful if you cache your build artifacts for a build process which
detects changes based on source modification time (such as most C or C++ build
systems) on a continuous integration service (such as Travis CI), which clones
the repo for every build.

When the repo is cloned, all source files have a modification time equal to the
current time, making the cached build artifacts (for example .o files) obsolete.
mtime_cache allows you to cache the modification times of the files, enabling a
minimal rebuild for each clone.

## 官网

- 主页: https://github.com/iboB/mtime_cache
- 文档: https://www.rubydoc.info/gems/mtime_cache/1.0.2
- RubyGems: https://rubygems.org/gems/mtime_cache

## 历史版本号

- 1.0.2 (2016-10-27)
- 1.0.0 (2016-10-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/mtime_cache
- gem 安装: `gem install mtime_cache`
- Bundler: `gem "mtime_cache"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/mtime_cache-1.0.2.gem
- 版本锁定: `gem "mtime_cache", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
