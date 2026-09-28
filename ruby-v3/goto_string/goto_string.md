# goto_string

**Tag**: library

## 简介

== FEATURES/PROBLEMS:  * Partial string matching * The algorithm is not particularly performant  == SYNOPSIS:  require 'goto_string'  s = %w(goto_string is a small library that implements a substring matching and ranking algorithm. The matching and ranking is similar to that found in Quicksilver or TextMate) GotoString::Matcher.match('string', s) #=&gt; [[&quot;goto_string&quot;, &quot;goto_string&quot;, 0.679259259259259, [[&quot;string&quot;, 5]]], [&quot;substring&quot;, &quot;substring&quot;, 0.461481481481481, [[&quot;s&quot;, 0], [&quot;tring&quot;, 4]]]]  An array is returned which contains one entry for each match. Matches are ordered by rank.  Each match is itself an array, containing the following elements:  [ &quot;original candidate&quot;, &quot;matched string&quot;, rank, [[&quot;substring_1&quot;, offset], [&quot;substring_2&quot;, offset], ... ] ]  You can optionally pass a block to the match method which will get each candidate passed to it. The return value of the block is what will be used for matching. This is so you can pass in arrays of complex objects as candidates:  GotoString::Matcher.match( &quot;goto&quot;, Project.find(:all) ) do |p| p.name end  The resulting matches will contain a reference to the matched string (the project name) as well as the project (the original candidate)  == REQUIREMENTS:  * None

## 官网

- 文档: https://www.rubydoc.info/gems/goto_string/0.1.4
- RubyGems: https://rubygems.org/gems/goto_string

## 历史版本号

- 0.1.4 (2009-07-25)
- 0.1.3 (2009-07-25)
- 0.1.2 (2009-07-25)
- 0.1.1 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/goto_string
- gem 安装: `gem install goto_string`
- Bundler: `gem "goto_string"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/goto_string-0.1.4.gem
- 版本锁定: `gem "goto_string", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
