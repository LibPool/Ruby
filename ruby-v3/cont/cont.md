# cont

**Tag**: web, networking, tooling

## 简介

The Cont module provides methods for working with continuations.
Continuations are a way to save the execution state of a program
so that it can be resumed later. They are used for advanced control
flow structures such as coroutines, generators, and so on.

Ruby have a built-in support for continuations, but it is deprecated
and should not be used. This implementation uses the 'fiber' library
based on https://github.com/minoki/delimited-continuations-in-lua .
That library is released under the MIT license.

Caution: The continuations of this implementation are 'one-shot',
So they can only be resumed once. If you try to resume a dead
continuation, an exception will be raised.

## 官网

- 文档: https://www.rubydoc.info/gems/cont/0.2.1
- RubyGems: https://rubygems.org/gems/cont

## 历史版本号

- 0.2.1 (2024-06-11)
- 0.2.0 (2024-06-11)
- 0.1.1 (2024-06-09)
- 0.1.0 (2024-06-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/cont
- gem 安装: `gem install cont`
- Bundler: `gem "cont"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/cont-0.2.1.gem
- 版本锁定: `gem "cont", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
