# cocoapods-local-override

**Tag**: serialization, filesystem

## 简介

自动读取项目根目录下的 Podfile.local (YAML 格式)，
    在不修改 Podfile 的情况下，将指定的 pod 从远程依赖切换为本地路径依赖。
    也支持替换版本号和 git 分支。

    Podfile.local 示例：
    local_pods:
      SomePod: ../path/to/SomePod
      AnotherPod: ../path/to/AnotherPod
    replace_versions:
      SomePod: 1.2.3
    replace_branches:
      SomePod: develop

## 官网

- 主页: https://github.com/charleszhao888888/cocoapods-local-override
- 文档: https://www.rubydoc.info/gems/cocoapods-local-override/1.0.1
- RubyGems: https://rubygems.org/gems/cocoapods-local-override

## 历史版本号

- 1.0.1 (2026-08-24)
- 1.0.0 (2026-07-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/cocoapods-local-override
- gem 安装: `gem install cocoapods-local-override`
- Bundler: `gem "cocoapods-local-override"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/cocoapods-local-override-1.0.1.gem
- 版本锁定: `gem "cocoapods-local-override", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
