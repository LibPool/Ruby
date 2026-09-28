# singleflight

**Tag**: library

## 简介

Its primary purpose is to ensure that only one call to an expensive or duplicative operation is in flight at any given time.
   When multiple requests request the same resource, singleflight ensures that the function is executed only once, and the result is shared among all callers.
   This pattern is particularly useful in scenarios where caching isn't suitable or when the results are expected to change frequently.

## 官网

- 主页: https://github.com/yoavgeva/singleflight
- 更新日志: https://github.com/yoavgeva/singleflight/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/singleflight

## 历史版本号

- 0.1.0 (2024-10-18)

## 获取地址

- RubyGems: https://rubygems.org/gems/singleflight
- gem 安装: `gem install singleflight`
- Bundler: `gem "singleflight"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/singleflight-0.1.0.gem
- 版本锁定: `gem "singleflight", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
