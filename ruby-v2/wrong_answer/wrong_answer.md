# wrong_answer

**Tag**: web, networking

## 简介

* http://www.rubysideshow.com/ * http://rubysideshow.rubyforge.org/wrong_answer/  == DESCRIPTION:  30 seconds after requiring wrong_answer, 1% of your comparisons will return false when it should have been true, or true when it should have been false.  == FEATURES/PROBLEMS:  * Sleeps for 30 seconds, then wrecks havoc  == SYNOPSIS:  require 'rubygems' require 'wrong_answer'  sleep 30  (1..1000).each do puts &quot;Wrong answer!&quot; if true == false end  # Wrong answer! # Wrong answer! # Wrong answer! # Wrong answer! # Wrong answer! # Wrong answer! # Wrong answer! # Wrong answer! # Wrong answer!  == REQUIREMENTS:  * an immature sense of humor * a visit to rickroll.com * a fondness for french fries * wasabe * gas money  == INSTALL:  * sudo gem install wrong_answer

## 官网

- 文档: https://www.rubydoc.info/gems/wrong_answer/0.1.0
- RubyGems: https://rubygems.org/gems/wrong_answer

## 历史版本号

- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/wrong_answer
- gem 安装: `gem install wrong_answer`
- Bundler: `gem "wrong_answer"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/wrong_answer-0.1.0.gem
- 版本锁定: `gem "wrong_answer", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
