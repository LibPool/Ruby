# mail-store-agent

**Tag**: testing

## 简介

require 'mail'
    require 'mail-store-agent'

    Mail.defaults do
      delivery_method :test
    end

    Mail::TestMailer.deliveries = MailStoreAgent.new

    # send some mail to someone@someplace.com, and then ...

    Mail::TestMailer.deliveries.get('someone@someplace.com').is_a? Mail::Message # or nil

## 官网

- 主页: http://github.com/lsiden/mail-store-agent/
- RubyGems: https://rubygems.org/gems/mail-store-agent

## 历史版本号

- 0.1.1 (2011-12-28)
- 0.1.0 (2011-12-21)

## 获取地址

- RubyGems: https://rubygems.org/gems/mail-store-agent
- gem 安装: `gem install mail-store-agent`
- Bundler: `gem "mail-store-agent"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/mail-store-agent-0.1.1.gem
- 版本锁定: `gem "mail-store-agent", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
