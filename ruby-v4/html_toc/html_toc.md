# html_toc

**Tag**: web, template

## 简介

This gem is intended to be used in Rails pre-processing, after the page has been generated but before it is delivered to the requestor. 

It does a case-insensitive search in the source text for the pseudo-tag &lt;toc /&gt;, which marks where the table of contents will be placed. If the tag is not found, the unmodified source is returned.

If the tag is found, it searches the text for header tags in a given range, and add an id attribute if the header does not already have one. If no headers were found, it will remove the tag and return the modified source. 

If there are headers, a link is generated for each one, using the header's text and id for the link's text and href. The links are wrapped in some divs, with classes and ids added so the table of contents can be styled. The &lt;toc /&gt; pseudo-tag is then replaced with the table of contents, and the the modified source is returned.

## 官网

- 主页: https://github.com/GGadow/html_toc
- 文档: https://www.rubydoc.info/gems/html_toc/1.2.0
- RubyGems: https://rubygems.org/gems/html_toc

## 历史版本号

- 1.2.0 (2014-12-28)
- 1.1.0 (2014-12-13)
- 1.0.2 (2014-12-10)
- 1.0.1 (2014-12-10)
- 1.0.0 (2014-12-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/html_toc
- gem 安装: `gem install html_toc`
- Bundler: `gem "html_toc"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/html_toc-1.2.0.gem
- 版本锁定: `gem "html_toc", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
