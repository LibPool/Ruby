# ruck

**Tag**: web, tooling, filesystem

## 简介

Ruck uses continuations and a simple scheduler to ensure "shreds"
      (Ruck threads) are woken at precisely the right time according
      to its virtual clock. Schedulers can map virtual time to samples
      in a WAV file, real time, time in a MIDI file, or anything else
      by overriding "sim_to" in the Shreduler class.
      
      A small library of useful unit generators and plenty of examples
      are provided. See the README or the web page for details.

## 官网

- 主页: http://github.com/alltom/ruck
- RubyGems: https://rubygems.org/gems/ruck

## 历史版本号

- 0.3.0 (2010-08-15)
- 0.2.0 (2010-07-10)
- 0.1.2 (2009-11-20)
- 0.1.0 (2009-11-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruck
- gem 安装: `gem install ruck`
- Bundler: `gem "ruck"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/ruck-0.3.0.gem
- 版本锁定: `gem "ruck", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
