# safe_uri

**Tag**: filesystem

## 简介

SafeURI is an alternative implementation that allows you to open an URI with safer approach - with SafeURI.#open, you can always force to use URI.parse(url).open, or File.open(filename) depending on the provided argument. The pipe character '|' is NOT accepted as it does not delegate to Kernel.#open (falls back to File.#open), unlike URI.#open that falls back to Kernel.#open when un-openable arguments are given.

## 官网

- 主页: https://github.com/fursich/safe_uri
- 文档: https://www.rubydoc.info/gems/safe_uri/0.1.0
- RubyGems: https://rubygems.org/gems/safe_uri

## 历史版本号

- 0.1.0 (2019-04-06)

## 获取地址

- RubyGems: https://rubygems.org/gems/safe_uri
- gem 安装: `gem install safe_uri`
- Bundler: `gem "safe_uri"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/safe_uri-0.1.0.gem
- 版本锁定: `gem "safe_uri", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
