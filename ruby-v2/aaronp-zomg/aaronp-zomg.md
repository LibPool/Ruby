# aaronp-zomg

**Tag**: cli, tooling, filesystem

## 简介

ZOMG is an OMG IDL parser.  ZOMG will generate a Ruby AST from an IDL AST, and will even generate ruby (by means of Ruby2Ruby).  == FEATURES/PROBLEMS:  * Parses IDL, generates Ruby * Ships with OMFG the Object Management File Generator * Ignores nested structs/unions * Treats out/inout parameters are DIY  == SYNOPSIS:  In code:  ZOMG::IDL.parse(File.read(ARGV[0])).to_ruby  Command line:  $ omfg lol.idl &gt; roflmao.rb

## 官网

- 主页: http://zomg.rubyforge.org/
- 文档: https://www.rubydoc.info/gems/aaronp-zomg/1.0.2.20080830162937
- RubyGems: https://rubygems.org/gems/aaronp-zomg

## 历史版本号

- 1.0.2.20080827232412 (2014-08-11)
- 1.0.2.20080828210656 (2014-08-11)
- 1.0.2.20080830162937 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/aaronp-zomg
- gem 安装: `gem install aaronp-zomg`
- Bundler: `gem "aaronp-zomg"`
- 最新版本: 1.0.2.20080830162937
- 最新版归档: https://rubygems.org/downloads/aaronp-zomg-1.0.2.20080830162937.gem
- 版本锁定: `gem "aaronp-zomg", "~> 1.0.2.20080830162937"`
- 中央仓库: https://rubygems.org/
