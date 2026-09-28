# gemfile_lock_to_gemfile

**Tag**: tooling, devops, filesystem

## 简介

## Why I have to develop this tool

One of my ruby project is using bundler to manage gem dependencies. But the `Gemfile` is very complicate. It requires external `Gemfile` by using ruby `eval`. Because I have lots of similar projects that will use same piece of gems. So I decide to abstract these gems into a standalone `Gemfile`. And let those projects’ `Gemfile` loads it.

The problem I met is when I building my docker image. I hope that image can pre-install all the ruby gems in that `Gemfile.lock`. Unluckily, `bundle install` require you must have the `Gemfile`. So I have to find out a way to revert `Gemfile.lock` to a usable `Gemfile`.

So here we are!

## 官网

- 主页: https://github.com/agate/gemfile_lock_to_gemfile
- 文档: https://www.rubydoc.info/gems/gemfile_lock_to_gemfile/0.1.2
- RubyGems: https://rubygems.org/gems/gemfile_lock_to_gemfile

## 历史版本号

- 0.1.2 (2017-01-03)
- 0.1.1 (2017-01-03)
- 0.1.0 (2017-01-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/gemfile_lock_to_gemfile
- gem 安装: `gem install gemfile_lock_to_gemfile`
- Bundler: `gem "gemfile_lock_to_gemfile"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/gemfile_lock_to_gemfile-0.1.2.gem
- 版本锁定: `gem "gemfile_lock_to_gemfile", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
