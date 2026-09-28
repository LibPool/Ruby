# y_petri

**Tag**: testing, filesystem, data

## 简介

YPetri is a DSL (domain-specific language) for modelling of dynamical systems. It is biologically inspired, but concerns of biology and chemistry have been purposely separated away from it. YPetri caters solely to the two main concerns of modelling, model specification and simulation, and it excels in the first one. Dynamical systems are described under a Petri net paradigm. YPetri implements a universal Petri net abstraction that integrates discrete/continous, timed/timeless and stoichiometric/nonstoichiometric dichotomies of the extended Petri nets, and allows efficient specification of any kind of dynamical system. Like Petri nets themselves, YPetri was inspired by problems from the domain of chemistry (biochemical pathway modelling), but is not specific to it. Other gems, YChem and YCell are planned to cater to the concerns specific to chemistry and cell biochemistry. A lower-level extension of YPetri is currently under development under the name YNelson. Its usage is practically identical to YPetri, so any YPetri user can now consider using YNelson instead. YNelson covers additional concerns: it allows relations among nodes and parameters to be specified under a zz structure paradigm (developed by Ted Nelson) and it is also aimed towards providing a higher level of abstraction in Petri net specification by providing commands that create more than one Petri net node per command. YPetri documentation is avalable online, but due to formatting issues, you may prefer to generate the documentation on your own by running rdoc in the gem directory. As for the user manuals, there are currently 3 documents applicable for both YPetri and YNelson, whose master copies are stored in the YNelson source directory: 1. Introduction to YNelson and YPetri (hands-on tutorial), 2. Object model of YNelson and YPetri, 3. Introduction to Ruby for YNelson users. These manuals are written to allow beginners, including those unfamiliar with Ruby, to start working with YPetri and/or YNelson. For an example of how YPetri can be used to model complex dynamical systems, see the eukaryotic cell cycle model which I released as "cell_cycle" gem.

## 官网

- 源码仓库: https://github.com/boris-s/y_petri
- 文档: https://www.rubydoc.info/gems/y_petri/2.4.9
- RubyGems: https://rubygems.org/gems/y_petri

## 历史版本号

- 2.4.9 (2016-07-13)
- 2.4.8 (2016-06-28)
- 2.4.6 (2016-06-24)
- 2.4.4 (2016-06-23)
- 2.4.3 (2016-06-22)
- 2.4.2 (2016-03-11)
- 2.4.0 (2015-10-16)
- 2.3.12 (2015-10-09)
- 2.3.11 (2015-10-05)
- 2.3.10 (2014-12-08)
- 2.3.9 (2014-12-04)
- 2.3.8 (2014-12-03)
- 2.3.6 (2014-12-03)
- 2.3.5 (2014-11-30)
- 2.3.4 (2014-11-28)
- 2.3.3 (2014-04-24)
- 2.3.2 (2014-04-23)
- 2.2.4 (2013-10-22)
- 2.2.3 (2013-10-21)
- 2.2.2 (2013-10-18)
- 2.2.1 (2013-10-16)
- 2.2.0 (2013-10-14)
- 2.1.51 (2013-09-01)
- 2.1.50 (2013-08-31)
- 2.1.49 (2013-08-27)
- 2.1.48 (2013-08-26)
- 2.1.47 (2013-08-26)
- 2.1.46 (2013-08-24)
- 2.1.45 (2013-08-24)
- 2.1.44 (2013-08-24)
- 2.1.42 (2013-08-23)
- 2.1.40 (2013-08-23)
- 2.1.39 (2013-08-23)
- 2.1.37 (2013-08-22)
- 2.1.36 (2013-08-22)
- 2.1.35 (2013-08-22)
- 2.1.34 (2013-08-22)
- 2.1.33 (2013-08-22)
- 2.1.31 (2013-08-20)
- 2.1.30 (2013-08-20)
- 2.1.26 (2013-08-20)
- 2.1.25 (2013-08-20)
- 2.1.24 (2013-08-19)
- 2.1.22 (2013-08-18)
- 2.1.21 (2013-08-18)
- 2.1.20 (2013-08-18)
- 2.1.18 (2013-08-18)
- 2.1.17 (2013-08-18)
- 2.1.16 (2013-08-16)
- 2.1.12 (2013-08-12)
- 2.1.11 (2013-08-12)
- 2.1.10 (2013-08-11)
- 2.1.9 (2013-08-10)
- 2.1.7 (2013-08-09)
- 2.1.6 (2013-08-09)
- 2.1.3 (2013-08-01)
- 2.0.15 (2013-06-30)
- 2.0.14.p1 (2013-06-27)
- 2.0.14 (2013-06-27)
- 2.0.7 (2013-06-26)
- 2.0.3 (2013-05-13)
- 2.0.2 (2013-05-02)
- 2.0.1 (2013-05-02)
- 2.0.0 (2013-05-02)
- 1.0.0 (2013-04-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/y_petri
- gem 安装: `gem install y_petri`
- Bundler: `gem "y_petri"`
- 最新版本: 2.4.9
- 最新版归档: https://rubygems.org/downloads/y_petri-2.4.9.gem
- 版本锁定: `gem "y_petri", "~> 2.4.9"`
- 中央仓库: https://rubygems.org/
