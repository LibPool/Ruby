# nostalgia

**Tag**: testing

## 简介

Often I want to evaluate what changed on an object after it has saved and has been transactionally committed.  One use case is enqueuenig a background job when a specific attribute changed.  Typically you should wait until after_commit to enqueue the job.  This ensures that your workers will have access to the updates that were being made inside the transaction. This is a problem because ActiveRecord forgets the changes after_save.  This gem keeps those changes around for later inspection and evaluation.

## 官网

- 主页: http://github.com/AcademicWorks/nostalgia
- RubyGems: https://rubygems.org/gems/nostalgia

## 历史版本号

- 0.0.1 (2013-04-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/nostalgia
- gem 安装: `gem install nostalgia`
- Bundler: `gem "nostalgia"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/nostalgia-0.0.1.gem
- 版本锁定: `gem "nostalgia", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
