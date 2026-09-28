# mongoid-history-patched

**Tag**: web, filesystem

## 简介

In frustration of Mongoid::Versioning, I created this plugin for tracking historical changes for any document, including embedded ones. It achieves this by storing all history tracks in a single collection that you define. (See Usage for more details) Embedded documents are referenced by storing an association path, which is an array of document_name and document_id fields starting from the top most parent document and down to the embedded document that should track history.

  This plugin implements multi-user undo, which allows users to undo any history change in any order. Undoing a document also creates a new history track. This is great for auditing and preventing vandalism, but it is probably not suitable for use cases such as a wiki.

## 官网

- 主页: http://github.com/aq1018/mongoid-history
- RubyGems: https://rubygems.org/gems/mongoid-history-patched

## 历史版本号

- 0.2.3 (2012-10-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/mongoid-history-patched
- gem 安装: `gem install mongoid-history-patched`
- Bundler: `gem "mongoid-history-patched"`
- 最新版本: 0.2.3
- 最新版归档: https://rubygems.org/downloads/mongoid-history-patched-0.2.3.gem
- 版本锁定: `gem "mongoid-history-patched", "~> 0.2.3"`
- 中央仓库: https://rubygems.org/
