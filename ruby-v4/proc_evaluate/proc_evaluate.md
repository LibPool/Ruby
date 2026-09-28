# proc_evaluate

**Tag**: web, networking, template

## 简介

Adds an `evaluate` refinement method to Proc and Object instances.

    The goal of this gem is to allow the evaluation of variables, procs, and lambdas with the same level of flexibility.

    The `evaluate` method has been added to the Object class to return the evaluated value of the variable.
    The `evaluate` method is overridden on the Proc class to allow parameters to be passed to lambdas in the same flexible way as procs.
    This takes into consideration, required/optional/remaining parameters, and required/optional/remaining keyword parameters.

    For information on Refinements, see:
    - https://ruby-doc.org/core-2.0.0/doc/syntax/refinements_rdoc.html
    - https://ruby-doc.org/core-2.1.0/doc/syntax/refinements_rdoc.html
    - https://ruby-doc.org/core-2.2.0/doc/syntax/refinements_rdoc.html
    - https://ruby-doc.org/core-2.3.0/doc/syntax/refinements_rdoc.html
    - https://ruby-doc.org/core-2.4.0/doc/syntax/refinements_rdoc.html
    - http://yehudakatz.com/2010/11/30/ruby-2-0-refinements-in-practice/

## 官网

- 主页: https://github.com/br3nt/proc_evaluate
- 文档: https://www.rubydoc.info/gems/proc_evaluate/1.1.1
- RubyGems: https://rubygems.org/gems/proc_evaluate

## 历史版本号

- 1.1.1 (2023-11-02)
- 1.1.0 (2023-09-05)
- 1.0.0 (2017-10-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/proc_evaluate
- gem 安装: `gem install proc_evaluate`
- Bundler: `gem "proc_evaluate"`
- 最新版本: 1.1.1
- 最新版归档: https://rubygems.org/downloads/proc_evaluate-1.1.1.gem
- 版本锁定: `gem "proc_evaluate", "~> 1.1.1"`
- 中央仓库: https://rubygems.org/
