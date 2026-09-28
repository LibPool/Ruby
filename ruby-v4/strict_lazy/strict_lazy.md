# strict_lazy

**Tag**: web, testing, template

## 简介

strict_lazy applies the spirit of Rails' strict_loading to computed values
(external APIs, window functions, cross-table aggregates) that associations
cannot express. It forces explicit preloading and raises on unloaded access
in development/test, so hidden per-record queries never slip into views.
No batch-loader / N1Loader / ar_lazy_preload dependency — activesupport only.

## 官网

- 主页: https://github.com/aki77/strict_lazy
- 更新日志: https://github.com/aki77/strict_lazy/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/strict_lazy

## 历史版本号

- 0.4.1 (2026-06-20)
- 0.4.0 (2026-06-15)
- 0.3.0 (2026-06-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/strict_lazy
- gem 安装: `gem install strict_lazy`
- Bundler: `gem "strict_lazy"`
- 最新版本: 0.4.1
- 最新版归档: https://rubygems.org/downloads/strict_lazy-0.4.1.gem
- 版本锁定: `gem "strict_lazy", "~> 0.4.1"`
- 中央仓库: https://rubygems.org/
