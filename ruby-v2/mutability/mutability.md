# mutability

**Tag**: library

## 简介

Mutability is a module that provides the very simple ability to designate an "original" version of an object that is frozen, and will not change even if the working copy of the object does. The best example is a Hash or Array -- collections like those exist partly so they can be mutated in some way, either by adding or removing elements or changing their order.  Now, rather than having to establish a separate "original" version of the object (not to mention dealing with the whole ivars-act-like-pointers-and-can-get-magically-changed-oops problem), you can use a MutableHash or MutableArray, and then change it to your heart's content.

The MutableHash/Array are built from the Mutability mix-in, so downloading this gem also provides a library for you to add the same capabilities to any other Class you might want.

Also included is the ability to revert to the original form with a single method call.

## 官网

- 主页: https://github.com/ksearfos/mutability
- 文档: https://www.rubydoc.info/gems/mutability/1.0.3
- RubyGems: https://rubygems.org/gems/mutability

## 历史版本号

- 1.0.3 (2014-12-24)
- 1.0.2 (2014-12-24)
- 1.0.1 (2014-12-24)
- 1.0.0 (2014-12-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/mutability
- gem 安装: `gem install mutability`
- Bundler: `gem "mutability"`
- 最新版本: 1.0.3
- 最新版归档: https://rubygems.org/downloads/mutability-1.0.3.gem
- 版本锁定: `gem "mutability", "~> 1.0.3"`
- 中央仓库: https://rubygems.org/
