# lorax

**Tag**: web, serialization, networking, template

## 简介

The Lorax is a full diff and patch library for XML/HTML documents, based on Nokogiri.

It can tell you whether two XML/HTML documents are identical, or if
they're not, tell you what's different. In trivial cases, it can even
apply the patch.

It's based loosely on Gregory Cobena's master's thesis paper, which
generates deltas in less than O(n * log n) time, accepting some
tradeoffs in the size of the delta set. You can find his paper at
http://gregory.cobena.free.fr/www/Publications/thesis.html.

"I am the Lorax, I speak for the trees."

## 官网

- 主页: http://github.com/flavorjones/lorax
- RubyGems: https://rubygems.org/gems/lorax

## 历史版本号

- 0.3.0.rc2 (2019-03-19)
- 0.3.0.rc1 (2012-10-12)
- 0.2.0 (2010-10-14)
- 0.1.0 (2010-03-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/lorax
- gem 安装: `gem install lorax`
- Bundler: `gem "lorax"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/lorax-0.2.0.gem
- 版本锁定: `gem "lorax", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
