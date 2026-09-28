# proc_eval

**Tag**: web, networking, template

## 简介

Adds an `evaulate` refinement method to Proc and Object instances.

    The goal of this gem is to allow evaluation of variables, procs, and lambdas with the same level of flexibility.

    The `evaluate` method has been added to the Object class to simply return the value of the variable.
    The `evaluate` method is overriden on the Proc class to allow parameters to be passed to lambdas in the same flexible way as procs.
    This takes into consideration, required/optional/remaining parameters, and required/optional/remaining keyword parameters.

    For information on Refinements, see:
    - https://ruby-doc.org/core-2.0.0/doc/syntax/refinements_rdoc.html
    - https://ruby-doc.org/core-2.1.0/doc/syntax/refinements_rdoc.html
    - https://ruby-doc.org/core-2.2.0/doc/syntax/refinements_rdoc.html
    - https://ruby-doc.org/core-2.3.0/doc/syntax/refinements_rdoc.html
    - https://ruby-doc.org/core-2.4.0/doc/syntax/refinements_rdoc.html
    - http://yehudakatz.com/2010/11/30/ruby-2-0-refinements-in-practice/

## 官网

- 主页: https://github.com/reeganviljoen/proc_eval
- 文档: https://www.rubydoc.info/gems/proc_eval/2.0.0
- RubyGems: https://rubygems.org/gems/proc_eval

## 历史版本号

- 2.0.0 (2023-09-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/proc_eval
- gem 安装: `gem install proc_eval`
- Bundler: `gem "proc_eval"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/proc_eval-2.0.0.gem
- 版本锁定: `gem "proc_eval", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
