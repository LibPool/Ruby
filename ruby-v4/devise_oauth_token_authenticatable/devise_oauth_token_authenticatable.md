# devise_oauth_token_authenticatable

**Tag**: web, cli, testing, security

## 简介

There are plenty of gems out there that deal with being an OAuth2 "consumer",
where you redirect users to an OAuth2 "provider", allowing you to hand off
authentication to a separate service. There are also plenty of gems that set
you up as your own OAuth2 provider. ***BUT***, what happens when you want to
separate your "authentication" server from your "resource" server?

This gem is meant to be used on an API "resource" server, where you want to
accept OAuth Access Tokens from a client, and validate them against a separate
"authentication" server. This communication is outside the scope of the
official OAuth 2 spec, but there is a need for it anyway.

## 官网

- 主页: https://github.com/mleglise/devise_oauth_token_authenticatable
- RubyGems: https://rubygems.org/gems/devise_oauth_token_authenticatable

## 历史版本号

- 0.0.2 (2012-08-06)
- 0.0.1 (2012-07-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/devise_oauth_token_authenticatable
- gem 安装: `gem install devise_oauth_token_authenticatable`
- Bundler: `gem "devise_oauth_token_authenticatable"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/devise_oauth_token_authenticatable-0.0.2.gem
- 版本锁定: `gem "devise_oauth_token_authenticatable", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
