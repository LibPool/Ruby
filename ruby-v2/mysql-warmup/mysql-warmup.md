# mysql-warmup

**Tag**: database

## 简介

When you've just created new slave instance, first requests to DB (with InnoDB storage engine)
    will be hit on disk instead of buffer poll. So, the requests will be slow down.
    You can use this tool for warming up buffer poll before the first requests come.
    Please see document for other cases.

## 官网

- 主页: https://github.com/manhdaovan/mysql_warmup
- 文档: https://www.rubydoc.info/gems/mysql-warmup/0.0.3
- RubyGems: https://rubygems.org/gems/mysql-warmup

## 历史版本号

- 0.0.3 (2017-01-15)
- 0.0.2 (2017-01-14)
- 0.0.1 (2017-01-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/mysql-warmup
- gem 安装: `gem install mysql-warmup`
- Bundler: `gem "mysql-warmup"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/mysql-warmup-0.0.3.gem
- 版本锁定: `gem "mysql-warmup", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
