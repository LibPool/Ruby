# decc_2050_model

**Tag**: web, cli, testing, networking, tooling, filesystem, data

## 简介

# DECC 2050 CALCULATOR TOOL

A C version and ruby wrapper for the www.decc.gov.uk 2050 energy and climate change excel calculator

Further detail on the project:
http://www.decc.gov.uk/2050

Canonical source:
http://github.com/decc/decc_2050_model

## DEPENDENCIES

1. ruby 1.9.2 (including development headers)
2. basic c development headers

This has ONLY been tested on OSX and on Ubuntu 64 bit EC2 ami.
Grateful for reports from other platforms. 

In the util folder there is an example script that creates a new EC2 EMI, installs all the dependencies and then compiles the gem. It may be useful if you are trying to figure out the complete set of dependencies.

## INSTALLATION

Note that this compiles the underlying c code, which might take 10-20 minutes or so

    gem install decc_2050_model
  
## UPDATING TO NEWER VERSIONS OF EXCEL MODEL

First of all, you need to be working on the github version of the code, not the rubygem:
    
    git clone http://github.com/decc/decc_2050_model

Then put the new spreadsheet in spreadsheet/model.xlsx

Then, from the top directory of the gem:
  
    bundle
    bundle exec rake
  
The next step is to check whether Rakefile, lib/model/_model_result.rb and lib/model/model_structure.rb need to be altered so that they
pick up the correct places in the underlying excel.
  
The final stage is to build and install the new gem:
    
    gem build model.gemspec
    gem install decc_2050_model-<version>.gem 

... where <version> is the version number of the gem file that was created in the folder.
  
Now follow the instructions in the twenty-fifty server directory in order to ensure that it is using this new version of the gem.

## 官网

- 主页: http://github.com/decc/decc_2050_model
- 文档: https://www.rubydoc.info/gems/decc_2050_model/3.5.1
- RubyGems: https://rubygems.org/gems/decc_2050_model

## 历史版本号

- 3.5.1-x86_64-linux (2013-12-04)
- 3.5.1 (2013-11-27)
- 3.5.0 (2013-11-19)
- 3.5.0-x86_64-linux (2013-11-19)
- 3.4.8-x86_64-linux (2013-11-12)
- 3.4.8 (2013-11-12)
- 3.4.7-x86_64-linux (2013-03-04)
- 3.4.7 (2013-03-04)
- 3.4.6-x86_64-linux (2013-01-11)
- 3.4.6 (2013-01-11)
- 3.4.5 (2013-01-08)
- 3.4.1olderlibc-x86_64-linux (2012-12-07)
- 3.4.1 (2012-12-06)
- 3.4.1-x86_64-linux (2012-12-06)
- 0.0.8-x86_64-linux (2012-06-12)
- 0.0.8 (2012-06-08)
- 0.0.7 (2012-06-04)
- 0.0.6-x86_64-linux (2012-05-01)
- 0.0.6 (2012-05-01)
- 0.0.5-x86_64-linux (2012-04-29)
- 0.0.5 (2012-04-29)
- 0.0.4 (2012-04-26)
- 0.0.3 (2012-04-24)
- 0.0.2 (2012-04-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/decc_2050_model
- gem 安装: `gem install decc_2050_model`
- Bundler: `gem "decc_2050_model"`
- 最新版本: 3.5.1
- 最新版归档: https://rubygems.org/downloads/decc_2050_model-3.5.1.gem
- 版本锁定: `gem "decc_2050_model", "~> 3.5.1"`
- 中央仓库: https://rubygems.org/
