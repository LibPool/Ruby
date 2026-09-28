# status_enumerator

**Tag**: library

## 简介

This class provides an enumeration function to have the object which I added tree information to in an argument.
The instance receives an enumerable object and provides #each and #each_method. The #each method calls a block in an argument in own. The #each_method method calls the method of an object appointed own in an argument.
I have the information of the object equal to the ancestors in own and front and back and hierarchy structure, and a block and the argument handed to a method maintain the state flag in the enumeration again.
It is necessary to appoint the information about the descendant in the hierarchy structure in a block - a method explicitly. When the #into method receives an enumerable object, and a block is not exhibited, a block - a method is used recursively.
This class provides a function to enumerate it, but it is not the object which it can enumerate.

## 官网

- 主页: http://github.com/Ktouth/status_enumerator
- RubyGems: https://rubygems.org/gems/status_enumerator

## 历史版本号

- 0.0.3 (2011-06-19)
- 0.0.2 (2011-05-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/status_enumerator
- gem 安装: `gem install status_enumerator`
- Bundler: `gem "status_enumerator"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/status_enumerator-0.0.3.gem
- 版本锁定: `gem "status_enumerator", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
