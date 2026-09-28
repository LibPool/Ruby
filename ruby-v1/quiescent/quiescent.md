# quiescent

**Tag**: testing

## 简介

This is a very simple mixin to support quiescing constants (which we call "quiescents") in Ruby.  You may assign a value to a quiescing constant once during the execution of the program; however, a quiescing constant's value is fixed after the first time it is read.  Quiescing constants may have default values (specified either as explicit values or argumentless blocks to compute that value) that take effect if they are not explicitly assigned to before their first use.

## 官网

- 主页: http://github.com/willb/quiescent
- RubyGems: https://rubygems.org/gems/quiescent

## 历史版本号

- 0.1.1 (2011-09-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/quiescent
- gem 安装: `gem install quiescent`
- Bundler: `gem "quiescent"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/quiescent-0.1.1.gem
- 版本锁定: `gem "quiescent", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
