# text-hyphen

**Tag**: testing, filesystem

## 简介

Text::Hyphen is a Ruby library to hyphenate words in various languages using
Ruby-fied versions of TeX hyphenation patterns. It will properly hyphenate
various words according to the rules of the language the word is written in. The
algorithm is based on that of the TeX typesetting system by Donald E. Knuth.

This is originally based on the Perl implementation of [TeX::Hyphen][] and the
[Ruby port][]. The language hyphenation pattern files are based on the sources
available from [CTAN][] as of 2004.12.19 and have been manually translated by
Austin Ziegler.

This is a small feature release adding Russian language support and fixing a bug
in the custom hyphen support introduced last version. This release provides both
Ruby 1.8.7 and Ruby 1.9.2 support (but please read below). In short, Ruby 1.8
support is deprecated and I will not be providing any bug fixes related to Ruby
1.8. New features will be developed and tested against Ruby 1.9 only.

## 官网

- 主页: https://rubygems.org/gems/text-hyphen
- 文档: https://www.rubydoc.info/gems/text-hyphen/1.5.0

## 历史版本号

- 1.5.0 (2023-03-18)
- 1.4.1 (2012-08-27)
- 1.4 (2012-08-26)
- 1.3 (2012-06-21)
- 1.2 (2011-07-17)
- 1.0.2 (2011-02-09)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/text-hyphen
- gem 安装: `gem install text-hyphen`
- Bundler: `gem "text-hyphen"`
- 最新版本: 1.5.0
- 最新版归档: https://rubygems.org/downloads/text-hyphen-1.5.0.gem
- 版本锁定: `gem "text-hyphen", "~> 1.5.0"`
- 中央仓库: https://rubygems.org/
