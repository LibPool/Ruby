# stable_profile

**Tag**: web, testing, filesystem

## 简介

Solves a quirk of rspec --profile in some code bases: result vary with every random spec ordering. This seems to be due to differences in dependency load order, class initialization, and test server startup. This lib runs rspec --profile many times, averaging the results to always give the same (stable) and meaningful result.

## 官网

- 文档: https://www.rubydoc.info/gems/stable_profile/0.6.1
- RubyGems: https://rubygems.org/gems/stable_profile

## 历史版本号

- 0.6.1 (2023-11-02)
- 0.6.0 (2023-11-02)
- 0.5.0 (2023-11-02)
- 0.4.1 (2023-10-31)
- 0.4.0 (2023-10-31)
- 0.3.0 (2023-10-31)
- 0.2.0 (2023-10-31)
- 0.1.0 (2023-10-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/stable_profile
- gem 安装: `gem install stable_profile`
- Bundler: `gem "stable_profile"`
- 最新版本: 0.6.1
- 最新版归档: https://rubygems.org/downloads/stable_profile-0.6.1.gem
- 版本锁定: `gem "stable_profile", "~> 0.6.1"`
- 中央仓库: https://rubygems.org/
