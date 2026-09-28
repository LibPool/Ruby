# cook

**Tag**: security, serialization, template, filesystem

## 简介

cook is a rake extension with:

1. configuration file,
1. the ability to retrieve passwords from encrypted configuration files,
1. the ability to create files using Erubis templates,
1. the ablity to interact with both local and remote shells.

Its main file is a traditional rake Rakefile, which has recipe 
commands.  Each recipe is a collection of rake task files and 
associated YAML configuration files, allowing tasks to make use of 
extensive configuration information.  The configuration is built up 
from the various fragments in the conf files assocaited with each set 
of rake tasks.

## 官网

- 主页: https://github.com/stephengaito/rGems-cook
- 文档: https://www.rubydoc.info/gems/cook/2.0.10
- RubyGems: https://rubygems.org/gems/cook

## 历史版本号

- 2.0.10 (2015-10-21)
- 2.0.9 (2014-09-16)
- 2.0.8 (2014-07-22)
- 2.0.7 (2014-04-23)
- 2.0.6 (2014-02-28)
- 2.0.5 (2014-02-26)
- 2.0.4 (2014-02-17)
- 2.0.3 (2014-02-15)
- 2.0.2 (2014-02-15)
- 2.0.1 (2014-01-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/cook
- gem 安装: `gem install cook`
- Bundler: `gem "cook"`
- 最新版本: 2.0.10
- 最新版归档: https://rubygems.org/downloads/cook-2.0.10.gem
- 版本锁定: `gem "cook", "~> 2.0.10"`
- 中央仓库: https://rubygems.org/
