# called_from

**Tag**: filesystem

## 简介

Extention Module 'called_from' provides called_from() global function
which gets filename and line number of caller.

In short:

    require 'called_from'
    filename, linenum, function = called_from(1)

is equivarent to:

    caller(1)[0] =~ /:(d+)( in `(.*)')?/
    filename, linenum, function = $`, $1, $2

But called_from() is much faster than caller()[0].

## 官网

- 主页: http://github.com/kwatch/called_from/
- RubyGems: https://rubygems.org/gems/called_from

## 历史版本号

- 0.1.0 (2009-11-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/called_from
- gem 安装: `gem install called_from`
- Bundler: `gem "called_from"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/called_from-0.1.0.gem
- 版本锁定: `gem "called_from", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
