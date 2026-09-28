# permafrost

**Tag**: testing

## 简介

Environment variables are a standard way for configuring applications in
production. It allows for quickly changing the configuration, and avoids
having to introduce secrets in the code.

When testing code that relies on environment variables, it becomes
problematic to mock the environment, and even more to clean up afterwards.

Permafrost allows you to define a limited scope where the environment is
set as you decide, returning it to its original state afterwards.

## 官网

- 主页: https://github.com/subvisual/permafrost
- 更新日志: https://github.com/subvisual/permafrost/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/permafrost

## 历史版本号

- 1.0.0 (2020-06-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/permafrost
- gem 安装: `gem install permafrost`
- Bundler: `gem "permafrost"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/permafrost-1.0.0.gem
- 版本锁定: `gem "permafrost", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
