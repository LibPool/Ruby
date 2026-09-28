# chunky_png

**Tag**: web, testing, networking, filesystem, data

## 简介

This pure Ruby library can read and write PNG images without depending on an external
    image library, like RMagick. It tries to be memory efficient and reasonably fast.

    It supports reading and writing all PNG variants that are defined in the specification,
    with one limitation: only 8-bit color depth is supported. It supports all transparency,
    interlacing and filtering options the PNG specifications allows. It can also read and
    write textual metadata from PNG files. Low-level read/write access to PNG chunks is
    also possible.

    This library supports simple drawing on the image canvas and simple operations like
    alpha composition and cropping. Finally, it can import from and export to RMagick for
    interoperability.

    Also, have a look at OilyPNG at https://github.com/wvanbergen/oily_png. OilyPNG is a
    drop in mixin module that implements some of the ChunkyPNG algorithms in C, which
    provides a massive speed boost to encoding and decoding.

## 官网

- 主页: https://github.com/wvanbergen/chunky_png/wiki
- 源码仓库: https://github.com/wvanbergen/chunky_png
- RubyGems: https://rubygems.org/gems/chunky_png

## 历史版本号

- 1.4.0 (2020-12-28)
- 1.3.15 (2020-12-15)
- 1.3.14 (2020-10-27)
- 1.3.13 (2020-10-23)
- 1.3.12 (2020-08-03)
- 1.3.11 (2018-11-21)
- 1.3.10 (2018-01-23)
- 1.3.9 (2018-01-23)
- 1.3.8 (2016-11-11)
- 1.3.7 (2016-08-31)
- 1.3.6 (2016-06-19)
- 1.3.5 (2015-10-28)
- 1.3.4 (2015-02-16)
- 1.3.3 (2014-10-24)
- 1.3.2 (2014-10-18)
- 1.3.1 (2014-04-28)
- 1.3.0 (2014-02-10)
- 1.2.9 (2013-10-17)
- 1.2.8 (2013-03-30)
- 1.2.7 (2013-01-07)
- 1.2.6 (2012-08-07)
- 1.2.5 (2011-09-23)
- 1.2.4 (2011-09-14)
- 1.2.3 (2011-09-14)
- 1.2.2 (2011-09-14)
- 1.2.1 (2011-08-10)
- 1.2.0 (2011-05-08)
- 1.1.2 (2011-05-06)
- 1.1.1 (2011-04-22)
- 1.1.0 (2011-03-19)
- 1.0.1 (2011-03-08)
- 1.0.0 (2011-03-06)
- 1.0.0.rc2 (2011-03-02)
- 1.0.0.rc1 (2011-02-24)
- 1.0.0.beta2 (2011-01-28)
- 1.0.0.beta1 (2011-01-24)
- 0.12.0 (2010-12-12)
- 0.11.1 (2010-11-16)
- 0.11.0 (2010-11-01)
- 0.10.5 (2010-10-22)
- 0.10.4 (2010-10-18)
- 0.10.3 (2010-10-08)
- 0.10.2 (2010-10-05)
- 0.10.1 (2010-10-04)
- 0.10.0 (2010-10-04)
- 0.9.2 (2010-09-17)
- 0.9.1 (2010-09-16)
- 0.9.0 (2010-08-18)
- 0.8.0 (2010-07-01)
- 0.7.3 (2010-04-29)
- 0.7.1 (2010-03-23)
- 0.7.0 (2010-03-15)
- 0.6.0 (2010-02-26)
- 0.5.8 (2010-02-25)
- 0.5.7 (2010-02-25)
- 0.5.6 (2010-02-16)
- 0.5.5 (2010-02-16)
- 0.5.4 (2010-01-18)
- 0.5.3 (2010-01-17)
- 0.5.2 (2010-01-16)
- 0.5.1 (2010-01-16)
- 0.5.0 (2010-01-16)
- 0.0.5 (2010-01-13)
- 0.0.4 (2010-01-13)
- 0.0.3 (2010-01-13)
- 0.0.2 (2010-01-12)
- 0.0.1 (2010-01-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/chunky_png
- gem 安装: `gem install chunky_png`
- Bundler: `gem "chunky_png"`
- 最新版本: 1.4.0
- 最新版归档: https://rubygems.org/downloads/chunky_png-1.4.0.gem
- 版本锁定: `gem "chunky_png", "~> 1.4.0"`
- 中央仓库: https://rubygems.org/
