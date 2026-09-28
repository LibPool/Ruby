# file_overwrite

**Tag**: testing, filesystem

## 简介

This class provides a Ruby-oriented scheme to safely overwrite an existing file, leaving a backup file unless specified otherwise.  It writes a temporary file first, which is renamed to the original file in one action.  It accepts a block like some IO class-methods (e.g., each_line) and chaining like String methods (e.g., sub and gsub).

## 官网

- 主页: https://www.wisebabel.com
- 文档: https://www.rubydoc.info/gems/file_overwrite/1.0
- RubyGems: https://rubygems.org/gems/file_overwrite

## 历史版本号

- 1.0 (2018-10-13)
- 0.1 (2018-09-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/file_overwrite
- gem 安装: `gem install file_overwrite`
- Bundler: `gem "file_overwrite"`
- 最新版本: 1.0
- 最新版归档: https://rubygems.org/downloads/file_overwrite-1.0.gem
- 版本锁定: `gem "file_overwrite", "~> 1.0"`
- 中央仓库: https://rubygems.org/
