# websitary

**Tag**: web, networking, template

## 简介

== DESCRIPTION: websitary (formerly known as websitiary with an extra &quot;i&quot;) monitors  webpages, rss feeds, podcasts etc. It reuses other programs (w3m, diff  etc.) to do most of the actual work. By default, it works on an ASCII  basis, i.e. with the output of text-based webbrowsers like w3m (or lynx,  links etc.) as the output can easily be post-processed. It can also work  with HTML and highlight new items. This script was originally planned as  a ruby-based websec replacement.  By default, this script will use w3m to dump HTML pages and then run  diff over the current page and the previous backup. Some pages are  better viewed with lynx or links. Downloaded documents (HTML or ASCII)  can be post-processed (e.g., filtered through some ruby block that  extracts elements via hpricot and the like). Please see the  configuration options below to find out how to change this globally or  for a single source.  This user manual is also available as PDF[http://websitiary.rubyforge.org/websitary.pdf].  == FEATURES/PROBLEMS: * Handle webpages, rss feeds (optionally save attachments in podcasts  etc.) * Compare webpages with previous backups * Display differences between the current version and the backup * Provide hooks to post-process the downloaded documents and the diff * Display a one-page report summarizing all news * Automatically open the report in your favourite web-browser * Experimental: Download webpages on defined intervalls and generate  incremental diffs.

## 官网

- 主页: http://rubyforge.org/projects/websitiary/
- RubyGems: https://rubygems.org/gems/websitary

## 历史版本号

- 0.5 (2009-07-25)
- 0.4 (2009-07-25)
- 0.3 (2009-07-25)
- 0.2.1 (2009-07-25)
- 0.2.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/websitary
- gem 安装: `gem install websitary`
- Bundler: `gem "websitary"`
- 最新版本: 0.5
- 最新版归档: https://rubygems.org/downloads/websitary-0.5.gem
- 版本锁定: `gem "websitary", "~> 0.5"`
- 中央仓库: https://rubygems.org/
