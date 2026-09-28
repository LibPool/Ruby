# superators

**Tag**: testing, tooling

## 简介

== FEATURES/PROBLEMS:  * Presently a superator operand must support having a singleton class. Because true, false, nil, Symbols, and Fixnums are all specially optimized for in MRI and cannot have singleton classes, they can't be given to a superator. There are ways this can be potentially accounted for, but nothing is in place at the moment, causing this to be classified as a bug.  * When defining a superator in a class, any operators overloaded after the superator definition will override a superator definition. For example, if you create the superator &quot;&lt;---&quot; and then define the &lt;() operator, the superator will not work. In this case, the superator's definition should be somewhere after the &lt;() definition.  * Superators work by handling a binary Ruby operator specially and then building a chain of unary operators after it. For this reason, a superator must match the regexp /^(\*\*|\*|\/|%|\+|\-|&lt;&lt;|&gt;&gt;|&amp;|\||\^|&lt;=&gt;|&gt;=|&lt;=|&lt;|&gt;|===|==|=~)(\-|~|\+)+$/.  == SYNOPSIS:

## 官网

- 文档: https://www.rubydoc.info/gems/superators/0.9.1
- RubyGems: https://rubygems.org/gems/superators

## 历史版本号

- 0.9.1 (2009-07-25)
- 0.9.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/superators
- gem 安装: `gem install superators`
- Bundler: `gem "superators"`
- 最新版本: 0.9.1
- 最新版归档: https://rubygems.org/downloads/superators-0.9.1.gem
- 版本锁定: `gem "superators", "~> 0.9.1"`
- 中央仓库: https://rubygems.org/
