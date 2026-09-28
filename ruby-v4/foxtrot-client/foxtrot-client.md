# foxtrot-client

**Tag**: web, cli, networking, filesystem, data

## 简介

# Foxtrot Ruby Client Library

This is the Ruby client library for interacting with the Foxtrot API. The only endpoint currently exposed is the route optimization endpoint (`Foxtrot::Client.optimize!`).

In order to make requests, you need a valid API key. Your API key can be found at the bottom of any page in the [Foxtrot web app](http://app.foxtrot.io/).

## Installation

`gem install foxtrot-client`

## Usage

```ruby
data = {
  file_url: "https://www.domain.io/your_file.xlsx",
  file_name: "your_file.xlsx",
  geocode: "false",
  stop_name: "Customer",
  lat: "Lat",
  lng: "Long",
  load: "Load",
  service_time: "Service Time",
  time_window: "Time Window",
  extra_info: "Contact Info",
  date_starting: "1407712069593",
  warehouse: "77 Massachusetts Ave, Cambridge MA",
  num_drivers: 1,
  num_avg_service_time: 10,
  float_fuel_cost: 3.56,
  float_driver_wage: 6.01,
  float_mpg: 8.32
}

api_key = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

require 'foxtrot'
fox = Foxtrot::Client.new api_key

resp = fox.optimize!(data).poll_and_block!
result = resp.get_result
```

## 官网

- 主页: https://github.com/FoxtrotSystems/api-client-ruby
- 文档: https://www.rubydoc.info/gems/foxtrot-client/0.0.4
- RubyGems: https://rubygems.org/gems/foxtrot-client

## 历史版本号

- 0.0.4 (2014-12-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/foxtrot-client
- gem 安装: `gem install foxtrot-client`
- Bundler: `gem "foxtrot-client"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/foxtrot-client-0.0.4.gem
- 版本锁定: `gem "foxtrot-client", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
