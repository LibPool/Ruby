# nele

**Tag**: library

## 简介

Nele translates ruby string to the other language.

It uses external public translators like Microsoft Translator or Yahoo's Babelfish.

### Installation:

    git install nele

### Usage:

    require 'nele'

    String.translators
    => [:babelfish, :ms]

### Microsoft Translator:

    String.translator = :ms
    String.translator.config[:from] = "en"
    String.translator.config[:to] = "pl"
    String.translator.config[:appId] = YOUR_APP_ID

    "nice girl".translate
    => "mila dziewczyna"

### Yahoo's Babelfish:

    String.translator = :babelfish
    String.translator.config[:lp] = "en_es"

    "hello".translate
    => "hola"

If you know any other (free) public translators just let me know, or write your own adapter for nele.

## 官网

- 主页: http://github.com/cfx/nele
- RubyGems: https://rubygems.org/gems/nele

## 历史版本号

- 0.2.2 (2011-12-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/nele
- gem 安装: `gem install nele`
- Bundler: `gem "nele"`
- 最新版本: 0.2.2
- 最新版归档: https://rubygems.org/downloads/nele-0.2.2.gem
- 版本锁定: `gem "nele", "~> 0.2.2"`
- 中央仓库: https://rubygems.org/
