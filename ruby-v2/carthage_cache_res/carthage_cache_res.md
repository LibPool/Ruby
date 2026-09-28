# carthage_cache_res

**Tag**: tooling, devops, filesystem

## 简介

CarthageCache generate a hash key based on the content of your Cartfile.resolved and checks
    if there is a cache archive (a zip file of your Carthage/Build directory) associated to that hash.
    If there is one it will download it and install it in your project avoiding the need to run carthage bootstrap.
    ----------------------Thanks Mr.Blas but now we are facing dependency conflict with Fastlane 2.144--------------------
    What I want to solve: Dependency conflict with Fastlane 2.144
    What I did: 
      1. Changed name of this gem to "carthage_cache_res"
      2. Fixed runtime dependencies: aws-sdk < 3, commander = 4.3.8
      3. Changed system dependency versions: ruby > 2.6, xcode 11.x

## 官网

- 主页: https://github.com/dokim/carthage_cache_res
- 文档: https://www.rubydoc.info/gems/carthage_cache_res/0.9.4
- RubyGems: https://rubygems.org/gems/carthage_cache_res

## 历史版本号

- 0.9.4 (2020-03-31)
- 0.9.3 (2020-03-31)
- 0.9.2 (2020-03-31)
- 0.9.1 (2020-03-31)

## 获取地址

- RubyGems: https://rubygems.org/gems/carthage_cache_res
- gem 安装: `gem install carthage_cache_res`
- Bundler: `gem "carthage_cache_res"`
- 最新版本: 0.9.4
- 最新版归档: https://rubygems.org/downloads/carthage_cache_res-0.9.4.gem
- 版本锁定: `gem "carthage_cache_res", "~> 0.9.4"`
- 中央仓库: https://rubygems.org/
