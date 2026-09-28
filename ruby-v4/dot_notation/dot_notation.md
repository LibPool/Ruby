# dot_notation

**Tag**: web

## 简介

Simple-ish enumberable-simplifier. Useful for APIs like Twitter, etc

If you have a hash or an array or something that quacks like one, you can do stuff

example:
    require 'dot_notation'
    h = {a: {b: {c: [{d: 'hi'}]}}}
    h.extend(DotNotation)
    h.dot('a.b.c.0.d')
    #=&gt; 'hi'
    h.dot('a.b.c.foo.bar.bz.whatever.124.whocares')
    #=&gt; nil

## 官网

- 主页: https://github.com/joshsz/dot_notation
- RubyGems: https://rubygems.org/gems/dot_notation

## 历史版本号

- 1.0.1 (2014-08-18)
- 1.0.0 (2014-08-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/dot_notation
- gem 安装: `gem install dot_notation`
- Bundler: `gem "dot_notation"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/dot_notation-1.0.1.gem
- 版本锁定: `gem "dot_notation", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
