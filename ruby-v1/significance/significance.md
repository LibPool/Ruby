# significance

**Tag**: library

## 简介

Similar in behavior to Object#presence defined in ActiveSupport,
    Significance is a state which determines not just the blank-ness of an
    object but whether or not the non-blank object has any real-world value.
    The utility of this gem can best be demonstrated when considering the
    merging of two hashes. Under normal circumstances the mere existence of an
    equivalent key in the second hash results in its overriding the
    corresponding value in the original hash. Using Hash#significant_merge,
    however, the second hash will retain only key-value pairs whose values are
    "significant," even applying the significance filter recursively into child
    hashes or arrays.

## 官网

- 主页: http://github.com/caleon/significance
- RubyGems: https://rubygems.org/gems/significance

## 历史版本号

- 0.2.1 (2012-10-25)
- 0.2.0 (2012-10-22)
- 0.1.1 (2011-11-16)
- 0.1.0 (2011-11-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/significance
- gem 安装: `gem install significance`
- Bundler: `gem "significance"`
- 最新版本: 0.2.1
- 最新版归档: https://rubygems.org/downloads/significance-0.2.1.gem
- 版本锁定: `gem "significance", "~> 0.2.1"`
- 中央仓库: https://rubygems.org/
