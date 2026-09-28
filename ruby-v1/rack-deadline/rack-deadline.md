# rack-deadline

**Tag**: web, security

## 简介

rack-deadline is a simple rack middleware that automatically
clears sessions that have been open too long (by default,
1 day).

This is designed for use with cookie stores to mitigate the
risk of session fixation, since it is impossible to invalidate
older sessions with a pure cookie-based approach.

It is impossible to enforce a deadline with the standard rack
cookie session API. The expire_after setting is not part of the
session itself (it's part of the cookie, and not cryptographically
signed), and an attacker who has access to a previous cookie can
just omit it when making a request.

This stores a deadline inside the crytographically signed session,
and once the deadline is passed, the session will no longer be valid.

## 官网

- 主页: http://github.com/jeremyevans/rack-deadline
- 文档: https://www.rubydoc.info/gems/rack-deadline/1.0.1
- RubyGems: https://rubygems.org/gems/rack-deadline

## 历史版本号

- 1.0.1 (2015-01-27)
- 1.0.0 (2014-01-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-deadline
- gem 安装: `gem install rack-deadline`
- Bundler: `gem "rack-deadline"`
- 最新版本: 1.0.1
- 最新版归档: https://rubygems.org/downloads/rack-deadline-1.0.1.gem
- 版本锁定: `gem "rack-deadline", "~> 1.0.1"`
- 中央仓库: https://rubygems.org/
