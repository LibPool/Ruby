# colored2

**Tag**: web, security, networking

## 简介

This is a heavily modified fork of http://github.com/defunkt/colored gem, with many
sensible pull requests combined. Since the authors of the original gem no longer support it,
this might, perhaps, be considered a good alternative.

Simple gem that adds various color methods to String class, and can be used as follows:

  require 'colored2'

  puts 'this is red'.red
  puts 'this is red with a yellow background'.red.on.yellow
  puts 'this is red with and italic'.red.italic
  puts 'this is green bold'.green.bold << ' and regular'.green
  puts 'this is really bold blue on white but reversed'.bold.blue.on.white.reversed
  puts 'this is regular, but '.red! << 'this is red '.yellow! << ' and yellow.'.no_color!
  puts ('this is regular, but '.red! do
    'this is red '.yellow! do
      ' and yellow.'.no_color!
    end
  end)

## 官网

- 主页: http://github.com/kigster/colored2
- 文档: https://www.rubydoc.info/gems/colored2/4.0.3
- RubyGems: https://rubygems.org/gems/colored2

## 历史版本号

- 4.0.3 (2025-01-18)
- 4.0.0 (2023-08-24)
- 3.1.2 (2017-02-14)
- 2.0.2 (2016-03-10)
- 2.0.0 (2016-03-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/colored2
- gem 安装: `gem install colored2`
- Bundler: `gem "colored2"`
- 最新版本: 4.0.3
- 最新版归档: https://rubygems.org/downloads/colored2-4.0.3.gem
- 版本锁定: `gem "colored2", "~> 4.0.3"`
- 中央仓库: https://rubygems.org/
