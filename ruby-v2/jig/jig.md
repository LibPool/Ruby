# jig

**Tag**: serialization, template

## 简介

A jig is an ordered sequence of objects (usually strings) and named _gaps_.  When rendered as a string by Jig#to_s, the objects are rendered calling #to_s on each object in order. The gaps are skipped.  A new jig may be constructed from an existing jig by 'plugging' one or more of the named gaps.  The new jig shares the objects and their ordering from the original jig but with the named gap replaced with the 'plug'.  Gaps may be plugged by any object or sequence of objects.  When a gap is plugged with another jig, the contents (including gaps) are incorporated into the new jig.  Several subclasses (Jig::XML, Jig::XHTML, Jig::CSS) are defined to help in the construction of XML, XHTML, and CSS documents.  This is a jig with a single gap named :alpha. Jig.new(:alpha)                         # =&gt; &lt;#Jig: [:alpha]&gt; This is a jig with two objects, 'before' and 'after' separated by a gap named :middle. j = Jig.new('before', :middle, 'after)  # =&gt; #&lt;Jig: [&quot;before&quot;, :middle, &quot;after&quot;]&gt; The plug operation derives a new jig from the old jig. j.plug(:middle, &quot;, during, and&quot;)        # =&gt; #&lt;Jig: [&quot;before&quot;, &quot;, during, and &quot;, &quot;after&quot;]&gt; This operation doesn't change j.  It can be used again: j.plug(:middle, &quot; and &quot;)                # =&gt; #&lt;Jig: [&quot;before&quot;, &quot; and &quot;, &quot;after&quot;]&gt; There is a destructive version of plug that modifies the jig in place: j.plug!(:middle, &quot;filled&quot;)          # =&gt; #&lt;Jig: [&quot;before&quot;, &quot;filled&quot;, &quot;after&quot;]&gt; j                                   # =&gt; #&lt;Jig: [&quot;before&quot;, &quot;filled&quot;, &quot;after&quot;]&gt; There are a number of ways to construct a Jig and many of them insert an implicit gap into the Jig.  This gap is identified as :___ and is used as the default gap for plug operations when one isn't provided:

## 官网

- 主页: http://jig.rubyforge.org
- RubyGems: https://rubygems.org/gems/jig

## 历史版本号

- 0.1.2 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/jig
- gem 安装: `gem install jig`
- Bundler: `gem "jig"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/jig-0.1.2.gem
- 版本锁定: `gem "jig", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
