# ply

**Tag**: web, networking, filesystem, data

## 简介

Ply is a ruby gem for reading Stanford PLY-format 3D model files.

The PLY file format is a flexible format for storing semi-structured binary
data, and is often used to stored polygonalized 3D models generated with
range scanning hardware.  You can find some examples of the format at the
{Stanford 3D Scanning Repository}[http://graphics.stanford.edu/data/3Dscanrep/].
 
Ply provides a simple API for quick access to the data in a PLY file
(including examining the structure of a particular file's content), and
an almost-as-simple event-driven API which can be used to process extremely
large ply files in a streaming fashion, without needing to keep the full
dataset represented in the file in memory.  Ply handles all three types of
PLY files (ascii, binary-big-endian and binary-little-endian).

If you don't have any Stanford PLY files on hand, you probably don't need
this gem, but if you're curious, the PLY file format is described at
Wikipedia[http://en.wikipedia.org/wiki/PLY_(file_format)].

## 官网

- 主页: https://github.com/jimwise/ply
- RubyGems: https://rubygems.org/gems/ply

## 历史版本号

- 0.9.1 (2013-03-30)
- 0.9 (2013-02-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/ply
- gem 安装: `gem install ply`
- Bundler: `gem "ply"`
- 最新版本: 0.9.1
- 最新版归档: https://rubygems.org/downloads/ply-0.9.1.gem
- 版本锁定: `gem "ply", "~> 0.9.1"`
- 中央仓库: https://rubygems.org/
