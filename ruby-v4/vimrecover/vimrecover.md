# vimrecover

**Tag**: testing, filesystem

## 简介

This package provides a handy command to help you recover from Vim recovery files.  Vim makes .swp files as you edit your files so that if an edit session crashes you can recover the latest changes you haven't saved. Unfortunately though, there's no easy way to compare a saved file with the recovery file, so if a session does crash you are often left with many .swp files that you have to save under new names one by one and compare to the original files.   vimrecover searches for swap files in the current directory, converts them to  files that can be compared to the original files, lets you compare them with meld, deletes them if they are the same as the original files and generally helps you clean up the mess.  vimrecover is an interactive command-line program.

## 官网

- 主页: http://www.lesismore.co.za
- RubyGems: https://rubygems.org/gems/vimrecover

## 历史版本号

- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/vimrecover
- gem 安装: `gem install vimrecover`
- Bundler: `gem "vimrecover"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/vimrecover-1.0.0.gem
- 版本锁定: `gem "vimrecover", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
