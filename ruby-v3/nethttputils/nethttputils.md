# nethttputils

**Tag**: web, security, networking, filesystem

## 简介

Back in 2015 I was a guy automating things at my job and two scripts had a common need --
    they both had to pass the same credentials to Jenkins (via query params, I guess).

    That common tool with a single method was a Net::HTTP wrapper -- that's where the name from.
    Then when the third script appeared two of them had to pass the Basic Auth.
    The verb POST was added and common logging format, and relatively complex retry logic.
    Then some website had redirects and I had to store cookies, then GZIP and API rate limits...

    I was not going to gemify this monster but it is now a dependency in many other gems,
    and since Gemfile does not support Github dependencies I have to finally gemify it.

## 官网

- 主页: https://github.com/nakilon/nethttputils
- 文档: https://www.rubydoc.info/gems/nethttputils/0.4.5.0
- RubyGems: https://rubygems.org/gems/nethttputils

## 历史版本号

- 0.4.5.0 (2023-11-13)
- 0.4.4.0 (2023-05-14)
- 0.4.3.2 (2022-02-02)
- 0.4.3.0 (2021-10-16)
- 0.4.2.0 (2021-10-05)
- 0.4.1.3 (2021-06-28)
- 0.4.1.2 (2021-06-28)
- 0.4.1.1 (2020-12-07)
- 0.4.1.0 (2020-08-23)
- 0.4.0.0 (2020-01-04)
- 0.3.3.0 (2019-11-08)
- 0.3.2.11 (2019-06-08)
- 0.3.2.10 (2019-05-18)
- 0.3.2.9 (2019-05-18)
- 0.3.2.8 (2019-05-18)
- 0.3.2.7 (2019-05-18)
- 0.3.2.6 (2019-02-24)
- 0.3.2.5 (2019-02-03)
- 0.3.2.4 (2019-02-02)
- 0.3.2.3 (2019-01-20)
- 0.3.2.2 (2019-01-20)
- 0.3.2.1 (2019-01-14)
- 0.3.2.0 (2019-01-11)
- 0.3.1.0 (2018-12-30)
- 0.3.0.0 (2018-12-30)
- 0.2.5.1 (2018-11-05)
- 0.2.5.0 (2018-10-24)
- 0.2.4.2 (2018-06-29)
- 0.2.4.1 (2018-06-14)
- 0.2.4.0 (2018-05-23)
- 0.2.3.0 (2018-05-17)
- 0.2.2.0 (2018-05-07)
- 0.2.1.1 (2018-05-07)
- 0.2.0.0 (2018-05-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/nethttputils
- gem 安装: `gem install nethttputils`
- Bundler: `gem "nethttputils"`
- 最新版本: 0.4.5.0
- 最新版归档: https://rubygems.org/downloads/nethttputils-0.4.5.0.gem
- 版本锁定: `gem "nethttputils", "~> 0.4.5.0"`
- 中央仓库: https://rubygems.org/
