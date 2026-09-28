# acts_as_wrapped_class

**Tag**: library

## 简介

== FEATURES/PROBLEMS:  *  Wrappers do not dispatch const_missing yet, so constants are not accessible yet.  == SYNOPSIS:  class Something acts_as_wrapped_class :methods =&gt; [:safe_method] # SomethingWrapper is now defined  def safe_method  # allowed to access this method through SomethingWrapper Something.new end  def unsafe_method  # not allowed to access this method through SomethingWrapper end end

## 官网

- 文档: https://www.rubydoc.info/gems/acts_as_wrapped_class/1.0.1
- RubyGems: https://rubygems.org/gems/acts_as_wrapped_class

## 历史版本号

- 1.0.1 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/acts_as_wrapped_class
- gem 安装: `gem install acts_as_wrapped_class`
- Bundler: `gem "acts_as_wrapped_class"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/acts_as_wrapped_class-1.0.1.gem
- 版本锁定: `gem "acts_as_wrapped_class", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
