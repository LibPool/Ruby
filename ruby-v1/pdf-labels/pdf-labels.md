# pdf-labels

**Tag**: web, serialization, networking, template, tooling

## 简介

== DESCRIPTION:  Welcome to the PDF-Labels project.  Our aim is to make creating labels programmatically easy in Ruby.  This Library builds on top of &quot;PDF::Writer&quot;:http://ruby-pdf.rubyforge.org/ and uses the templates from &quot;gLabels&quot;:http://glabels.sourceforge.org.  What this means is easy, clean Ruby code to create many common label types without measuring the labels yourself!  All of this in pure Ruby (we use the XML templates from gLabels, we do NOT have a dependancy on gLabels, nor on Gnome)  == FEATURES/PROBLEMS:  * Works with all gLabels supported templates for rectangular labels * Does not yet work for CD labels (circles)  == SYNOPSIS:  p = PDFLabelPage.new(&quot;Avery  8160&quot;) # label is 2 x 10 #Some examples of adding labels p.add_label() # should add to col 1, row 1 p.add_label(:position =&gt; 1) # should add col 1, row 2 p.add_label(:text =&gt; &quot;Positoin 15&quot;, :position =&gt; 15) # should add col 2, row 1 p.add_label(:text =&gt; 'No Margin', :position =&gt; 5, :use_margin =&gt; false) #this doesn't use a margin p.add_label(:position =&gt; 9, :text =&gt; &quot;X Offset = 4, Y Offset = -6&quot;, :offset_x =&gt; 4, :offset_y =&gt; -6) p.add_label(:text =&gt; &quot;Centered&quot;, :position =&gt; 26, :justification =&gt; :center) # should add col 2, row 15 p.add_label(:text =&gt; &quot;[Right justified]&quot;, :justification =&gt; :right, :position =&gt; 28)# col 2, row 14, right justified. p.add_label(:position =&gt; 29) # should add col 2, row 15 p.add_label(:position =&gt; 8, :text =&gt; &quot;This was added last and has a BIG font&quot;, :font_size =&gt; 18)

## 官网

- 文档: https://www.rubydoc.info/gems/pdf-labels/2.0.1
- RubyGems: https://rubygems.org/gems/pdf-labels

## 历史版本号

- 2.0.1 (2009-07-25)
- 1.0.1 (2009-07-25)
- 1.0.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/pdf-labels
- gem 安装: `gem install pdf-labels`
- Bundler: `gem "pdf-labels"`
- 最新版本: 2.0.1
- 最新版归档: https://rubygems.org/downloads/pdf-labels-2.0.1.gem
- 版本锁定: `gem "pdf-labels", "~> 2.0.1"`
- 中央仓库: https://rubygems.org/
