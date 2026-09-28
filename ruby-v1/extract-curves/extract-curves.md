# extract-curves

**Tag**: filesystem

## 简介

Extract Curves a simplistic GTK Ruby-based appliaction which can convert the raster image file result of a geometric-trace-producing process's interaction with the characteristic of motion of another (interesting) process into a list of rectangular coordinates (in raster image's system) representing the inferred characteristic of motion of the midline of an image blob.  Blob recognition is done by color: * by maximum pixel neighbor-to-neighbor difference * by maximum difference from blob's average color * by maximum difference from a pixel neighborhood's average color (using RGB or HSV).  Use other software to pre-process (e.g. enhance contrast, or even reduce to gray scale), but Extract Curves's skeletonization is done based on the hypothesis of a recognized image blob, as opposed to a collection of pixels.  Output is human-readable (tab-separated).

## 官网

- 文档: https://www.rubydoc.info/gems/extract-curves/0.1.1
- RubyGems: https://rubygems.org/gems/extract-curves

## 历史版本号

- 0.1.1 (2009-09-24)
- 0.1.1-mswin32 (2009-09-24)
- 0.1.1-i586-linux (2009-09-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/extract-curves
- gem 安装: `gem install extract-curves`
- Bundler: `gem "extract-curves"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/extract-curves-0.1.1.gem
- 版本锁定: `gem "extract-curves", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
