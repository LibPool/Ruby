# rmmseg-cpp

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

- 主页: http://rmmseg-cpp.rubyforge.org
- RubyGems: https://rubygems.org/gems/rmmseg-cpp

## 历史版本号

- 0.2.9 (2011-09-10)
- 0.2.7 (2009-07-25)
- 0.2.6 (2009-07-25)
- 0.2.5 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/rmmseg-cpp
- gem 安装: `gem install rmmseg-cpp`
- Bundler: `gem "rmmseg-cpp"`
- 最新版本: 0.2.9
- 最新版归档: https://rubygems.org/downloads/rmmseg-cpp-0.2.9.gem
- 版本锁定: `gem "rmmseg-cpp", "~> 0.2.9"`
- 中央仓库: https://rubygems.org/
