# mail_provider

**Tag**: testing, data

## 简介

Smartly check whether a given email/domain belongs to a free or disposable
  mail provider. There are hundreds of lists available in Github repositories
  or Gists that list various free and disposable email providers. This gem
  downloads a bunch of these scripts (pre-configured URLs) and parses them to
  count votes against each domain in the list. We, then, create a Trie
  structure to efficiently query this data with a given domain or email. For
  each query, you get back a number specifying how many sources are claiming
  that the domain is a free or disposable email provider.

## 官网

- 主页: https://github.com/nikhgupta/mail_provider
- 文档: https://www.rubydoc.info/gems/mail_provider/0.1.0
- RubyGems: https://rubygems.org/gems/mail_provider

## 历史版本号

- 0.1.0 (2020-03-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/mail_provider
- gem 安装: `gem install mail_provider`
- Bundler: `gem "mail_provider"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/mail_provider-0.1.0.gem
- 版本锁定: `gem "mail_provider", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
