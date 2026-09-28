# action_mailer_auto_previews

**Tag**: web, testing, template, data

## 简介

Enhances the ActionMailer Previews introduced in 4.1 by automatically creating ActionMailer Previews at runtime in development mode.
    See automatic previews of your ActionMailer emails, with no extra effort or mock data. Install the action_mailer_auto_previews gem
    into your :development group, and it'll 'just work' with sensible defaults. Each ActionMailer email object that has .deliver or
    .deliver_later called will automatically launch your default browser right to a ActionMailer Preview page with the real data
    passed to that email. Flexible options allow you to alter this behavior as well.

    Warning: Since this is dynamically creating Ruby classes/methods, you will want to make sure your web-server is single threaded.
    For example, if you're using Puma, be sure to set the `workers` configuration parameter to 1.

## 官网

- 主页: https://github.com/makifund/action_mailer_auto_previews
- 文档: https://www.rubydoc.info/gems/action_mailer_auto_previews/0.1.0
- RubyGems: https://rubygems.org/gems/action_mailer_auto_previews

## 历史版本号

- 0.1.0 (2016-04-28)

## 获取地址

- RubyGems: https://rubygems.org/gems/action_mailer_auto_previews
- gem 安装: `gem install action_mailer_auto_previews`
- Bundler: `gem "action_mailer_auto_previews"`
- 最新版本: 0.1.0
- 最新版归档: https://rubygems.org/downloads/action_mailer_auto_previews-0.1.0.gem
- 版本锁定: `gem "action_mailer_auto_previews", "~> 0.1.0"`
- 中央仓库: https://rubygems.org/
