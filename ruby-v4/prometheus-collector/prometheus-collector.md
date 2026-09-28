# prometheus-collector

**Tag**: web, cli, filesystem, data

## 简介

Application to gather prometheus style metrics

# Usage

Install  the gem into your gemfile

```gem prometheus-collector```

Install your gemset

```bundle install```

Consume the program.


```
require 'prometheus/collector'

class Guage < Prometheus::Collector::Extensions::Base
  install

  def run
    # Do some things that would be collected in Prometheus::Client Objects
  end
end
```

Mount the Prometheus::Collector::Application application, or start it from your app.rb

```
Prometheus::Collector::Application.start
```

# How it works

The collector app makes use of the Prometheus client collector and exporter middleware to allow you to write custom applications that export prometheus style metrics.

It is designed as a bare-bones scaffold to get you off the ground with a ruby applet to get some statistics.

It utilizes rack and its middleware.

The interface is fairly straightforward: Your Metric Executing code needs to extend Prometheus::Collector::Extensions::Base for 'repeatedly-runbable' operations and Prometheus::Collector::Extensions::Once for something that should only be executed Once.

Your class should implement an instance level `run` function, and may optionally implement a class level `schedule` function: This must return a `cron` style string to tell the application when to invoke your `run` code. By default, `schedule` is set to `* * * * *` which would allow the code to be executed every minute.

### Scheduling
Scheduling is implemented via em-cron. Thus the re-scheduling of a task should occur within the parameters of the `schedule` string but is evaluated upon completion. Thus in normal operation, the code should not execute more than one `run` of a given worker definition at a time.

## 官网

- 主页: https://github.com/essjayhch/prometheus-collector
- 文档: https://www.rubydoc.info/gems/prometheus-collector/0.0.1
- RubyGems: https://rubygems.org/gems/prometheus-collector

## 历史版本号

- 0.0.1 (2021-12-30)

## 获取地址

- RubyGems: https://rubygems.org/gems/prometheus-collector
- gem 安装: `gem install prometheus-collector`
- Bundler: `gem "prometheus-collector"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/prometheus-collector-0.0.1.gem
- 版本锁定: `gem "prometheus-collector", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
