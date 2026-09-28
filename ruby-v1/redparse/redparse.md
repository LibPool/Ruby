# redparse

**Tag**: tooling

## 简介

RedParse is a ruby parser (and parser-compiler) written in pure ruby. 
Instead of YACC or ANTLR, it's parse tool is a home-brewed language. (The
tool is (at least) LALR(1)-equivalent and the 'parse language' is 
pretty nice, even in it's current form.)

My intent is to have a completely correct parser for ruby, in 100% 
ruby. And I think I've more or less succeeded. Aside from some fairly
minor quibbles (see below), RedParse can parse all known ruby 1.8 and 1.9 
constructions correctly. Input text may be encoded in ascii, binary, 
utf-8, iso-8859-1, and the euc-* family of encodings. Sjis is not yet 
supported.

## 官网

- 主页: http://github.com/coatl/redparse
- 文档: https://www.rubydoc.info/gems/redparse/1.0.0
- RubyGems: https://rubygems.org/gems/redparse

## 历史版本号

- 1.0.0 (2016-08-11)
- 0.8.4 (2010-01-03)
- 0.8.3 (2009-08-05)
- 0.8.0 (2009-07-25)
- 0.8.2 (2009-07-25)
- 0.8.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/redparse
- gem 安装: `gem install redparse`
- Bundler: `gem "redparse"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/redparse-1.0.0.gem
- 版本锁定: `gem "redparse", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
