# warden_openid_bearer

**Tag**: web, cli, security

## 简介

This gem is like the `warden_openid_auth` gem, except that it only
provides support for the very last step of the OAuth code flow, i.e.
when the resource server / relying party (your Ruby Web app)
validates the bearer token.

Use this gem if your client-side Web (or mobile) app will be taking
care of the rest of the OAuth2 motions, such as redirecting (or
opening a popup window) to the authentication server at login time,
managing and refreshing tokens, doing all these unspeakable things
with iframes, etc.

## 官网

- 主页: https://github.com/epfl-si/warden_openid_bearer
- 更新日志: https://github.com/epfl-si/warden_openid_bearer/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/warden_openid_bearer

## 历史版本号

- 0.2.2 (2023-11-02)
- 0.2.1 (2023-11-02)
- 0.2.0 (2023-11-02)
- 0.1.4 (2022-10-11)
- 0.1.3 (2022-10-07)
- 0.1.2 (2022-10-07)
- 0.1.1 (2022-10-07)
- 0.1.0 (2022-10-07)

## 获取地址

- RubyGems: https://rubygems.org/gems/warden_openid_bearer
- gem 安装: `gem install warden_openid_bearer`
- Bundler: `gem "warden_openid_bearer"`
- 最新版本: 0.2.2
- 最新版归档: https://rubygems.org/downloads/warden_openid_bearer-0.2.2.gem
- 版本锁定: `gem "warden_openid_bearer", "~> 0.2.2"`
- 中央仓库: https://rubygems.org/
