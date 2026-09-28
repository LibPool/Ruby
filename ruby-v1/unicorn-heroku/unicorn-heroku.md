# unicorn-heroku

**Tag**: library

## 简介

\This is a fork of Unicorn designed to run on Heroku. Heroku and Unicorn
disagree on signal handling, so I've swapped Unicorn's handling of
SIGINT/SIGTERM and SIGQUIT. Now, Unicorn can shut down gracefully on
Heroku.

## 官网

- 主页: http://unicorn.bogomips.org/
- RubyGems: https://rubygems.org/gems/unicorn-heroku

## 历史版本号

- 4.3.1.1.gc608.dirty (2012-05-29)

## 获取地址

- RubyGems: https://rubygems.org/gems/unicorn-heroku
- gem 安装: `gem install unicorn-heroku`
- Bundler: `gem "unicorn-heroku"`
- 最新版本: 4.3.1.1.gc608.dirty
- 最新版归档: https://rubygems.org/downloads/unicorn-heroku-4.3.1.1.gc608.dirty.gem
- 版本锁定: `gem "unicorn-heroku", "~> 4.3.1.1.gc608.dirty"`
- 中央仓库: https://rubygems.org/
