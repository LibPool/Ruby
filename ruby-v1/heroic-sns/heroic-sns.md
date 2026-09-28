# heroic-sns

**Tag**: web, testing, devops

## 简介

Secure, lightweight Rack middleware for Amazon Simple Notification Service (SNS)
endpoints. SNS messages are intercepted, parsed, verified, and then passed along
to the web application via the 'sns.message' environment key. Heroic::SNS has no
dependencies besides Rack (specifically, the aws-sdk gem is not needed).
SNS message signatures are verified in order to reject forgeries and replay
attacks.

## 官网

- 主页: https://github.com/benzado/heroic-sns
- 文档: https://www.rubydoc.info/gems/heroic-sns/1.2
- RubyGems: https://rubygems.org/gems/heroic-sns

## 历史版本号

- 1.2 (2020-06-15)
- 1.1.3 (2016-07-13)
- 1.1.2 (2016-03-24)
- 1.1.1 (2013-08-09)
- 1.1.0 (2013-06-25)
- 1.0.1 (2013-05-17)
- 1.0.0 (2013-05-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/heroic-sns
- gem 安装: `gem install heroic-sns`
- Bundler: `gem "heroic-sns"`
- 最新版本: 1.2
- 最新版归档: https://rubygems.org/downloads/heroic-sns-1.2.gem
- 版本锁定: `gem "heroic-sns", "~> 1.2"`
- 中央仓库: https://rubygems.org/
