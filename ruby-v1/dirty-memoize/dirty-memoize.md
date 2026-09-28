# dirty-memoize

**Tag**: testing

## 简介

Like Memoize, but designed for mutable and parametizable objects

Use when: 
1. You have one expensive method (\compute) which set many internal
   variables. So, is preferable lazy evaluation of these dependent variables.
2. The expensive operation depends on one or more parameters
3. Changes on one or more parameters affect all dependent variables
4. You may want to hide the call of 'compute' operation
5. The user could want test several different parameters values

## 官网

- 主页: http://github.com/clbustos/dirty-memoize
- RubyGems: https://rubygems.org/gems/dirty-memoize

## 历史版本号

- 0.0.4 (2011-01-26)
- 0.0.3 (2010-04-01)
- 0.0.1 (2010-04-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/dirty-memoize
- gem 安装: `gem install dirty-memoize`
- Bundler: `gem "dirty-memoize"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/dirty-memoize-0.0.4.gem
- 版本锁定: `gem "dirty-memoize", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
