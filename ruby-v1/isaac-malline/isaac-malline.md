# isaac-malline

**Tag**: web, serialization, networking, template, filesystem

## 简介

Malline is a full-featured template system designed to be a replacement for ERB views in Rails or any other framework. It also includes standalone bin/malline to compile Malline templates to XML in commandline. All Malline templates are pure Ruby, see http://www.malline.org/ for more info.  See documentation on http://www.malline.org/  Copyright Â© 2007,2008 Riku PalomÃ¤ki, riku@palomaki.fi Malline is released under GNU Lesser General Public License.   Example Rails template file images.html.mn:  xhtml do _render :partial =&gt; 'head' body do div.images! "There are some images:" do images.each do |im| a(:href =&gt; img_path(im)) { img :src =&gt; im.url } span.caption im.caption end _"No more images" end div.footer! { _render :partial =&gt; 'footer' } end end

## 官网

- 主页: http://www.malline.org/
- 文档: https://www.rubydoc.info/gems/isaac-malline/1.1.0
- RubyGems: https://rubygems.org/gems/isaac-malline

## 历史版本号

- 1.1.0 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/isaac-malline
- gem 安装: `gem install isaac-malline`
- Bundler: `gem "isaac-malline"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/isaac-malline-1.1.0.gem
- 版本锁定: `gem "isaac-malline", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
