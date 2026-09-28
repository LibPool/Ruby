# fast_xs

**Tag**: web, testing, serialization, networking, tooling

## 简介

fast_xs provides C extensions for escaping text.

The original String#fast_xs method is based on the xchar code by Sam Ruby:

* http://intertwingly.net/stories/2005/09/28/xchar.rb
* http://intertwingly.net/blog/2005/09/28/XML-Cleansing

_why also packages an older version with Hpricot (patches submitted).
The version here should be compatible with the latest version of Hpricot
code.

Ruby on Rails will automatically use String#fast_xs from either Hpricot
or this gem version with the bundled Builder package.

String#fast_xs is an almost exact translation of Sam Ruby's original
implementation (String#to_xs), but it does escape "&quot;" (which is an
optional, but all parsers are able ot handle it.  XML::Builder as
packaged in Rails 2.0 will be automatically use String#fast_xs instead
of String#to_xs available.

## 官网

- 主页: http://fast-xs.rubyforge.org/
- RubyGems: https://rubygems.org/gems/fast_xs

## 历史版本号

- 0.8.0 (2011-01-26)
- 0.7.1 (2009-08-05)
- 0.7.2 (2009-08-05)
- 0.7.3 (2009-08-05)
- 0.7 (2009-07-25)
- 0.6 (2009-07-25)
- 0.5 (2009-07-25)
- 0.4 (2009-07-25)
- 0.3 (2009-07-25)
- 0.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/fast_xs
- gem 安装: `gem install fast_xs`
- Bundler: `gem "fast_xs"`
- 最新版本: 0.8.0
- 最新版归档: https://rubygems.org/downloads/fast_xs-0.8.0.gem
- 版本锁定: `gem "fast_xs", "~> 0.8.0"`
- 中央仓库: https://rubygems.org/
