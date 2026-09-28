# apoptosis

**Tag**: web, networking, filesystem

## 简介

https://rubygems.org/gems/apoptosis

I got the idea for this gem during JRubyConf during Michael Feathers' talk. He made a point that software is alive and unlike biological systems, doesn't have an automatic way to kill off old 'cells'. This gem is to aid in finding old, potentially crufty areas of your project that may need to be killed off and remade, or at least looked at.

Currently the gem alerts you to any lines that haven't been touched in at least a year. 
  
 \ gem install apoptosis

Navigate to a project directory which is also a git repository and run
the command:

  apoptosis

This command will create a DeathRow.md file in the directory with a list
of files and lines in your project which have not been touched in a
year.  The idea is that you should re-evaluate and/or refactor them.

## 官网

- 主页: https://rubygems.org/gems/apoptosis
- 源码仓库: https://github.com/swerner/apoptosis

## 历史版本号

- 0.0.5 (2011-08-05)
- 0.0.4 (2011-08-04)
- 0.0.3 (2011-08-04)
- 0.0.2 (2011-08-04)
- 0.0.1 (2011-08-04)

## 获取地址

- RubyGems: https://rubygems.org/gems/apoptosis
- gem 安装: `gem install apoptosis`
- Bundler: `gem "apoptosis"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/apoptosis-0.0.5.gem
- 版本锁定: `gem "apoptosis", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
