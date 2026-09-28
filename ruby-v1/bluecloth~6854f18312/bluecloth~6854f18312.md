# bluecloth

**Tag**: web, networking, template

## 简介

BlueCloth is a Ruby implementation of John Gruber's
Markdown[http://daringfireball.net/projects/markdown/], a text-to-HTML
conversion tool for web writers. To quote from the project page: Markdown
allows you to write using an easy-to-read, easy-to-write plain text format,
then convert it to structurally valid XHTML (or HTML).

It borrows a naming convention and several helpings of interface from
{Redcloth}[http://redcloth.org/], Why the Lucky Stiff's processor for a
similar text-to-HTML conversion syntax called
Textile[http://www.textism.com/tools/textile/].

BlueCloth 2 is a complete rewrite using David Parsons'
Discount[http://www.pell.portland.or.us/~orc/Code/discount/] library, a C
implementation of Markdown. I rewrote it using the extension for speed and
accuracy; the original BlueCloth was a straight port from the Perl version
that I wrote in a few days for my own use just to avoid having to shell out to
Markdown.pl, and it was quite buggy and slow. I apologize to all the good
people that sent me patches for it that were never released.

Note that the new gem is called 'bluecloth' and the old one 'BlueCloth'. If
you have both installed, you can ensure you're loading the new one with the
'gem' directive:

	# Load the 2.0 version
	gem 'bluecloth', '>= 2.0.0'
	
	# Load the 1.0 version
	gem 'BlueCloth'
	require 'bluecloth'

## 官网

- 主页: http://deveiate.org/projects/BlueCloth
- 文档: http://deveiate.org/code/bluecloth/
- 问题追踪: http://deveiate.org/projects/BlueCloth/query
- RubyGems: https://rubygems.org/gems/bluecloth

## 历史版本号

- 2.2.0 (2011-11-01)
- 2.1.0-x86-mswin32 (2011-03-12)
- 2.1.0-x86-mingw32 (2011-03-12)
- 2.1.0 (2011-03-12)
- 2.0.11 (2011-02-10)
- 2.0.11-x86-mswin32 (2011-02-10)
- 2.0.11-x86-mingw32 (2011-02-10)
- 2.0.11pre158-x86-mingw32 (2011-02-10)
- 2.0.11pre158-x86-mswin32 (2011-02-10)
- 2.0.11pre158 (2011-02-10)
- 2.0.10 (2011-01-17)
- 2.0.9 (2010-09-23)
- 2.0.7 (2010-01-25)
- 2.0.7-x86-mswin32 (2010-01-25)
- 2.0.7-x86-mingw32 (2010-01-25)
- 2.0.7.pre126 (2010-01-24)
- 2.0.7.pre126-x86-mswin32 (2010-01-24)
- 2.0.7.pre126-x86-mingw32 (2010-01-24)
- 2.0.6-x86-mswin32 (2010-01-17)
- 2.0.6-x86-mingw32 (2010-01-17)
- 2.0.6 (2010-01-17)
- 2.0.6.pre122-x86-mswin32 (2010-01-17)
- 2.0.6.pre122-x86-mingw32 (2010-01-17)
- 2.0.6.pre122 (2010-01-17)
- 2.0.6.pre120-x86-mswin32 (2010-01-16)
- 2.0.6.pre120-x86-mingw32 (2010-01-16)
- 2.0.6.pre120 (2010-01-16)
- 2.0.5-x86-mingw32 (2009-09-15)
- 2.0.0 (2009-08-12)
- 2.0.1 (2009-08-12)
- 2.0.2 (2009-08-12)
- 2.0.3 (2009-08-12)
- 2.0.4 (2009-08-12)
- 2.0.5 (2009-08-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/bluecloth
- gem 安装: `gem install bluecloth`
- Bundler: `gem "bluecloth"`
- 最新版本: 2.2.0
- 最新版归档: https://rubygems.org/downloads/bluecloth-2.2.0.gem
- 版本锁定: `gem "bluecloth", "~> 2.2.0"`
- 中央仓库: https://rubygems.org/
