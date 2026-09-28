# jcnetdev-paperclip

**Tag**: cli, testing, filesystem

## 简介

Paperclip is intended as an easy file attachment library for ActiveRecord. The intent behind it was to keep setup as easy as possible and to treat files as much like other attributes as possible. This means they aren't saved to their final locations on disk, nor are they deleted if set to nil, until ActiveRecord::Base#save is called. It manages validations based on size and presence, if required. It can transform its assigned image into thumbnails if needed, and the prerequisites are as simple as installing ImageMagick (which, for most modern Unix-based systems, is as easy as installing the right packages). Attached files are saved to the filesystem and referenced in the browser by an easily understandable specification, which has sensible and useful defaults.

## 官网

- 主页: http://github.com/thoughtbot/paperclip
- 文档: https://www.rubydoc.info/gems/jcnetdev-paperclip/1.1
- RubyGems: https://rubygems.org/gems/jcnetdev-paperclip

## 历史版本号

- 1.0.20080704 (2014-08-11)
- 1.1 (2014-08-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/jcnetdev-paperclip
- gem 安装: `gem install jcnetdev-paperclip`
- Bundler: `gem "jcnetdev-paperclip"`
- 最新版本: 1.1
- 最新版归档: https://rubygems.org/downloads/jcnetdev-paperclip-1.1.gem
- 版本锁定: `gem "jcnetdev-paperclip", "~> 1.1"`
- 中央仓库: https://rubygems.org/
