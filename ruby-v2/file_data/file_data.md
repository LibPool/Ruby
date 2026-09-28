# file_data

**Tag**: web, testing, filesystem, data

## 简介

Provides apis for extracting common metadata out of files as well as low level apis for advanced metadata parsing. Currently exif (jpeg/jpg) is almost entirely supported and mpeg4 (mp4,m4v,moov...) has limited support. For common metadata the FileInfo class provides methods names after the metadata items taking a filename. As an example, to get the origin date of a file you would call FileData::FileInfo.origin_date(filename). Advanced apis are provided via specific classes for each metadata type. For example, Exif for exif data and Mpeg4 for mpeg4 data. These can be used to improve the performance of gathering multiple metadata values from a file

## 官网

- 主页: https://github.com/ScottHaney/file_data
- RubyGems: https://rubygems.org/gems/file_data

## 历史版本号

- 6.0.0 (2021-11-22)
- 5.2.3 (2021-10-21)
- 5.2.2 (2018-07-21)
- 5.2.1 (2018-07-21)
- 5.2.0 (2018-07-21)
- 5.0.0 (2017-05-24)
- 4.0.0 (2017-05-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/file_data
- gem 安装: `gem install file_data`
- Bundler: `gem "file_data"`
- 最新版本: 6.0.0
- 最新版归档: https://rubygems.org/downloads/file_data-6.0.0.gem
- 版本锁定: `gem "file_data", "~> 6.0.0"`
- 中央仓库: https://rubygems.org/
