# spatialnetworks-pdf-stamper

**Tag**: networking, template

## 简介

Super cool PDF templates using iText's PdfStamper.  == CAVEAT:  Anything super cool must have a caveat. You have to use JRuby or RJB. Plus you can only use Adobe LiveCycle Designer to create the templates.  == EXAMPLE: pdf = PDF::Stamper.new("my_template.pdf") pdf.text :first_name, "Jason" pdf.text :last_name, "Yates" pdf.image :photo, "photo.jpg" pdf.save_as "my_output.pdf"

## 官网

- 主页: http://github.com/spatialnetworks/pdf-stamper/
- RubyGems: https://rubygems.org/gems/spatialnetworks-pdf-stamper

## 历史版本号

- 0.3.0 (2010-08-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/spatialnetworks-pdf-stamper
- gem 安装: `gem install spatialnetworks-pdf-stamper`
- Bundler: `gem "spatialnetworks-pdf-stamper"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/spatialnetworks-pdf-stamper-0.3.0.gem
- 版本锁定: `gem "spatialnetworks-pdf-stamper", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
