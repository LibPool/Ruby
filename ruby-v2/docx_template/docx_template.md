# docx_template

**Tag**: template

## 简介

template = DocxTemplate::Docx.new "/opt/docx_template.docx"
    template.replace_text("##SINGLE_REPLACE_TEXT##", "ACTUAL TEXT HERE")
    template.replace_text("##MULTI_REPLACE_TEXT##", "ACTUAL TEXT HERE", true)
    template.replace_header("##HEADER_REPLACE_TEXT##", "ACTUAL TEXT HERE", true)
    template.replace_image("image1.jpeg", "/opt/image5.jpg")
    template.save('/opt/final.docx')

## 官网

- 主页: https://www.facebook.com/maniankara
- 文档: https://www.rubydoc.info/gems/docx_template/0.7
- RubyGems: https://rubygems.org/gems/docx_template

## 历史版本号

- 0.7 (2014-09-26)
- 0.6 (2014-09-24)
- 0.5 (2014-09-23)
- 0.4 (2014-09-22)
- 0.3 (2014-09-22)
- 0.2 (2014-09-21)
- 0.1 (2014-09-20)

## 获取地址

- RubyGems: https://rubygems.org/gems/docx_template
- gem 安装: `gem install docx_template`
- Bundler: `gem "docx_template"`
- 最新版本: 0.7
- 最新版归档: https://rubygems.org/downloads/docx_template-0.7.gem
- 版本锁定: `gem "docx_template", "~> 0.7"`
- 中央仓库: https://rubygems.org/
