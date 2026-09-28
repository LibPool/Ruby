# rack-cors-csrf_prevention

**Tag**: web, testing, serialization, networking, filesystem

## 简介

The middleware makes sure any request to specified paths would have been
preflighted if it was sent by a browser.

We don't want random websites to be able to execute actual GraphQL
operations from a user's browser unless our CORS policy supports it. It's
not good enough just to ensure that the browser can't read the response from
the operation; we also want to prevent CSRF, where the attacker can cause
side effects with an operation or can measure the timing of a read
operation. Our goal is to ensure that we don't run the context function or
execute the GraphQL operation until the browser has evaluated the CORS
policy, which means we want all operations to be pre-flighted. We can do
that by only processing operations that have at least one header set that
appears to be manually set by the JS code rather than by the browser
automatically.

POST requests generally have a content-type `application/json`, which is
sufficient to trigger preflighting. So we take extra care with requests that
specify no content-type or that specify one of the three non-preflighted
content types. For those operations, we require one of a set of specific
headers to be set. By ensuring that every operation either has a custom
content-type or sets one of these headers, we know we won't execute
operations at the request of origins who our CORS policy will block.

## 官网

- 主页: https://github.com/digitaz/rack-cors-csrf_prevention
- RubyGems: https://rubygems.org/gems/rack-cors-csrf_prevention

## 历史版本号

- 0.3.0 (2025-11-24)
- 0.2.1 (2024-02-15)
- 0.2.0 (2024-02-15)
- 0.1.0 (2024-02-15)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-cors-csrf_prevention
- gem 安装: `gem install rack-cors-csrf_prevention`
- Bundler: `gem "rack-cors-csrf_prevention"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/rack-cors-csrf_prevention-0.3.0.gem
- 版本锁定: `gem "rack-cors-csrf_prevention", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
