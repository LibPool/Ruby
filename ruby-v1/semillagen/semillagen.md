# semillagen

**Tag**: testing, serialization, template, tooling, filesystem

## 简介

SemillaGen let's you create (Actionscript3.0 based) projects and classes with ease.
SemillaGen generated projects or classes are customizable via templates.

The default templates setup the project for Continuous Integration using FlexUnit.
the default class template creates a class and a test case automatically.

usage:

To create a new project run:
  $ semillagen project MyAwesomeProject  
  $ ls
  MyAwesomeProject
  
To create a new class with test case:
  $ cd MyAwesomeProject
  $ semillagen class com.semilla.MillionDollarClass
  
You will see that semillagen created the following files:
src/com/semilla/MillionDollarClass.as
test-src/com/semilla/MillionDollarClassTest.as

The default template is ready for building as soon as created.
To build and test your project we use rake.

  $ rake
  
Rake will build a debug and release versions of your project. It will also create a FlexUnit test swf and run the test.
You will see the results of the tests and also you will see some xml files under the [test-report] folder. These reports
are JUnit compatible.

You can use a CI tool like Jenkins to automatically build and test your project.

## 官网

- 主页: http://github.com/vicro/SemillaGen/
- 源码仓库: https://github.com/vicro/SemillaGen
- RubyGems: https://rubygems.org/gems/semillagen

## 历史版本号

- 0.0.2 (2012-05-10)
- 0.0.1 (2012-04-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/semillagen
- gem 安装: `gem install semillagen`
- Bundler: `gem "semillagen"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/semillagen-0.0.2.gem
- 版本锁定: `gem "semillagen", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
