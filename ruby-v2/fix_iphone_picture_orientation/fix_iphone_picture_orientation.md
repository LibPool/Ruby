# fix_iphone_picture_orientation

**Tag**: testing

## 简介

Convert iPhone images to have a useful Orientation tag value
and be internally correctly oriented.

The iPhone has used the EXIF tag Orientation to store the actual
orientation of the camera. A lot of programs and libraries don't
seem to understand this, especially online photo galleries such
as Flickr and Gallery.

This program will modify the image to rotate it internally according
to the iPhone's orientation value, and then set the EXIF orientation
tag to "Horizontal (normal)" thus removing the confusion.

## 官网

- 主页: http://github.com/tamouse/fix_iphone_orientation.git
- 文档: https://www.rubydoc.info/gems/fix_iphone_picture_orientation/0.0.1
- RubyGems: https://rubygems.org/gems/fix_iphone_picture_orientation

## 历史版本号

- 0.0.1 (2013-11-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/fix_iphone_picture_orientation
- gem 安装: `gem install fix_iphone_picture_orientation`
- Bundler: `gem "fix_iphone_picture_orientation"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/fix_iphone_picture_orientation-0.0.1.gem
- 版本锁定: `gem "fix_iphone_picture_orientation", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
