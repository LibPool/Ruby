# json_logging

**Tag**: web, serialization

## 简介

Emits one JSON object per log line without replacing Rails.logger. Existing
calls keep working: strings become the "message" field, hashes are merged as
fields, and exceptions are expanded into a structured "error" object.
ActiveSupport::TaggedLogging stays fully functional, and registered tags of
the form "name=value" are promoted to first-class JSON fields instead of
being flattened into a "[name=value]" message prefix. Optional log
subscribers replace the framework's prose output with typed fields.

## 官网

- 主页: https://github.com/atpoint-cloud/json_logging
- 文档: https://github.com/atpoint-cloud/json_logging/blob/main/README.md
- 更新日志: https://github.com/atpoint-cloud/json_logging/blob/main/CHANGELOG.md
- 问题追踪: https://github.com/atpoint-cloud/json_logging/issues
- RubyGems: https://rubygems.org/gems/json_logging

## 历史版本号

- 0.1.0 (2026-08-12)

## 获取地址

- RubyGems: https://rubygems.org/gems/json_logging
- gem 安装: `gem install json_logging`
- Bundler: `gem "json_logging"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/json_logging-0.1.0.gem
- 版本锁定: `gem "json_logging", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
