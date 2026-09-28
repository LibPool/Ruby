# kickflow

**Tag**: web, cli, security, networking

## 简介

This gem is a REST API client for the kickflow[https://kickflow.com/].
For its REST API documentation, see {kickflow Developer / REST API}[https://developer.kickflow.com/rest/].

Example::
  Kickflow.configure { |config| config.access_token = YOUR_ACCESS_TOKEN }
  Kickflow::DefaultApi.new.get_categories(debug_auth_names: ["Authorization"]) #=> [...]

## 官网

- 主页: https://codeberg.org/gemmaro/kickflow
- 文档: https://www.rubydoc.info/gems/kickflow
- 更新日志: https://codeberg.org/gemmaro/kickflow/src/branch/main/CHANGELOG.md
- 问题追踪: https://codeberg.org/gemmaro/kickflow/issues
- RubyGems: https://rubygems.org/gems/kickflow

## 历史版本号

- 0.3.0 (2025-02-10)
- 0.2.1 (2024-10-17)
- 0.2.0 (2024-10-07)
- 0.1.0 (2024-08-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/kickflow
- gem 安装: `gem install kickflow`
- Bundler: `gem "kickflow"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/kickflow-0.3.0.gem
- 版本锁定: `gem "kickflow", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
