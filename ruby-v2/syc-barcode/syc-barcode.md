# syc-barcode

**Tag**: web, filesystem, data

## 简介

= Barcode
Creating barcodes (at the moment only Interleaved2of5). 

== Usage
Create the barcode string and the barcode graphics data
    i2o5 = Interleave2of5("01199")
    code = i2o5.encode
    barcode = i2o5.barcode
    pdf = Prawn::Document.new
    barcode.to_pdf(pdf)

When used with rails add
    require 'interleave2of5'
to config/application.rb

The barcode can be used to create a graphical representation of the barcode.

== Release Notes
* Version 0.0.1
  Create barcode Interleaved 2 of 5 that can be added to a pdf file

* Version 0.0.2
  Fix check digit calculation

* Version 0.0.3
  Add valid? to check whether a decoded value (e.g. by a barcode scanner) is
  valid

== Licencse
Barcode is published under the MIT license

## 官网

- 主页: http://syc.dyndns.org/drupal
- 源码仓库: https://github.com/sugaryourcoffee/syc-barcode
- 文档: https://www.rubydoc.info/gems/syc-barcode/0.0.3
- RubyGems: https://rubygems.org/gems/syc-barcode

## 历史版本号

- 0.0.3 (2014-07-06)
- 0.0.2 (2013-06-16)
- 0.0.1 (2013-06-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/syc-barcode
- gem 安装: `gem install syc-barcode`
- Bundler: `gem "syc-barcode"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/syc-barcode-0.0.3.gem
- 版本锁定: `gem "syc-barcode", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
