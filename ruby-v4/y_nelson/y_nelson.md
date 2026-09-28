# y_nelson

**Tag**: testing, template, data

## 简介

Zz structures are an interesting way of representing relations invented by Ted Nelson, whose domain model I provide in a gem Yzz. In this gem, YNelson, I combine Yzz with the universal Petri net provided by YPetri (another gem I wrote) to obtain a hybrid data structure that formalizes and generelizes a spreadsheet. Because let us note spreadsheets (as I have seen them) can be considered Petri nets of a kind, with cell functions acting as Petri net transitions. At the same time, spreadsheets are globally orthogonal structures with 3 typical dimensions (rows, columns and sheets). By using zz structures, the globally orthogonal spreadsheet is generalized as a locally orthogonal zz structure, with relations represented as zz dimensions, thus generalizing and formalizing a spreadsheet. The catch is that I have not yet finished the thinking process regarding what everything should be a zz object: Places (cells) and transitions definitely yes, but how about nets and dimensions? Should YNelson go as far as making namespaces into zz objects? The reason why these questions are hard to answer is because Ted Nelson himself, while providing interfaces guidelines (zz structure views, cursors...) did not comment on these questions. While being a (textual) DSL, YNelson aims to provide convenience on par with actual spreadsheet apps. Unlike YPetri, YNelson also aims to be able to specify more than one Petri net node per command, but this is still under development. See the user guide and the documentation for the details. YNelson documentation is available online, but due to formatting issues, you may prefer to generate the documentation on your own by running rdoc in the gem directory. For an example of how YPetri can be used to model complex dynamical systems, see the eukaryotic cell cycle model which I released as "cell_cycle" gem.

## 官网

- 源码仓库: https://github.com/boris-s/y_nelson
- 文档: https://www.rubydoc.info/gems/y_nelson/2.3.8
- RubyGems: https://rubygems.org/gems/y_nelson

## 历史版本号

- 2.3.8 (2016-07-13)
- 2.3.7 (2016-06-28)
- 2.3.6 (2016-06-22)
- 2.3.4 (2014-12-03)
- 2.3.3 (2014-12-03)
- 2.3.2 (2014-12-02)
- 2.3.0 (2014-04-23)
- 2.1.0 (2013-10-21)
- 2.0.8 (2013-09-03)
- 2.0.7 (2013-09-01)
- 2.0.6 (2013-08-24)
- 2.0.5 (2013-08-23)
- 2.0.4 (2013-08-22)
- 2.0.3 (2013-08-20)
- 2.0.1 (2013-08-18)
- 0.1.5 (2013-05-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/y_nelson
- gem 安装: `gem install y_nelson`
- Bundler: `gem "y_nelson"`
- 最新版本: 2.3.8
- 最新版归档: https://rubygems.org/downloads/y_nelson-2.3.8.gem
- 版本锁定: `gem "y_nelson", "~> 2.3.8"`
- 中央仓库: https://rubygems.org/
