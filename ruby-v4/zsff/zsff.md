# zsff

**Tag**: security

## 简介

== FEATURES/PROBLEMS:  Right now, only one function: parse.  This does the validation and parsing all in one step.  This is intended to be used by any reader (who would take care of what links have been read, etc).  == SYNOPSIS:  results = Zsff.parse(url) results[:errors] #Any errors encountered while parsing results[:warnings] #Any warnings encountered while parsing results[:attrs] #A hash for the author, title, etc information from the feed results[:links] #List of links in the feed  == REQUIREMENTS:

## 官网

- 文档: https://www.rubydoc.info/gems/zsff/1.0.0
- RubyGems: https://rubygems.org/gems/zsff

## 历史版本号

- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/zsff
- gem 安装: `gem install zsff`
- Bundler: `gem "zsff"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/zsff-1.0.0.gem
- 版本锁定: `gem "zsff", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
