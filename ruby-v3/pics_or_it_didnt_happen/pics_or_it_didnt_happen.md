# pics_or_it_didnt_happen

**Tag**: web, security, networking, template, filesystem, data

## 简介

Sometimes, you might want your HTML to include a one-off image file that is just for one person. Making this file public may be undesireable for security reasons, or perhaps simply because it is not worth the overhead of multiple HTTP requests.
This gem provides a utility method that takes a locally-saved image file, perhaps within your non-public tmp directory, encodes it as Base64, and returns an HTML <img> element with the correct data URL attributes.
It is made possible by the RFC 2397 scheme, which is now fairly well supported in modern browsers.

## 官网

- 主页: https://github.com/NeomindLabs/pics_or_it_didnt_happen
- 问题追踪: https://github.com/NeomindLabs/pics_or_it_didnt_happen/issues
- RubyGems: https://rubygems.org/gems/pics_or_it_didnt_happen

## 历史版本号

- 1.1.5 (2023-08-16)
- 1.1.4 (2023-08-16)
- 1.1.3 (2023-06-09)
- 1.1.2 (2023-04-20)
- 1.0.0 (2022-11-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/pics_or_it_didnt_happen
- gem 安装: `gem install pics_or_it_didnt_happen`
- Bundler: `gem "pics_or_it_didnt_happen"`
- 最新版本: 1.1.5
- 最新版归档: https://rubygems.org/downloads/pics_or_it_didnt_happen-1.1.5.gem
- 版本锁定: `gem "pics_or_it_didnt_happen", "~> 1.1.5"`
- 中央仓库: https://rubygems.org/
