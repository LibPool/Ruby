# lazy_data

**Tag**: devops, data

## 简介

LazyData provides data types featuring thread-safe lazy computation. These objects are constructed with a block that can be called to compute the final value, but it is not actually called until the value is requested. Once requested, the computation takes place only once, in the first thread that requested the value. Future requests will return a cached value. Furthermore, any other threads that request the value during the initial computation will block until the first thread has completed the computation. This implementation also provides retry and expiration features. The code was extracted from the google-cloud-env gem that originally used it.

## 官网

- 主页: https://github.com/dazuma/lazy_data
- 源码仓库: https://github.com/dazuma/lazy_data/tree/lazy_data/v0.1.0
- 文档: https://dazuma.github.io/lazy_data/gem/v0.1.0
- 更新日志: https://dazuma.github.io/lazy_data/gem/v0.1.0/file.CHANGELOG.html
- 问题追踪: https://github.com/dazuma/lazy_data/issues
- RubyGems: https://rubygems.org/gems/lazy_data

## 历史版本号

- 0.1.0 (2026-03-19)
- 0.0.0 (2026-03-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/lazy_data
- gem 安装: `gem install lazy_data`
- Bundler: `gem "lazy_data"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/lazy_data-0.1.0.gem
- 版本锁定: `gem "lazy_data", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
