# jekyll_html_truncatewords

**Tag**: testing, template

## 简介

A Jekyll filter to truncate HTML to a specified number of words. The Liquid truncatewords filter can't operate on HTML because it isn't aware of tags. But Jekyll blog posts usually contain HTML, so this makes it difficult to, for example, use the first 50 words of a blog post as the preview. jekyll_html_truncatewords solves that problem. It works the same as truncatewords, but it is aware of HTML tags so it counts words correctly within HTML and won't break HTML.

## 官网

- 主页: https://github.com/mkasberg/jekyll_html_trunctewords
- 更新日志: https://github.com/mkasberg/jekyll_html_trunctewords/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/jekyll_html_truncatewords

## 历史版本号

- 0.1.2 (2021-01-24)
- 0.1.1 (2021-01-24)
- 0.1.0 (2020-12-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/jekyll_html_truncatewords
- gem 安装: `gem install jekyll_html_truncatewords`
- Bundler: `gem "jekyll_html_truncatewords"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/jekyll_html_truncatewords-0.1.2.gem
- 版本锁定: `gem "jekyll_html_truncatewords", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
