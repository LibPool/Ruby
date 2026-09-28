# cosine-quacks-like

**Tag**: web, testing

## 简介

QuacksLike is a module for RSpec to add matchers that test if an object is fully duck-typed to pretend to be another class.  This kind of thing is really only necessary when passing such an object as the return value in an API where you don't know exactly how it will be consumed, but it needs to "quack like an Array" or something.  It does its job by checking every instance method in the class that the target object needs to "quack like" and makes sure the target both responds to that method name and that the arity of the method is appropriate.

## 官网

- 主页: http://cosine.org/ruby/QuacksLike/
- 文档: https://www.rubydoc.info/gems/cosine-quacks-like/1.0.0
- RubyGems: https://rubygems.org/gems/cosine-quacks-like

## 历史版本号

- 1.0.0 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/cosine-quacks-like
- gem 安装: `gem install cosine-quacks-like`
- Bundler: `gem "cosine-quacks-like"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/cosine-quacks-like-1.0.0.gem
- 版本锁定: `gem "cosine-quacks-like", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
