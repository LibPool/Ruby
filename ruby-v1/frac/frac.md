# frac

**Tag**: library

## 简介

Find rational approximation to given real number.  Based on the theory of continued fractions  if x = a1 + 1/(a2 + 1/(a3 + 1/(a4 + ...)))  then best approximation is found by truncating this series (with some adjustments in the last term). Note the fraction can be recovered as the first column of the matrix  ( a1 1 ) ( a2 1 ) ( a3 1 ) ... ( 1  0 ) ( 1  0 ) ( 1  0 )  Instead of keeping the sequence of continued fraction terms, we just keep the last partial product of these matrices.

## 官网

- 主页: https://github.com/valodzka/frac
- RubyGems: https://rubygems.org/gems/frac

## 历史版本号

- 0.9.6 (2013-01-17)
- 0.9.5 (2011-07-25)
- 0.9.4 (2011-06-23)
- 0.9.3 (2010-05-26)
- 0.9.2 (2010-05-25)
- 0.9.1 (2010-05-25)
- 0.9.0 (2010-05-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/frac
- gem 安装: `gem install frac`
- Bundler: `gem "frac"`
- 最新版本: 0.9.6
- 最新版归档: https://rubygems.org/downloads/frac-0.9.6.gem
- 版本锁定: `gem "frac", "~> 0.9.6"`
- 中央仓库: https://rubygems.org/
