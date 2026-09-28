# rails_cookie_overflow

**Tag**: web, networking, data

## 简介

Rails raises a CookieOverflow exception when the total size of the incoming request's                       cookie crosses a certain threshold - currently set as 4096 bytes. While it is not                       advisable to store or pass around such large data in cookies, sometimes, bad actors                       can try to send large cookie payloads to your application to see if your systems are                       able to handle it. If not handled, your application would end up raising a large number                       of 500 exceptions. This gem handles the exception gracefully and responds with a                       422 Unprocessable Entity HTTP status code.

## 官网

- 主页: https://github.com/ritikesh/rails_cookie_overflow
- 更新日志: https://github.com/ritikesh/rails_cookie_overflow/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/rails_cookie_overflow

## 历史版本号

- 1.0.1 (2022-11-24)
- 1.0.0 (2022-07-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/rails_cookie_overflow
- gem 安装: `gem install rails_cookie_overflow`
- Bundler: `gem "rails_cookie_overflow"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/rails_cookie_overflow-1.0.1.gem
- 版本锁定: `gem "rails_cookie_overflow", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
