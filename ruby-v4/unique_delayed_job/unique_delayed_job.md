# unique_delayed_job

**Tag**: testing

## 简介

Class for creating delayed jobs that can be de-duped with existing delayed jobs
already in the delayed jobs table. You just specify some additional columns on
your delayed_jobs table and set them to have uniqueness constraints. Then
specify these column values when you create a UniqueDelayedJob and if a
duplicate key is raised on insert, then the insert will just be ignored. There
are factory methods for creating a delayed job in the following ways:
* with a delayed job handler class (one that responds to perform())
* with an object, method and method arguments
* with a code string to be evaled

NOTE: you must have delayed_job installed as a gem or plugin

## 官网

- 主页: http://github.com/bmpercy/unique_delayed_job
- RubyGems: https://rubygems.org/gems/unique_delayed_job

## 历史版本号

- 0.1.1 (2009-11-20)
- 0.1.0 (2009-11-19)
- 0.0.1 (2009-11-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/unique_delayed_job
- gem 安装: `gem install unique_delayed_job`
- Bundler: `gem "unique_delayed_job"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/unique_delayed_job-0.1.1.gem
- 版本锁定: `gem "unique_delayed_job", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
