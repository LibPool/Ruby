# jeckyl

**Tag**: template, filesystem

## 简介

Create and manage configuration files in Ruby for Ruby. Jeckyl can be used to create a parameters hash 
from a simple config file written in Ruby, having run whatever checks you want on the file to ensure 
the values passed in are valid. All you need to do is define a class inheriting from Jeckyl, methods for
each parameter, its default, whatever checking rules are appropriate and even a comment for generating templates etc.
This is then used to parse a Ruby config file and create the parameters hash. Jeckyl 
comes complete with a utility to check a config file against a given class and to generate a default file for you to tailor.
Type 'jeckyl readme' for more information.

## 官网

- 源码仓库: https://github.com/osburn-sharp/jeckyl
- 文档: http://rubydoc.info/github/osburn-sharp/jeckyl/frames
- 问题追踪: https://github.com/osburn-sharp/jeckyl/issues
- RubyGems: https://rubygems.org/gems/jeckyl

## 历史版本号

- 0.4.0 (2014-10-01)
- 0.3.7 (2013-09-19)
- 0.2.7 (2012-11-21)
- 0.2.5 (2012-10-25)
- 0.2.4 (2012-10-25)
- 0.2.3 (2012-09-21)
- 0.2.1 (2012-09-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/jeckyl
- gem 安装: `gem install jeckyl`
- Bundler: `gem "jeckyl"`
- 最新版本: 0.4.0
- 最新版归档: https://rubygems.org/downloads/jeckyl-0.4.0.gem
- 版本锁定: `gem "jeckyl", "~> 0.4.0"`
- 中央仓库: https://rubygems.org/
