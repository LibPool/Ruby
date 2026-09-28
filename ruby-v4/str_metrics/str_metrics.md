# str_metrics

**Tag**: web, networking

## 简介

Ruby gem (native extension in Rust) providing implementations of various string metrics. Current metrics supported are: Sørensen–Dice, Levenshtein, Damerau–Levenshtein, Jaro & Jaro–Winkler. Strings that are UTF-8 encodable (convertible to UTF-8 representation) are supported. All comparison of strings is done at the grapheme cluster level as described by Unicode Standard Annex #29 (https://www.unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries); this may be different from many gems that calculate string metrics.

## 官网

- 主页: https://github.com/anirbanmu/str_metrics
- 更新日志: https://github.com/anirbanmu/str_metrics/blob/v0.1.1/CHANGELOG.md
- 问题追踪: https://github.com/anirbanmu/str_metrics/issues
- RubyGems: https://rubygems.org/gems/str_metrics

## 历史版本号

- 0.1.1 (2020-03-15)
- 0.1.0 (2020-03-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/str_metrics
- gem 安装: `gem install str_metrics`
- Bundler: `gem "str_metrics"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/str_metrics-0.1.1.gem
- 版本锁定: `gem "str_metrics", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
