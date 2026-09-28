# deconstructable

**Tag**: library

## 简介

This gem provides Deconstructable, a mixin module that helps you to support
pattern-matching over your types.

Usage
--------

```
class Thing
  include Deconstructable

  ...

  deconstructable :x, :y

  deconstructable def foo
    do_the_foo
  end
end
```

This class provides a single DSL method `deconstructable` which helps you to mark
methods and attributes as deconstructable. Deconstructable attributes will be made
available in pattern matching, e.g.:

```
thing in Thing(foo:, x: 100, y:)
```

Classes that include `Deconstructable` gain an implementation of `deconstruct_keys` that permits
hash-style key based pattern matching. Positional array-style patterns are not supported.

## 官网

- 主页: https://rubygems.org/gems/deconstructable
- 源码仓库: https://gitlab.com/alexkalderimis/deconstructable
- 更新日志: https://gitlab.com/alexkalderimis/deconstructable/-/blob/master/CHANGELOG.md

## 历史版本号

- 0.1.0 (2020-05-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/deconstructable
- gem 安装: `gem install deconstructable`
- Bundler: `gem "deconstructable"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/deconstructable-0.1.0.gem
- 版本锁定: `gem "deconstructable", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
