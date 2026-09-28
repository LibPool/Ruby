# pessimizer

**Tag**: web, testing, filesystem

## 简介

Add the pessimistic constraint operator to all gems in your Gemfile, restricting the maximum update version.

This is for people who work with projects that use bundler, such as rails projects. The pessimistic constraint operator (~>) allows you to specify the maximum version that a gem can be updated, and reduces potential breakages when running `bundle update`. Pessimize automatically retrieves the current versions of your gems, then adds them to your Gemfile (so you don't have to do it by hand).

## 官网

- 主页: https://github.com/iachettifederico/pessimizer
- 文档: https://www.rubydoc.info/gems/pessimizer/1.0.0
- RubyGems: https://rubygems.org/gems/pessimizer

## 历史版本号

- 1.0.0 (2023-01-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/pessimizer
- gem 安装: `gem install pessimizer`
- Bundler: `gem "pessimizer"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/pessimizer-1.0.0.gem
- 版本锁定: `gem "pessimizer", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
