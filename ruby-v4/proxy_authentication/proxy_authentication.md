# proxy_authentication

**Tag**: web, security

## 简介

ProxyAuthentication allows two Rails applications to share an authenticated user, through a url token.
    App A can (through its own authentication system, e.g. Devise) authenticate a user, and then generate a link to App B
    with the encoded user info (in the url token). App B can then validate the request and decode the user info.

## 官网

- 主页: http://github.com/jdugarte/proxy_authentication/
- 文档: https://www.rubydoc.info/gems/proxy_authentication/0.0.4
- RubyGems: https://rubygems.org/gems/proxy_authentication

## 历史版本号

- 0.0.4 (2015-10-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/proxy_authentication
- gem 安装: `gem install proxy_authentication`
- Bundler: `gem "proxy_authentication"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/proxy_authentication-0.0.4.gem
- 版本锁定: `gem "proxy_authentication", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
