# erbook

**Tag**: web, networking, template, filesystem, data

## 简介

ERBook 9.2.1

           Write books, manuals, and documents in eRuby

               http://snk.tuxfamily.org/lib/erbook/

   ERBook is an extensible document processor that emits [1]any
   document you can imagine from [2]eRuby templates, which allow
   scripting and dynamic content generation.

Version 9.2.1 (2009-11-18)

   This release fixes some bugs in, and improves the readability
   and load time of, generated XHTML documents.

   Bug fixes

     * Prevent search button from starting search when search
       box untouched.

     * Prevent browser from fetching base-64 embedded URI
       sources by qualifying their digests with the "cid" URI
       schema, which is used to identify the parts of a
       multi-part e-mail message.
       This cuts down on the amount of "404 - File Not Found"
       errors on the web server which hosts your generated XHTML
       documents because web browsers will not confuse these
       embedded "cid" digests as being relative HTTP files.

   Housekeeping

     * Increase vertical spacing between [3]References for
       better readability.

     * Embed W3C validator badges as base-64 data URIs to reduce
       page load time.

     * Split the document processing code in ERBook::Document
       into smaller self-documenting methods.

References

   1. http://snk.tuxfamily.org/lib/erbook/#HelloWorld
   2. http://en.wikipedia.org/wiki/ERuby
   3. http://snk.tuxfamily.org/lib/erbook/#_references

## 官网

- 主页: http://snk.tuxfamily.org/lib/erbook/
- RubyGems: https://rubygems.org/gems/erbook

## 历史版本号

- 9.2.1 (2009-11-19)
- 9.2.0 (2009-11-07)
- 9.1.0 (2009-11-03)
- 9.0.0 (2009-10-19)
- 8.0.0 (2009-10-11)
- 7.3.0 (2009-10-10)
- 7.1.1 (2009-09-24)
- 7.1.0 (2009-09-24)
- 7.0.0 (2009-09-24)
- 6.1.0 (2009-09-24)
- 6.0.1 (2009-09-24)
- 6.0.0 (2009-09-24)
- 5.0.0 (2009-09-24)
- 4.0.0 (2009-09-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/erbook
- gem 安装: `gem install erbook`
- Bundler: `gem "erbook"`
- 最新版本: 9.2.1
- 最新版归档: https://rubygems.org/downloads/erbook-9.2.1.gem
- 版本锁定: `gem "erbook", "~> 9.2.1"`
- 中央仓库: https://rubygems.org/
