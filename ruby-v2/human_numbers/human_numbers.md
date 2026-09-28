# human_numbers

**Tag**: testing

## 简介

human_numbers defines the method #to_english on the classes Float and
Integer, as well as the method #to_french on the Integer class, for
converting numbers to natural language strings. By default, a cardinal
number will be returned (one, two, three), but supplying an :ordinal
argument will cause it to return an ordinal (first, second, third). It
works with numbers whose absolute value is less than 10^33. #to_french
supports a second argument for specifying the gender of the word,
which can be either :masculine or :feminine.

## 官网

- 主页: https://github.com/kybp/human_numbers
- 文档: https://www.rubydoc.info/gems/human_numbers/0.1.0
- RubyGems: https://rubygems.org/gems/human_numbers

## 历史版本号

- 0.1.0 (2016-09-02)
- 0.0.4 (2016-09-01)
- 0.0.3 (2016-09-01)
- 0.0.2 (2016-09-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/human_numbers
- gem 安装: `gem install human_numbers`
- Bundler: `gem "human_numbers"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/human_numbers-0.1.0.gem
- 版本锁定: `gem "human_numbers", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
