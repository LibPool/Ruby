# pdf-storycards

**Tag**: cli, testing, filesystem

## 简介

== DESCRIPTION:  Provides a script and library to parse stories saved in the RSpec plain text story format and creates a PDF file with printable 3&quot;x5&quot; index cards suitable for using in Agile planning and prioritization.  == FEATURES/PROBLEMS:  * Create a PDF with each page as a 3x5 sheet, or as 4 cards per 8.5 x 11 sheet * Included script reads stories from STDIN and writes PDF to STDOUT * TODO: Improve test coverage * TODO: Improve documentation  == SYNOPSIS:  From the command line with stories2cards &lt; /path/to/stories.txt  Or via Ruby story_text = File.read('my_story') pdf_content = PDF::Storycards::Writer.make_pdf(story_text, :style =&gt; :card_1up)  == REQUIREMENTS:

## 官网

- 主页: http://rubyforge.org/projects/pdf-storycards/
- RubyGems: https://rubygems.org/gems/pdf-storycards

## 历史版本号

- 0.0.1 (2009-07-25)
- 0.1.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/pdf-storycards
- gem 安装: `gem install pdf-storycards`
- Bundler: `gem "pdf-storycards"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/pdf-storycards-0.1.0.gem
- 版本锁定: `gem "pdf-storycards", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
