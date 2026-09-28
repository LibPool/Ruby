# bad_word_detector

**Tag**: serialization, filesystem

## 简介

Detects #uck F|_|__C_K and other variations of hidden swear words in text.
    Usage:
    ```
        finder = BadWordDetector.new
        finder.find("What the #uck")
        it will return BadWord object
    ```
    Transformation rules is defined in form: {"#" => {"symbol"=>"f", "weight" => 2}} (where weight is optional)
    in file conf/rules.yaml 
    List of swear words is located in conf/library.yaml
    Whitelist of english words in conf/whitelist.yaml
    You can also set own rules:
        finder = BadWordDetector.new rules, library, whitelist

## 官网

- 主页: https://github.com/hairyhum/bad-words.ruby
- RubyGems: https://rubygems.org/gems/bad_word_detector

## 历史版本号

- 0.0.5 (2013-03-16)
- 0.0.4 (2013-03-15)
- 0.0.3 (2013-03-15)
- 0.0.2 (2013-03-15)
- 0.0.1 (2013-02-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/bad_word_detector
- gem 安装: `gem install bad_word_detector`
- Bundler: `gem "bad_word_detector"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/bad_word_detector-0.0.5.gem
- 版本锁定: `gem "bad_word_detector", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
