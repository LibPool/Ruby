# cocoapods-pack

**Tag**: testing, filesystem

## 简介

A CocoaPods plugin that converts a given podspec into its binary version.
For a given podspec, a zip file will be produced containing the binary representation of the original podspec sources.
Each platform is packed as an `xcframework` within the zip file.
Other attributes such as `resource_bundles` specified in the source podspec will also be packed.
A binary podspec is also generated that can be published to a CocoaPods specs repo.

## 官网

- 主页: https://github.com/square/cocoapods-pack
- 文档: https://www.rubydoc.info/gems/cocoapods-pack/1.0.1
- RubyGems: https://rubygems.org/gems/cocoapods-pack

## 历史版本号

- 1.0.1 (2021-12-07)
- 1.0.0 (2021-11-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/cocoapods-pack
- gem 安装: `gem install cocoapods-pack`
- Bundler: `gem "cocoapods-pack"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/cocoapods-pack-1.0.1.gem
- 版本锁定: `gem "cocoapods-pack", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
