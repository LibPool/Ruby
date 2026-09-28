# pdf-stamper

**Tag**: template

## 简介

Super cool PDF templates using iText's PdfStamper.  == CAVEAT:  Anything super cool must have a caveat. You have to use JRuby or RJB. Plus you can only use Adobe LiveCycle Designer to create the templates.  == EXAMPLE: pdf = PDF::Stamper.new(&quot;my_template.pdf&quot;) pdf.text :first_name, &quot;Jason&quot; pdf.text :last_name, &quot;Yates&quot; pdf.image :photo, &quot;photo.jpg&quot; pdf.save_as &quot;my_output.pdf&quot;

## 官网

- 主页: http://github.com/jaywhy/pdf-stamper/
- RubyGems: https://rubygems.org/gems/pdf-stamper

## 历史版本号

- 0.3.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/pdf-stamper
- gem 安装: `gem install pdf-stamper`
- Bundler: `gem "pdf-stamper"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/pdf-stamper-0.3.0.gem
- 版本锁定: `gem "pdf-stamper", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
