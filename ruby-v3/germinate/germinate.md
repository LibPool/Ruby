# germinate

**Tag**: web, testing, networking, devops, filesystem

## 简介

Germinate is a tool for writing about code.  With Germinate, the source code IS the article.  For example, given the following source code:  # #!/usr/bin/env ruby # :BRACKET_CODE: &lt;pre&gt;, &lt;/pre&gt; # :PROCESS: ruby, &quot;ruby %f&quot;  # :SAMPLE: hello def hello(who) puts &quot;Hello, #{who}&quot; end  hello(&quot;World&quot;)  # :TEXT: # Check out my amazing program!  Here's the hello method: # :INSERT: @hello:/def/../end/  # And here's the output: # :INSERT: @hello|ruby  When we run the &lt;tt&gt;germ format&lt;/tt&gt; command the following output is generated:  Check out my amazing program!  Here's the hello method: &lt;pre&gt; def hello(who) puts &quot;Hello, #{who}&quot; end &lt;/pre&gt; And here's the output: &lt;pre&gt; Hello, World &lt;/pre&gt;  To get a better idea of how this works, please take a look at link:examples/basic.rb, or run:  germ generate &gt; basic.rb  To generate an example article to play with.  Germinate is particularly useful for writing articles, such as blog posts, which contain code excerpts.  Instead of forcing you to keep a source code file and an article document in sync throughout the editing process, the Germinate motto is &quot;The source code IS the article&quot;.  Specially marked comment sections in your code file become the article text.  Wherever you need to reference the source code in the article, use insertion directives to tell Germinate what parts of the code to excerpt.  An advanced selector syntax enables you to be very specific about which lines of code you want to insert.  If you also want to show the output of your code, Germinate has you covered. Special &quot;process&quot; directives enable you to define arbitrary commands which can be run on your code.  The output of the command then becomes the excerpt text. You can define an arbitrary number of processes and have different excerpts showing the same code as processed by different commands.  You can even string processes together into pipelines.  Development of Germinate is graciously sponsored by Devver, purveyor of fine cloud-based services to busy Ruby developers.  If you like this tool please check them out at http://devver.net.

## 官网

- 主页: http://github.com/devver/germinate/
- RubyGems: https://rubygems.org/gems/germinate

## 历史版本号

- 1.2.0 (2009-08-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/germinate
- gem 安装: `gem install germinate`
- Bundler: `gem "germinate"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/germinate-1.2.0.gem
- 版本锁定: `gem "germinate", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
