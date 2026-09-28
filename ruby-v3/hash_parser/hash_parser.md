# hash_parser

**Tag**: database, security, serialization, tooling, filesystem, data

## 简介

Parses a hash string of the format `'{ :a =&gt; "something" }'` into an actual ruby hash object `{ a: "something" }`.
This is useful when you by mistake serialize hashes and save it in database column or a text file and you want to
convert them back to hashes without the security issues of executing `eval(hash_string)`.

By default only following classes are allowed to be deserialized:

* TrueClass
* FalseClass
* NilClass
* Numeric
* String
* Array
* Hash

A HashParser::BadHash exception is thrown if unserializable values are present.

## 官网

- 主页: https://github.com/bibstha/ruby_hash_parser
- 文档: https://www.rubydoc.info/gems/hash_parser/0.0.2
- RubyGems: https://rubygems.org/gems/hash_parser

## 历史版本号

- 0.0.2 (2017-03-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/hash_parser
- gem 安装: `gem install hash_parser`
- Bundler: `gem "hash_parser"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/hash_parser-0.0.2.gem
- 版本锁定: `gem "hash_parser", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
