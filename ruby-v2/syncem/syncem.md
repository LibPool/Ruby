# syncem

**Tag**: database, filesystem, data

## 简介

Sometimes you have an object that is not thread-safe,
but you need to make sure each of its methods is thread-safe, because they
deal with some resources, like files or databases and you want them to
manage those resources sequentially. This small gem will help you achieve
exactly that without any re-design of the objects you already have. Just
decorate them with SyncEm decorator and that is it.

## 官网

- 主页: http://github.com/yegor256/syncem
- 文档: https://www.rubydoc.info/gems/syncem/0.2.0
- RubyGems: https://rubygems.org/gems/syncem

## 历史版本号

- 0.2.0 (2023-11-13)
- 0.1.2 (2019-06-23)
- 0.1.1 (2019-04-13)
- 0.1.0 (2019-03-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/syncem
- gem 安装: `gem install syncem`
- Bundler: `gem "syncem"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/syncem-0.2.0.gem
- 版本锁定: `gem "syncem", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
