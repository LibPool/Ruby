# ruen_speller

**Tag**: library

## 简介

This simple gem I've done in training.
It checking the spelling English or Russian text wiht tech.yandex.ru/speller site.
examples:
puts RuenSpeller.correct?("love")#=&gt; true
puts RuenSpeller.correct?("leve")#=&gt; ["lee", "live", "love", "lave", "level"]
RuenSpeller.correct?("leve").request_value #=&gt; 'leve'
RuenSpeller.correct?("leve").checked_values #=&gt; ["lee", "live", "love", "lave", "level"]
The default method sends GET-request. If you need a POST-request, just drop the last argument - true.
Example: RuenSpeller.correct?("Love", true)

## 官网

- 主页: http://rubygems.org/gem/speller
- 源码仓库: https://github.com/Rim-777/ruen_speller_gem
- RubyGems: https://rubygems.org/gems/ruen_speller

## 历史版本号

- 1.0.1 (2015-07-12)
- 1.0.0 (2015-07-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruen_speller
- gem 安装: `gem install ruen_speller`
- Bundler: `gem "ruen_speller"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/ruen_speller-1.0.1.gem
- 版本锁定: `gem "ruen_speller", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
