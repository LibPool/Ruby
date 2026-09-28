# primitive_wrapper

**Tag**: library

## 简介

This gem creates a thin shell to encapsulate primitive literal types such as integers, floats and symbols.
There are a family of wrappers which mimic the behavior of what they contain.
Primitive types have several drawbacks: no constructor to call, can't create instance variables, and can't create singleton methods.
There is some utility in wrapping a primitive type. You can simulate a call by reference for example.
You can also simulate mutability, and pointers.
Some wrappers are dedicated to holding a single type while others may hold a family of types such as the `Number` wrapper.
What is interesting to note is Number objects do not derive from `Numeric`, but instead derive from `Value` (the wrapper base class);
but at the same time, `Number` objects mimic the methods of `Fixnum`, `Complex`, `Float`, etc.
Many of the wrappers can be used in an expression without having to call an access method.
There are also new types: `Bool` which wraps `true,false` and `Property` which wraps `Hash` types.
The `Property` object auto-methodizes the key names of the Hash.
Also `Fraction` supports mixed fractions.

## 官网

- 文档: https://www.rubydoc.info/gems/primitive_wrapper/2.3.0
- RubyGems: https://rubygems.org/gems/primitive_wrapper

## 历史版本号

- 2.3.0 (2018-03-26)
- 2.2.0 (2018-02-12)
- 2.1.0 (2018-02-03)
- 2.0.0 (2018-01-22)
- 1.0.1 (2018-01-12)
- 1.0.0 (2018-01-12)
- 0.1.0 (2017-12-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/primitive_wrapper
- gem 安装: `gem install primitive_wrapper`
- Bundler: `gem "primitive_wrapper"`
- 最新版本: 2.3.0
- 最新版归档: https://rubygems.org/downloads/primitive_wrapper-2.3.0.gem
- 版本锁定: `gem "primitive_wrapper", "~> 2.3.0"`
- 中央仓库: https://rubygems.org/
