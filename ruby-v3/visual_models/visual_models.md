# visual_models

**Tag**: web, cli, testing, template, filesystem

## 简介

visual_models mounts a self-contained D3-powered association graph at any path in your
Rails app. It introspects ApplicationRecord (and, optionally, ActiveModel-only
classes) at runtime, walks every reflection (belongs_to, has_one, has_many,
has_many :through, has_and_belongs_to_many, polymorphic), and renders an
interactive force-directed graph with search, zoom, drag-to-rearrange, position
persistence, and a click-through details panel.

Ships with zero asset-pipeline dependencies — D3 and Stimulus are loaded from CDN.
Recommended for development environments only.

## 官网

- 主页: https://github.com/pniemczyk/visual_models
- 文档: https://pniemczyk.github.io/visual_models/
- 更新日志: https://github.com/pniemczyk/visual_models/blob/main/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/visual_models

## 历史版本号

- 0.1.0 (2026-04-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/visual_models
- gem 安装: `gem install visual_models`
- Bundler: `gem "visual_models"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/visual_models-0.1.0.gem
- 版本锁定: `gem "visual_models", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
