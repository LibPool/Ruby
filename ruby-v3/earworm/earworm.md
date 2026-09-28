# earworm

**Tag**: cli, filesystem

## 简介

Earworm can identify unknown music using MusicDNS and libofa.  == FEATURES/PROBLEMS:  * Identifies mp3, ogg, and wav files.  == SYNOPSIS:  Identify an unknown audio file:  ew = Earworm::Client.new('MY Music DNS Key') info = ew.identify(:file =&gt; '/home/aaron/unknown.wav') puts &quot;#{info.artist_name} - #{info.title}&quot;

## 官网

- 主页: http://earworm.rubyforge.org
- RubyGems: https://rubygems.org/gems/earworm

## 历史版本号

- 0.0.2 (2009-07-25)
- 0.0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/earworm
- gem 安装: `gem install earworm`
- Bundler: `gem "earworm"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/earworm-0.0.2.gem
- 版本锁定: `gem "earworm", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
