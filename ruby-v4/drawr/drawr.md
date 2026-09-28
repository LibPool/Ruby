# drawr

**Tag**: web, testing, template, data

## 简介

== DESCRIPTION:  This is a ruby wrapper around Plotr with a similar API to Gruff.  You can create graphs with a similar interface to Gruff, but offload the rendering to the browser!  == FEATURES/PROBLEMS:  * Needs more tests!  == SYNOPSIS:  An example in rails.  Your controller:  class GraphController &lt; ApplicationController def index @drawr = Drawr::Pie.new @drawr.title = &quot;Twan&quot; @drawr.data(&quot;One&quot;, [1]) @drawr.data('Two', [2]) @drawr.data('Three', [2]) @drawr.data('Four', [10]) @drawr.data('Five', [6]) end end  Your view:  &lt;html&gt; &lt;head&gt; &lt;%= javascript_include_tag 'prototype' %&gt; &lt;%= javascript_include_tag 'excanvas' %&gt; &lt;%= javascript_include_tag 'Plotr' %&gt; &lt;/head&gt; &lt;body&gt; &lt;%= @drawr %&gt; &lt;/body&gt; &lt;/html&gt;

## 官网

- 主页: http://seattlerb.org/
- RubyGems: https://rubygems.org/gems/drawr

## 历史版本号

- 1.0.1 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/drawr
- gem 安装: `gem install drawr`
- Bundler: `gem "drawr"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/drawr-1.0.1.gem
- 版本锁定: `gem "drawr", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
