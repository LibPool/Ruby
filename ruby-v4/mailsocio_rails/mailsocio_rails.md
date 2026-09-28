# mailsocio_rails

**Tag**: web

## 简介

# Mailsocio Rails

Плагин к ActionMailer для использования mailsocio для отправки электронной почты.

## Установка

Строчка в Гемфайл:

```ruby
gem 'mailsocio_rails'
```

Ну и выполните `bundle`.

## Использование

Сконфигурируйте ActionMailer вот так:

```ruby
# config/application.rb

config.action_mailer.delivery_method = :mailsocio
config.action_mailer.mailsocio_settings = {
  account_id: '&lt;your account id&gt;',
  api_key: '&lt;your account api key&gt;'
}
```

Готово!

## 官网

- 主页: http://app.mailarbor.com
- 文档: https://www.rubydoc.info/gems/mailsocio_rails/0.0.5
- RubyGems: https://rubygems.org/gems/mailsocio_rails

## 历史版本号

- 0.0.5 (2015-05-06)
- 0.0.4 (2015-04-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/mailsocio_rails
- gem 安装: `gem install mailsocio_rails`
- Bundler: `gem "mailsocio_rails"`
- 最新版本: 0.0.5
- 最新版归档: https://rubygems.org/downloads/mailsocio_rails-0.0.5.gem
- 版本锁定: `gem "mailsocio_rails", "~> 0.0.5"`
- 中央仓库: https://rubygems.org/
