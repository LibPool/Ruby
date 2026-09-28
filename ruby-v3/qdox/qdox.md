# qdox

**Tag**: web, testing, networking, template, tooling, filesystem

## 简介

==== QDox - http://qdox.codehaus.org
QDox is a high speed, small footprint parser for extracting class/interface/method definitions from Java source files complete with JavaDoc @tags. It is designed to be used by active code generators or documentation tools.

QDox is a Java library. Therefore this RubyGem needs JRuby.

==== Quickstart
Step 1: Load your Java sources. In JRuby (or +jirb+)  write:
 require 'qdox'
 builder = QDox::JavaDocBuilder.new
 builder.add_source_tree(java.io.File.new(".")

(Source: http://qdox.codehaus.org/usage.html)

Step 2: Inspect the source model.
  src = builder.sources.first
  pkg = src.package
  puts pkg.name # e.g. "com.bla.foo"
  imports = src.imports # => e.g. ["java.util.List", "java.util.Set"]
  some_class = src.classes.first # => a QDox::Model::JavaClass

  # output the javadoc comment for the first method in some_class
  puts some_class.methods.first.comment 

(Source: http://qdox.codehaus.org/model.html)

As you may have noticed, the Java packages used have been aliased to shorter Ruby Module names:
The Java package com.thoughtworks.qdox is the Ruby module QDox etc.

==== In a Nutshell
A custom built parser has been built using JFlex and BYacc/J. These have been chosen because of their proven performance and they require no external libraries at runtime.

The parser skims the source files only looking for things of interest such as class/interface definitions, import statements, JavaDoc and member declarations. The parser ignores things such as actual method implementations to avoid overhead (while in method blocks, curly brace counting suffices).

The end result of the parser is a very simple document model containing enough information to be useful.

==== License
Apache License, Version 2.0
QDox was created by Joe Walnes, Aslak Hellesoy, Paul Hammant, Mike Williams, Mauro Talevi, Robert Scholte, and others.
The RubyGem was created by Benjamin Bock.

## 官网

- 主页: http://qdox.codehaus.org/
- RubyGems: https://rubygems.org/gems/qdox

## 历史版本号

- 1.10.1 (2010-03-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/qdox
- gem 安装: `gem install qdox`
- Bundler: `gem "qdox"`
- 最新版本: 1.10.1
- 最新版归档: https://rubygems.org/downloads/qdox-1.10.1.gem
- 版本锁定: `gem "qdox", "~> 1.10.1"`
- 中央仓库: https://rubygems.org/
