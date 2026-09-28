# tree.rb

**Tag**: testing, tooling

## 简介

(This gem was named as treevisitor)
tree.rb is a 'clone' of tree unix command. The gem implements a library to mange tree structures.
The gem contains also a library to build tree with a dsl (domain specific language), and
an implementation of visitor design pattern.
An example of DSL to build tree:
&lt;pre&gt;
   tree = TreeNode.create do
     node "root" do
       leaf "l1"
       node "sub" do
         leaf "l3"
       end
       node "wo leaves"
     end
&lt;/pre&gt;

## 官网

- 主页: http://github.com/tokiro/tree.rb
- 源码仓库: https://github.com/tokiro/tree.rb
- 文档: https://www.rubydoc.info/gems/tree.rb/0.3.13
- 问题追踪: https://github.com/tokiro/tree.rb/issues
- RubyGems: https://rubygems.org/gems/tree.rb

## 历史版本号

- 0.3.13 (2016-03-07)
- 0.3.12 (2013-08-21)
- 0.3.11 (2013-04-18)
- 0.3.10 (2012-09-22)
- 0.3.9 (2012-09-16)
- 0.3.8 (2012-09-15)
- 0.3.7 (2012-09-01)
- 0.3.6 (2012-08-19)
- 0.3.5 (2012-08-19)
- 0.3.4 (2012-08-18)
- 0.3.3 (2012-08-18)
- 0.3.2 (2012-08-16)
- 0.3.1 (2012-08-15)
- 0.3.0 (2012-08-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/tree.rb
- gem 安装: `gem install tree.rb`
- Bundler: `gem "tree.rb"`
- 最新版本: 0.3.13
- 最新版归档: https://rubygems.org/downloads/tree.rb-0.3.13.gem
- 版本锁定: `gem "tree.rb", "~> 0.3.13"`
- 中央仓库: https://rubygems.org/
