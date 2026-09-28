# extract_curves

**Tag**: filesystem

## 简介

Extract Curves a simplistic GTK Ruby-based appliaction which can convert the raster image file result of a geometric-trace-producing process's interaction with the characteristic of motion of another (interesting) process into a list of rectangular coordinates (in raster image's system) representing the inferred characteristic of motion of an image blob.  Blob recognition is done by color: * by maximum pixel neighbor-to-neighbor difference * by maximum difference from blob's average color * by maximum difference from a pixel neighborhood's average color (using RGB or HSV).  Use other software to pre-process (e.g. enhance contrast, or even reduce to gray scale), but Extract Curves's skeletonization is done based on the hypothesis of a recognized image blob, as opposed to a collection of pixels.  Output is human-readable (tab-separated).

## 官网

- 文档: https://www.rubydoc.info/gems/extract_curves/0.0.1
- RubyGems: https://rubygems.org/gems/extract_curves

## 历史版本号

- 0.0.1 (2009-09-24)
- 0.0.1-mswin32 (2009-09-24)
- 0.0.1-i586-linux (2009-09-24)

## 获取地址

- RubyGems: https://rubygems.org/gems/extract_curves
- gem 安装: `gem install extract_curves`
- Bundler: `gem "extract_curves"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/extract_curves-0.0.1.gem
- 版本锁定: `gem "extract_curves", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
