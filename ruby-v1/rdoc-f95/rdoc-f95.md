# rdoc-f95

**Tag**: web, testing, networking, template, tooling, filesystem

## 简介

RDocF95 is an improved RDoc for generation of documents of Fortran 90/95 programs.   Differences to the original one are given below.   &lt;b&gt;Enhancement of &quot;parser/f95.rb&quot;&lt;/b&gt; :: The Fortran 90/95 parse script &quot;parser/f95.rb&quot; (In rdoc-f95, old name &quot;parsers/parse_f95.rb&quot; is used yet) is modified  in order to parse almost all entities of the Fortran 90/95 Standard.   &lt;b&gt;Addition of &lt;tt&gt;--ignore-case&lt;/tt&gt; option &lt;/b&gt; :: In the Fortran 90/95 Standard,   upper case letters are not distinguished from lower case letters,  although original RDoc produces case-dependently  cross-references of Class and  Methods. When this options is specified,  upper cases are not distinguished from lower cases.  &lt;b&gt;Cross-reference of file names&lt;/b&gt; :: Cross-reference of file names is available as well as modules, subroutines, and so on.  &lt;b&gt;Modification of &lt;tt&gt;--style&lt;/tt&gt; option&lt;/b&gt; :: Original RDoc can not treat relative path stylesheet. Application of this patch modifies this function.  &lt;b&gt;Conversion of TeX formula into MathML&lt;/b&gt;:: TeX formula can be converted into MathML format with --mathml option,  if &lt;b&gt;MathML library for Ruby version 0.6b -- 0.8&lt;/b&gt; is installed. This library is available from {Bottega of Hiraku (only JAPANESE)}[http://www.hinet.mydns.jp/~hiraku/]. See {RDocF95::Markup::ToXHtmlTexParser}[link:classes/RDocF95/Markup/ToXHtmlTexParser.html] about format.  &lt;b&gt;*** Caution ***&lt;/b&gt; Documents generated with &quot;--mathml&quot; option are not displayed correctly according to browser and/or its setting. We have been confirmed that  documents generated with &quot;--mathml&quot; option are displayed correctly with {Mozilla Firefox}[http://www.mozilla.org/products/firefox/] and Internet Explorer (+ {MathPlayer}[http://www.dessci.com/en/products/mathplayer/]). See {MathML Software - Browsers}[http://www.w3.org/Math/Software/mathml_software_cat_browsers.html] for other browsers.  Some formats of comments in HTML document are changed to improve the analysis features. See {parse_f95.rb}[link:files/lib/rdoc-f95/parsers/parse_f95_rb.html]

## 官网

- 文档: https://www.rubydoc.info/gems/rdoc-f95/0.0.2
- RubyGems: https://rubygems.org/gems/rdoc-f95

## 历史版本号

- 0.0.2 (2009-07-25)
- 0.0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/rdoc-f95
- gem 安装: `gem install rdoc-f95`
- Bundler: `gem "rdoc-f95"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/rdoc-f95-0.0.2.gem
- 版本锁定: `gem "rdoc-f95", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
