# scicom

**Tag**: web, cli, database, data

## 简介

SciCom (Scientific Computing) for Ruby brings the power of R to the Ruby community. SciCom 
is based on Renjin, a JVM-based interpreter for the R language for statistical computing.

Over the past two decades, the R language for statistical computing has emerged as the de 
facto standard for analysts, statisticians, and scientists. Today, a wide range of 
enterprises – from pharmaceuticals to insurance – depend on R for key business uses. Renjin 
is a new implementation of the R language and environment for the Java Virtual Machine (JVM),
whose goal is to enable transparent analysis of big data sets and seamless integration with 
other enterprise systems such as databases and application servers.

Renjin is still under development, but it is already being used in production for a number 
of client projects, and supports most CRAN packages, including some with C/Fortran 
dependencies.

SciCom integrates with Renjin and allows the use of R inside a Ruby script. In a sense, 
SciCom is similar to other solutions such as RinRuby, Rpy2, PipeR, etc. However, since 
SciCom and Renjin both target the JVM there is no need to integrate both solutions and 
there is no need to send data between Ruby and R, as it all resides in the same JVM. 
Further, installation of SciCom does not require the installation of GNU R; Renjin is the 
interpreter and comes with SciCom. Finally, although SciCom provides a basic interface to 
Renjin similar to RinRuby, a much tighter integration is also possible.

## 官网

- 主页: http://github.com/rbotafogo/scicom/wiki
- 文档: https://www.rubydoc.info/gems/scicom/0.4.1
- RubyGems: https://rubygems.org/gems/scicom

## 历史版本号

- 0.4.1-java (2016-03-14)
- 0.4.0-java (2016-03-03)
- 0.3.0-java (2015-03-19)
- 0.2.3.1-java (2015-01-02)
- 0.2.3-java (2014-12-30)
- 0.2.2-java (2014-11-19)
- 0.2.1-java (2014-11-16)
- 0.2.0-java (2014-11-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/scicom
- gem 安装: `gem install scicom`
- Bundler: `gem "scicom"`
- 最新版本: 0.4.1
- 最新版归档: https://rubygems.org/downloads/scicom-0.4.1.gem
- 版本锁定: `gem "scicom", "~> 0.4.1"`
- 中央仓库: https://rubygems.org/
