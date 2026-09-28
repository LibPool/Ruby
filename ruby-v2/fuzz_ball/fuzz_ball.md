# fuzz_ball

**Tag**: library

## 简介

FuzzBall is a gem that finds fuzzy matches of a string (the 'needle') within an array of strings (the 'haystack'). It does so via a two-step process: first, it finds candidate strings from the haystack that have high similarity to the needle, then uses a Smith-Waterman algorithm to fuzzily match from these candidates. Strings are returned along with a matching score. Both steps of the search are written in C for greater performance.

## 官网

- 主页: http://github.com/vincentchu/fuzz_ball
- RubyGems: https://rubygems.org/gems/fuzz_ball

## 历史版本号

- 0.9.1 (2011-10-20)
- 0.9.0 (2011-10-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/fuzz_ball
- gem 安装: `gem install fuzz_ball`
- Bundler: `gem "fuzz_ball"`
- 最新版本: 0.9.1
- 最新版归档: https://rubygems.org/downloads/fuzz_ball-0.9.1.gem
- 版本锁定: `gem "fuzz_ball", "~> 0.9.1"`
- 中央仓库: https://rubygems.org/
