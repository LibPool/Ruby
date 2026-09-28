# g1nn13-image_science

**Tag**: web, testing, networking, tooling

## 简介

g1nn13 fork changes:

* added buffer() method to get image buffer for writing (to Amazon S3)
* added fit_within() method to resize an image to fit within a specified
  height and width without changing the image's aspect ratio
* added resize_with_crop() to resize and crop images where the
  target aspect ratio differs from the original aspect ratio. This is
  for converting portrait to landscape and landscape to portrait.



ImageScience is a clean and happy Ruby library that generates
thumbnails -- and kicks the living crap out of RMagick. Oh, and it
doesn't leak memory like a sieve. :)

For more information including build steps, see http://seattlerb.rubyforge.org/

## 官网

- 主页: http://github.com/g1nn13/image_science
- RubyGems: https://rubygems.org/gems/g1nn13-image_science

## 历史版本号

- 1.2.10 (2011-08-10)
- 1.2.9 (2010-06-02)
- 1.2.8 (2010-05-27)
- 1.2.7 (2010-05-26)
- 1.2.6 (2010-05-26)
- 1.2.5 (2010-01-26)
- 1.2.4 (2010-01-26)
- 1.2.3 (2010-01-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/g1nn13-image_science
- gem 安装: `gem install g1nn13-image_science`
- Bundler: `gem "g1nn13-image_science"`
- 最新版本: 1.2.10
- 最新版归档: https://rubygems.org/downloads/g1nn13-image_science-1.2.10.gem
- 版本锁定: `gem "g1nn13-image_science", "~> 1.2.10"`
- 中央仓库: https://rubygems.org/
