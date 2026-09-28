# subload

**Tag**: web, networking, filesystem

## 简介

A handy dandy autoload / require / load helper for your rubies. Similar to
using[1], but with a few differences of opinion, and a bit shorter.

Basically, expand path is fine, up until a point. Sometimes there's no point
(i.e. when the load path already contains most of the path you're trying to
open). When you're writing libs that users might require sub parts with
'libname/sub_part', then expand_path combined with say, rubygems, can lead to
double requires. Lets not do that. :-)

[1] http://github.com/smtlaissezfaire/using/

## 官网

- 主页: http://rubygems.org/gems/subload
- 源码仓库: http://github.com/raggi/subload
- 文档: http://libraggi.rubyforge.org/subload/
- 问题追踪: http://github.com/raggi/subload/issues
- RubyGems: https://rubygems.org/gems/subload

## 历史版本号

- 1.1.0 (2010-03-17)
- 1.0.3 (2009-09-29)
- 1.0.0 (2009-09-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/subload
- gem 安装: `gem install subload`
- Bundler: `gem "subload"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/subload-1.1.0.gem
- 版本锁定: `gem "subload", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
