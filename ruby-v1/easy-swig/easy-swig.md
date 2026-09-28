# easy-swig

**Tag**: web, cli, networking, tooling, filesystem, data

## 简介

Library and CLI-Tool for automatic generation wrappers for C/C++ code using SWIG.
This is both a Ruby Gem and a CLI Tool. Feed it with a directory containing the library's header files (the ones you want to wrap) and a CSV File with basic configuration (see usage). EasySwig will generate the corresponding SWIG interface files (.i) in an output directory. EasySwig also offers a facade allowing you to directly call SWIG in order to generate wrappers in the target language.

EasySwig relies on the Doxyparser gem (https://github.com/davfuenmayor/ruby-doxygen-parser) which on his part depends on Nokogiri (http://nokogiri.org) and Doxygen (www.doxygen.org). Refer to Doxyparser for more information.
For using EasySwig you may also want to install SWIG (http://www.swig.org/). SWIG versions 2.x and 3.x are supported.

EasySwig supports currently only C#. There is  ongoing work on other languages support.

## 官网

- 主页: http://github.com/davfuenmayor/easy-swig
- 文档: https://www.rubydoc.info/gems/easy-swig/1.1
- RubyGems: https://rubygems.org/gems/easy-swig

## 历史版本号

- 1.1 (2014-05-11)
- 1.0 (2014-05-02)

## 获取地址

- RubyGems: https://rubygems.org/gems/easy-swig
- gem 安装: `gem install easy-swig`
- Bundler: `gem "easy-swig"`
- 最新版本: 1.1
- 最新版归档: https://rubygems.org/downloads/easy-swig-1.1.gem
- 版本锁定: `gem "easy-swig", "~> 1.1"`
- 中央仓库: https://rubygems.org/
