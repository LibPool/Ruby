# upcastable

**Tag**: testing

## 简介

Duck typing sometimes results in `NoMethodError` unexpectedly by calling methods
some classes don't have even if the code pass a test using other classes which
have the methods. We can avoid such situations by upcasting.
All we have to do is implementing methods defined in the super class or module
and we don't have to care about whether or not methods defined only in some
subclasses are called.

## 官网

- 主页: https://github.com/abicky/upcastable
- 文档: https://www.rubydoc.info/gems/upcastable/0.1.0
- RubyGems: https://rubygems.org/gems/upcastable

## 历史版本号

- 0.1.0 (2016-01-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/upcastable
- gem 安装: `gem install upcastable`
- Bundler: `gem "upcastable"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/upcastable-0.1.0.gem
- 版本锁定: `gem "upcastable", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
