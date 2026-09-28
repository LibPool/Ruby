# websitiary

**Tag**: web, testing, template

## 简介

== DESCRIPTION: This is a script for monitoring webpages that reuses other programs  (w3m, diff, webdiff etc.) to do most of the actual work. By default, it  works on an ASCII basis, i.e. with the output of text-based webbrowsers  like w3m (or lynx, links etc.) as the output can easily be  post-processed. With the help of some friends (see the section below on  requirements), it can also work with HTML. E.g., if you have websec  installed, you can also use its webdiff program to show colored diffs.  By default, this script will use w3m to dump HTML pages and then run  diff over the current page and the previous backup. Some pages are  better viewed with lynx or links. Downloaded documents (HTML or ASCII)  can be post-processed (e.g., filtered through some ruby block that  extracts elements via hpricot and the like). Please see the  configuration options below to find out how to change this globally or  for a single source.  === CAVEAT: The script also includes experimental support for monitoring whole  websites. Basically, this script supports robots.txt directives (see  requirements) but this is hardly tested and may not work in some cases.  While it is okay for your own websites to ignore robots.txt, it is not  for others. Please make sure that the webpages you run this program on  allow such a use.  Some webpages disallow the use of any automatic  downloader or offline reader in their user agreements.

## 官网

- 主页: http://rubyforge.org/projects/websitiary/
- RubyGems: https://rubygems.org/gems/websitiary

## 历史版本号

- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/websitiary
- gem 安装: `gem install websitiary`
- Bundler: `gem "websitiary"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/websitiary-0.1.0.gem
- 版本锁定: `gem "websitiary", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
