# flexible_polyline

**Tag**: web, networking

## 简介

The flexible polyline encoding from heremaps is a lossy compressed representation of a list of coordinate pairs or coordinate triples. It achieves that by:
1. Reducing the decimal digits of each value.
2. Encoding only the offset from the previous point.
3. Using variable length for each coordinate delta.
4. Using 64 URL-safe characters to display the result.

For more information, visit: https://github.com/heremaps/flexible-polyline

## 官网

- 主页: https://github.com/ioki-mobility/ruby-flexible-polyline
- 更新日志: https://github.com/ioki-mobility/ruby-flexible-polyline/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/ioki-mobility/ruby-flexible-polyline/issues
- RubyGems: https://rubygems.org/gems/flexible_polyline

## 历史版本号

- 0.1.0 (2022-06-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/flexible_polyline
- gem 安装: `gem install flexible_polyline`
- Bundler: `gem "flexible_polyline"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/flexible_polyline-0.1.0.gem
- 版本锁定: `gem "flexible_polyline", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
