# lijia-rmmseg-cpp

**Tag**: web, networking

## 简介

rmmseg-cpp is a high performance Chinese word segmentation utility for
Ruby. It features full "Ferret":http://ferret.davebalmain.com/ integration
as well as support for normal Ruby program usage.

rmmseg-cpp is a re-written of the original
RMMSeg(http://rmmseg.rubyforge.org/) gem in C++. RMMSeg is written
in pure Ruby. Though I tried hard to tweak RMMSeg, it just consumes
lots of memory and the segmenting process is rather slow.

The interface is almost identical to RMMSeg but the performance is
much better. This gem is always preferable in production
use. However, if you want to understand how the MMSEG segmenting
algorithm works, the source code of RMMSeg is a better choice than
this.

## 官网

- 主页: https://github.com/user-tony/rmmseg-cpp
- 文档: https://www.rubydoc.info/gems/lijia-rmmseg-cpp/10.2.9.2
- RubyGems: https://rubygems.org/gems/lijia-rmmseg-cpp

## 历史版本号

- 10.2.9.2 (2014-09-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/lijia-rmmseg-cpp
- gem 安装: `gem install lijia-rmmseg-cpp`
- Bundler: `gem "lijia-rmmseg-cpp"`
- 最新版本: 10.2.9.2
- 最新版归档: https://rubygems.org/downloads/lijia-rmmseg-cpp-10.2.9.2.gem
- 版本锁定: `gem "lijia-rmmseg-cpp", "~> 10.2.9.2"`
- 中央仓库: https://rubygems.org/
