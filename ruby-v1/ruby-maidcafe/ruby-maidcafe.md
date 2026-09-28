# ruby-maidcafe

**Tag**: web, cli, networking

## 简介

By utilizing this library, you can retrieve information of Japanese  Maidcafe via Maidcafe API web service (http://moeten.info/maidcafe/?m=api). This can be used as interactive command line tool, non-interactive one,  and library.  == SYNOPSIS:  In your code:  * get shop list api = Maidcafe::API.new rs = api.list :shop puts rs.description rs.items.each do |item| puts item.name puts item.id end	 * get shop information in osaka rs = api.shop :prefecture =&gt; Maidcafe::Prefecture::OSAKA puts rs.description rs.items.each do |item| puts item.name puts item.description puts item.opening_hour end

## 官网

- 文档: https://www.rubydoc.info/gems/ruby-maidcafe/0.0.1
- RubyGems: https://rubygems.org/gems/ruby-maidcafe

## 历史版本号

- 0.0.1 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/ruby-maidcafe
- gem 安装: `gem install ruby-maidcafe`
- Bundler: `gem "ruby-maidcafe"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/ruby-maidcafe-0.0.1.gem
- 版本锁定: `gem "ruby-maidcafe", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
