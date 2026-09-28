# oedipus_lex

**Tag**: security, tooling

## 简介

Oedipus Lex is a lexer generator in the same family as Rexical and
Rex. Oedipus Lex is my independent lexer fork of Rexical. Rexical was
in turn a fork of Rex. We've been unable to contact the author of rex
in order to take it over, fix it up, extend it, and relicense it to
MIT. So, Oedipus was written clean-room in order to bypass licensing
constraints (and because bootstrapping is fun).

Oedipus brings a lot of extras to the table and at this point is only
historically related to rexical. The syntax has changed enough that
any rexical lexer will have to be tweaked to work inside of oedipus.
At the very least, you need to add slashes to all your regexps.

Oedipus, like rexical, is based primarily on generating code much like
you would a hand-written lexer. It is _not_ a table or hash driven
lexer. It uses StrScanner within a multi-level case statement. As such,
Oedipus matches on the _first_ match, not the longest (like lex and
its ilk).

This documentation is not meant to bypass any prerequisite knowledge
on lexing or parsing. If you'd like to study the subject in further
detail, please try [TIN321] or the [LLVM Tutorial] or some other good
resource for CS learning. Books... books are good. I like books.

## 官网

- 主页: http://github.com/seattlerb/oedipus_lex
- RubyGems: https://rubygems.org/gems/oedipus_lex

## 历史版本号

- 2.6.3 (2025-12-24)
- 2.6.2 (2023-08-03)
- 2.6.1 (2023-05-31)
- 2.6.0 (2021-10-27)
- 2.5.3 (2021-05-30)
- 2.5.2 (2020-06-14)
- 2.5.1 (2019-06-04)
- 2.5.0 (2016-11-30)
- 2.4.1 (2016-01-21)
- 2.4.0 (2014-08-30)
- 2.3.2 (2014-08-07)
- 2.3.1 (2014-06-10)
- 2.3.0 (2014-05-16)
- 2.2.1 (2014-04-02)
- 2.2.0 (2014-03-14)
- 2.1.0 (2014-01-22)
- 2.0.0 (2013-12-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/oedipus_lex
- gem 安装: `gem install oedipus_lex`
- Bundler: `gem "oedipus_lex"`
- 最新版本: 2.6.3
- 最新版归档: https://rubygems.org/downloads/oedipus_lex-2.6.3.gem
- 版本锁定: `gem "oedipus_lex", "~> 2.6.3"`
- 中央仓库: https://rubygems.org/
