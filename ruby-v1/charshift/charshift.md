# charshift

**Tag**: library

## 简介

Charshift is a simple gem which adds functionality to the
                  String class.  It's primary function is to act on a given
                  string, taking a fixnum parameter, then shifting each 
                  character in that string to a higher or lower ordinal 
                  position in that strings encoding.

                  Charshift works with all of Ruby's included encodings and 
                  also works with devloper supplied 'custom encodings.'  
                  Simply provide an ordered set of characters as an optional
                  parameter and charshift will work on the string using that
                  set instead of the strings native encoding.

                  Charshift also includes a '.get_encoding_length' method which
                  returns the number of of characters which a given strings 
                  encoding contains.  Finally, strings can be shifted in place
                  using the '.charshift!' method.

## 官网

- 主页: https://github.com/cugamer/charshift
- 文档: https://www.rubydoc.info/gems/charshift/0.2.3
- RubyGems: https://rubygems.org/gems/charshift

## 历史版本号

- 0.2.3 (2016-06-23)
- 0.2.2 (2016-06-21)
- 0.2.1 (2016-06-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/charshift
- gem 安装: `gem install charshift`
- Bundler: `gem "charshift"`
- 最新版本: 0.2.3
- 最新版归档: https://rubygems.org/downloads/charshift-0.2.3.gem
- 版本锁定: `gem "charshift", "~> 0.2.3"`
- 中央仓库: https://rubygems.org/
