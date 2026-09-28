# zomg

**Tag**: cli, tooling, filesystem

## 简介

ZOMG is an OMG IDL parser.  ZOMG will generate a Ruby AST from an IDL AST, and will even generate ruby (by means of Ruby2Ruby).  == FEATURES/PROBLEMS:  * Parses IDL, generates Ruby * Ships with OMFG the Object Management File Generator * Ignores nested structs/unions * Treats out/inout parameters are DIY  == SYNOPSIS:  In code:  ZOMG::IDL.parse(File.read(ARGV[0])).to_ruby  Command line:  $ omfg lol.idl &gt; roflmao.rb

## 官网

- 主页: http://zomg.rubyforge.org/
- RubyGems: https://rubygems.org/gems/zomg

## 历史版本号

- 1.0.0 (2009-07-25)
- 1.0.2 (2009-07-25)
- 1.0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/zomg
- gem 安装: `gem install zomg`
- Bundler: `gem "zomg"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/zomg-1.0.2.gem
- 版本锁定: `gem "zomg", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
