# inquiry_attrs

**Tag**: web

## 简介

InquiryAttrs wraps ActiveRecord/ActiveModel (and StoreModel/Dry::Struct) attributes with
predicate-style inquiry methods. Write user.status.active? instead of
user.status == "active". Blank/nil values safely return false for every
predicate — no more NoMethodError on nil. Run `rails inquiry_attrs:install`
to generate an initializer that auto-includes the concern into every
ActiveRecord model.

## 官网

- 主页: https://github.com/pniemczyk/inquiry_attrs
- 更新日志: https://github.com/pniemczyk/inquiry_attrs/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/inquiry_attrs

## 历史版本号

- 1.0.2 (2026-02-27)
- 1.0.1 (2026-02-27)
- 1.0.0 (2026-02-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/inquiry_attrs
- gem 安装: `gem install inquiry_attrs`
- Bundler: `gem "inquiry_attrs"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/inquiry_attrs-1.0.2.gem
- 版本锁定: `gem "inquiry_attrs", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
