# global_2050_model

**Tag**: web, cli, testing, networking, tooling, devops, filesystem, data

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

In the util folder are two example scripts than can be helpful:

1. start-high-memory-instance.sh - is the script we use to setup an aws server to compile the model. You can't use it directly, because you won't have the right keys and certificates, but it can give clues.
2. setup-2050-model-builder-script.sh - is the script we use to get all the dependencies on that aws server correct, download this code, and then compile the model. Again, it may not be quite right for you but can server as inspiration

## INSTALLATION

Note that this compiles the underlying c code, which might take 10-20 minutes or so

    gem install decc_2050_model
  
## UPDATING TO NEWER VERSIONS OF EXCEL MODEL

First of all, you need to be working on the github version of the code, not the rubygem:
    
    git clone http://github.com/decc/decc_2050_model

Then put the new spreadsheet in spreadsheet/2050Model.xlsx

Then, from the top directory of the gem:
  
    bundle
    bundle exec rake
  
The next step is to check whether lib/decc_2050_model/decc_2050_model_result.rb and lib/decc_2050_model/model_structure.rb need to be altered so that they
pick up the correct places in the underlying excel.
  
The final stage is to build and install the new gem:
    
    gem build decc_2050_model.gemspec
    gem install decc_2050_model-<version>.gem 

... where <version> is the version number of the gem file that was created in the folder.
  
Now follow the instructions in the twenty-fifty server directory in order to ensure that it is using this new version of the gem.

## 官网

- 主页: http://github.com/decc/decc_2050_model
- RubyGems: https://rubygems.org/gems/global_2050_model

## 历史版本号

- 0.0.2-x86_64-darwin-12 (2012-10-12)
- 0.0.2-x86_64-linux (2012-10-12)
- 0.0.2 (2012-10-12)
- 0.0.1-x86_64-darwin-12 (2012-10-11)
- 0.0.1-x86_64-linux (2012-10-11)
- 0.0.1 (2012-10-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/global_2050_model
- gem 安装: `gem install global_2050_model`
- Bundler: `gem "global_2050_model"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/global_2050_model-0.0.2.gem
- 版本锁定: `gem "global_2050_model", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
