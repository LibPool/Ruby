# combinaut_rehearsal

**Tag**: web, database, template, data

## 简介

Rehearsal is a Rack Middleware gem that allows model changes to be previewed without persisting them to the database. It achieves this by intercepting the original update request and spawning a second request to Rails for a preview, wrapping both in a single database transaction that is rolled back after the preview is generated.

## 官网

- 主页: http://github.com/combinaut/rehearsal
- 文档: https://www.rubydoc.info/gems/combinaut_rehearsal/0.1.4
- RubyGems: https://rubygems.org/gems/combinaut_rehearsal

## 历史版本号

- 0.1.4 (2020-03-19)
- 0.1.3 (2019-10-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/combinaut_rehearsal
- gem 安装: `gem install combinaut_rehearsal`
- Bundler: `gem "combinaut_rehearsal"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/combinaut_rehearsal-0.1.4.gem
- 版本锁定: `gem "combinaut_rehearsal", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
