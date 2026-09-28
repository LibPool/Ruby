# xipio

**Tag**: web

## 简介

When reading the subdomain of an xip.io request, you will get a different value
compared to a local pow request. The reason for this is that the tld length is
1 by default, but an xip.io request has a tld length of 6. This gem inserts a
middleware that corrects the tld length config of rails on the fly so that you
can use local and xip requests at the same time without restarting the server.

## 官网

- 主页: https://github.com/fphilipe/xipio
- 文档: https://www.rubydoc.info/gems/xipio/1.0.2
- RubyGems: https://rubygems.org/gems/xipio

## 历史版本号

- 1.0.2 (2018-02-28)
- 1.0.1 (2018-02-06)
- 1.0.0 (2013-06-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/xipio
- gem 安装: `gem install xipio`
- Bundler: `gem "xipio"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/xipio-1.0.2.gem
- 版本锁定: `gem "xipio", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
