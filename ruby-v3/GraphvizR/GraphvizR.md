# GraphvizR

**Tag**: web, cli, testing, networking, template, filesystem

## 简介

Graphviz wrapper for Ruby. This can be used as a common library, a rails plugin and a command line tool.  == FEATURES/PROBLEMS:  GraphvizR is graphviz adapter for Ruby, and it can: * generate a graphviz dot file, * generate an image file by means of utilizing graphviz, * interprete rdot file and generate an image file, * and, generate a graph image file in rails application as a rails plugin. == SYNOPSYS:  === Command Line:  bin/graphviz_r sample/record.rdot  === In Your Code: This ruby code:  gvr = GraphvizR.new 'sample' gvr.graph [:label =&gt; 'example', :size =&gt; '1.5, 2.5']  gvr.beta [:shape =&gt; :box]                       gvr.alpha &gt;&gt; gvr.beta (gvr.beta &gt;&gt; gvr.delta) [:label =&gt; 'label1'] gvr.delta &gt;&gt; gvr.gamma gvr.to_dot  replies the dot code:  digraph sample { graph [label = &quot;example&quot;, size = &quot;1.5, 2.5&quot;]; beta [shape = box]; alpha -&gt; beta; beta -&gt; delta [label = &quot;label1&quot;]; delta -&gt; gamma; }  To know more detail, please see test/test_graphviz_r.rb  === On Rails :  &lt;b&gt;use _render :rdot_ in controller&lt;/b&gt; def show_graph render :rdot do graph [:size =&gt; '1.5, 2.5'] node [:shape =&gt; :record] node1 [:label =&gt; &quot;&lt;p_left&gt; left|&lt;p_center&gt;center|&lt;p_right&gt; right&quot;] node2 [:label =&gt; &quot;left|center|right&quot;] node1 &gt;&gt; node2 node1(:p_left) &gt;&gt; node2 node2 &gt;&gt; node1(:p_center) (node2 &gt;&gt; node1(:p_right)) [:label =&gt; 'record'] end end  &lt;b&gt;use rdot view template&lt;/b&gt;  class RdotGenController &lt; ApplicationController def index @label1 = &quot;&lt;p_left&gt; left|&lt;p_center&gt;center|&lt;p_right&gt; right&quot; @label2 = &quot;left|center|right&quot; end end  # view/rdot_gen/index.rdot graph [:size =&gt; '1.5, 2.5'] node [:shape =&gt; :record] node1 [:label =&gt; @label1] node2 [:label =&gt; @label2] node1 &gt;&gt; node2 node1(:p_left) &gt;&gt; node2 node2 &gt;&gt; node1(:p_center) (node2 &gt;&gt; node1(:p_right)) [:label =&gt; 'record']  == DEPENDENCIES:  * Graphviz (http://www.graphviz.org)  == TODO:  == INSTALL:  * sudo gem install graphviz_r * if you want to use this in ruby on rails * script/plugin install http://technohippy.net/svn/repos/graphviz_r/trunk/vendor/plugins/rdot   == LICENSE:  (The MIT License)

## 官网

- 主页: http://blog.technohippy.net/pages/products/graphviz_r/en
- RubyGems: https://rubygems.org/gems/GraphvizR

## 历史版本号

- 0.5.1 (2009-07-25)
- 0.5.0 (2009-07-25)
- 0.4.0 (2009-07-25)
- 0.3.2 (2009-07-25)
- 0.3.1 (2009-07-25)
- 0.3.0 (2009-07-25)
- 0.2.0 (2009-07-25)
- 0.1.0 (2009-07-25)
- 0.0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/GraphvizR
- gem 安装: `gem install GraphvizR`
- Bundler: `gem "GraphvizR"`
- 最新版本: 0.5.1
- 最新版归档: https://rubygems.org/downloads/GraphvizR-0.5.1.gem
- 版本锁定: `gem "GraphvizR", "~> 0.5.1"`
- 中央仓库: https://rubygems.org/
