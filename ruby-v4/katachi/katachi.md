# katachi

**Tag**: web, serialization

## 简介

== Description

A tool for describing and validating objects as intuitively as possible.
Easier to read and write than JSON Schema, and more powerful than a simple hash comparison.

Example usage:

  shape = {
      :$uuid => {
          email: :$email,
          first_name: String,
          last_name: String,
          preferred_name: AnyOf[String, nil],
          admin_only_information: AnyOf[{Symbol => String}, :$undefined],
          Symbol => Object,
      },
  }
  expect(api_response.body).to have_shape(shape)

## 官网

- 主页: https://github.com/jtannas/katachi
- 更新日志: https://github.com/jtannas/katachi/releases
- RubyGems: https://rubygems.org/gems/katachi

## 历史版本号

- 0.0.2.0 (2025-03-19)
- 0.0.1.4 (2025-03-18)
- 0.0.1.3 (2025-03-18)
- 0.0.1.2 (2025-03-18)
- 0.0.1.1 (2025-03-18)
- 0.0.1.0 (2025-03-18)
- 0.0.0.1 (2025-03-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/katachi
- gem 安装: `gem install katachi`
- Bundler: `gem "katachi"`
- 最新版本: 0.0.2.0
- 最新版归档: https://rubygems.org/downloads/katachi-0.0.2.0.gem
- 版本锁定: `gem "katachi", "~> 0.0.2.0"`
- 中央仓库: https://rubygems.org/
