# daedalus-core

**Tag**: tooling

## 简介

Daedalus is a build system based on years of attempting to build Rubinus with a collection of Rake tasks. Rubinius is a complex system. It has dependencies on external C libraries (some of which are vendored), internal C/C++ libraries, Ruby C-extensions, and compiled Ruby code. The Rubinius bytecode compiler is written in Ruby, so we have to bootstrap compiling it.

Rake fails at this task because there is no way to manage multiple, independent dependency trees without subprocessing another Rake process. This results in unreasonable and unmanagable complexity.

## 官网

- 主页: https://github.com/rubinius/daedalus-core
- 文档: https://www.rubydoc.info/gems/daedalus-core/1.6
- RubyGems: https://rubygems.org/gems/daedalus-core

## 历史版本号

- 1.6 (2017-09-30)
- 1.5 (2017-09-18)
- 1.4 (2017-08-20)
- 1.3 (2016-10-17)
- 1.2 (2016-08-04)
- 1.1 (2016-08-04)
- 1.0 (2016-08-03)
- 0.5.0 (2015-05-17)
- 0.4.0 (2015-05-17)
- 0.3.0 (2015-05-03)
- 0.2.0 (2014-12-15)
- 0.1.0 (2014-07-15)
- 0.0.3 (2013-12-27)
- 0.0.1 (2013-07-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/daedalus-core
- gem 安装: `gem install daedalus-core`
- Bundler: `gem "daedalus-core"`
- 最新版本: 1.6
- 最新版归档: https://rubygems.org/downloads/daedalus-core-1.6.gem
- 版本锁定: `gem "daedalus-core", "~> 1.6"`
- 中央仓库: https://rubygems.org/
