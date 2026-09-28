# sixword

**Tag**: security, data

## 简介

Sixword encodes binary data in a human-friendly format using English words.
    It uses the 6-word binary encoding created for S/Key (tm) and standardized
    by RFC 2289, RFC 1760, and RFC 1751. Binary data is encoded using a
    dictionary of 2048 short English words (1-4 letters in length). Each block
    of 64 bits is encoded using 6 words, which includes 2 parity bits for error
    checking. This is ideal for transmitting binary data such as cryptographic
    keys where humans must communicate or enter the values.

    See also: Bubble Babble, PGP Word List, Diceware, Base64, Base32

## 官网

- 主页: https://github.com/ab/sixword
- 文档: https://www.rubydoc.info/gems/sixword/0.5.0
- RubyGems: https://rubygems.org/gems/sixword

## 历史版本号

- 0.5.0 (2025-09-18)
- 0.4.0 (2021-10-05)
- 0.3.5 (2018-03-28)
- 0.3.4 (2015-12-06)
- 0.3.3 (2015-12-01)
- 0.3.2 (2015-11-25)
- 0.3.1 (2015-03-21)
- 0.3.0 (2014-07-10)
- 0.2.0 (2013-09-27)
- 0.1.0 (2013-09-26)
- 0.0.1 (2013-09-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/sixword
- gem 安装: `gem install sixword`
- Bundler: `gem "sixword"`
- 最新版本: 0.5.0
- 最新版归档: https://rubygems.org/downloads/sixword-0.5.0.gem
- 版本锁定: `gem "sixword", "~> 0.5.0"`
- 中央仓库: https://rubygems.org/
