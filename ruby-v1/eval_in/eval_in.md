# eval_in

**Tag**: web, networking

## 简介

Safely evaluates code (Ruby and others) by sending it through https://eval.in

== Languages and Versions

  Ruby          | MRI 1.0, MRI 1.8.7, MRI 1.9.3, MRI 2.0.0, MRI 2.1
  C             | GCC 4.4.3, GCC 4.9.1
  C++           | C++11 (GCC 4.9.1), GCC 4.4.3, GCC 4.9.1
  CoffeeScript  | CoffeeScript 1.7.1 (Node 0.10.29)
  Fortran       | F95 (GCC 4.4.3)
  Haskell       | Hugs98 September 2006
  Io            | Io 20131204
  JavaScript    | Node 0.10.29
  Lua           | Lua 5.1.5, Lua 5.2.3
  OCaml         | OCaml 4.01.0
  PHP           | PHP 5.5.14
  Pascal        | Free Pascal 2.6.4
  Perl          | Perl 5.20.0
  Python        | CPython 2.7.8, CPython 3.4.1
  Slash         | Slash HEAD
  x86 Assembly  | NASM 2.07

== Example:

It's this simple:

  result = EvalIn.call 'puts "example"', language: "ruby/mri-2.1"
  result.output # returns "example\n"

## 官网

- 主页: https://github.com/JoshCheek/eval_in
- 文档: http://rdoc.info/gems/eval_in/frames/EvalIn
- 问题追踪: https://github.com/JoshCheek/eval_in/issues
- RubyGems: https://rubygems.org/gems/eval_in

## 历史版本号

- 0.2.0 (2014-10-21)
- 0.1.6 (2014-09-06)
- 0.1.5 (2014-09-01)
- 0.1.4 (2014-08-31)
- 0.1.3 (2014-08-27)
- 0.1.2 (2014-08-24)
- 0.1.1 (2014-08-24)
- 0.1.0 (2014-08-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/eval_in
- gem 安装: `gem install eval_in`
- Bundler: `gem "eval_in"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/eval_in-0.2.0.gem
- 版本锁定: `gem "eval_in", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
