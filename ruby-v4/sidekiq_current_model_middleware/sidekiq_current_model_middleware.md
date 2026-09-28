# sidekiq_current_model_middleware

**Tag**: web, cli, serialization

## 简介

This gem provides Sidekiq middleware that extends the functionality of Sidekiq's built-in CurrentAttributes to persist and restore ActiveSupport::CurrentAttributes across Sidekiq jobs, with added support for ActiveRecord models. It uses GlobalID for serialization and deserialization of ActiveRecord objects, allowing seamless integration with Rails applications to maintain context between web requests and background jobs. The middleware supports multiple CurrentAttributes classes and handles both client-side and server-side persistence.

## 官网

- 文档: https://www.rubydoc.info/gems/sidekiq_current_model_middleware/1.1.0
- RubyGems: https://rubygems.org/gems/sidekiq_current_model_middleware

## 历史版本号

- 1.1.0 (2024-08-01)
- 1.0.2 (2024-08-01)
- 1.0.1 (2024-08-01)

## 获取地址

- RubyGems: https://rubygems.org/gems/sidekiq_current_model_middleware
- gem 安装: `gem install sidekiq_current_model_middleware`
- Bundler: `gem "sidekiq_current_model_middleware"`
- 最新版本: 1.1.0
- 最新版归档: https://rubygems.org/downloads/sidekiq_current_model_middleware-1.1.0.gem
- 版本锁定: `gem "sidekiq_current_model_middleware", "~> 1.1.0"`
- 中央仓库: https://rubygems.org/
