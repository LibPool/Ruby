# context

**Tag**: testing, template, data

## 简介

Context is a contextual UI framework.  It is based on the
	    Model View Presentor model.  The idea is that you have model
	    objects that represent the core data in your application.  You 
	    also have views that represent the user interface input and output.
	    Finally you have "contexts" that represent a user situation in
	    the application.  The logic that ties the models and views resides
	    in the contexts.  The main advantages to this model are that
	    you can easily write UI unit tests and you can easily create
	    bridge patterns for supporting multiple widget sets (although only
	    GTK+ is supported at the moment).  Context is intended to be
	    extremely minimal.  Only the top level abstract classes are
	    included.  It is *not* a widget set!  You have to write your
	    own models, views and contexts.

## 官网

- 主页: http://sakabatou.dnsdojo.org
- RubyGems: https://rubygems.org/gems/context

## 历史版本号

- 0.0.22 (2011-01-24)
- 0.0.16 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/context
- gem 安装: `gem install context`
- Bundler: `gem "context"`
- 最新版本: 0.0.22
- 最新版归档: https://rubygems.org/downloads/context-0.0.22.gem
- 版本锁定: `gem "context", "~> 0.0.22"`
- 中央仓库: https://rubygems.org/
