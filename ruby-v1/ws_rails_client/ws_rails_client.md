# ws_rails_client

**Tag**: web, cli, networking

## 简介

# ws-rails-client

Simple Ruby client to for Websocket Rails server.

Example:

```ruby
require 'ws_rails_client'
require 'eventmachine'

EM.run do
  client = WsRails::Client.new("ws://localhost:3000/websocket")

  client.handle 'my_event' do |message|
    client.send('my_response', message)
  end
end
```

## 官网

- 主页: https://github.com/dena-techstudig-2014/ws-rails-client
- 文档: https://www.rubydoc.info/gems/ws_rails_client/0.1.1
- RubyGems: https://rubygems.org/gems/ws_rails_client

## 历史版本号

- 0.1.1 (2014-09-16)
- 0.1.0 (2014-09-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/ws_rails_client
- gem 安装: `gem install ws_rails_client`
- Bundler: `gem "ws_rails_client"`
- 最新版本: 0.1.1
- 最新版归档: https://rubygems.org/downloads/ws_rails_client-0.1.1.gem
- 版本锁定: `gem "ws_rails_client", "~> 0.1.1"`
- 中央仓库: https://rubygems.org/
