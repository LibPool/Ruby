# ohmygems

**Tag**: testing, filesystem

## 简介

I'm tired of the complications that tools like bundler and rvm inject
into my system and my workflow. I don't want 4 billion gems installed
globally. I don't want to have `rake` slow down for no good reason. I
don't want rvm to regress on undefined variables over and over and
over (and I don't want to report it anymore when it does). I want as
much simplicity as I can afford and still be able to get my job done.

I've found pretty good balance using rbenv (only when needed) and by
using this 45 line shell function `ohmygems` (aliased to `omg`, of
course).

I still have my system-level gems as my previous GEM_HOME gets moved
into GEM_PATH so things like minitest and autotest are always
available. But now I have private gems that are incredibly easy to
switch around and only rely on simple environment variables to manage.

To go back to normal, simply run `omg reset`.

## 官网

- 主页: https://github.com/seattlerb/ohmygems
- 文档: https://www.rubydoc.info/gems/ohmygems/1.2.0
- RubyGems: https://rubygems.org/gems/ohmygems

## 历史版本号

- 1.2.0 (2014-06-17)
- 1.1.0 (2013-02-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/ohmygems
- gem 安装: `gem install ohmygems`
- Bundler: `gem "ohmygems"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/ohmygems-1.2.0.gem
- 版本锁定: `gem "ohmygems", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
