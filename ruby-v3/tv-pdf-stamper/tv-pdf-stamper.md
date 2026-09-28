# tv-pdf-stamper

**Tag**: template

## 简介

Fill out PDF forms (templates) using iText's PdfStamper.  == CAVEAT:  You have to use JRuby or RJB. You need Adobe LiveCycle Designer or Acrobat Professional to create the templates.  == EXAMPLE: pdf = PDF::Stamper.new("my_template.pdf") pdf.text :first_name, "Jason" pdf.text :last_name, "Yates" pdf.image :photo, "photo.jpg" pdf.checkbox :hungry pdf.save_as "my_output.pdf"

## 官网

- 主页: http://github.com/turbovote/pdf-stamper/
- RubyGems: https://rubygems.org/gems/tv-pdf-stamper

## 历史版本号

- 0.3.9 (2013-02-25)
- 0.3.8 (2013-01-21)
- 0.3.7 (2013-01-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/tv-pdf-stamper
- gem 安装: `gem install tv-pdf-stamper`
- Bundler: `gem "tv-pdf-stamper"`
- 最新版本: 0.3.9
- 最新版归档: https://rubygems.org/downloads/tv-pdf-stamper-0.3.9.gem
- 版本锁定: `gem "tv-pdf-stamper", "~> 0.3.9"`
- 中央仓库: https://rubygems.org/
