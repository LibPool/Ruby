# config_accessor

**Tag**: library

## 简介

== Synopsys
Class-level configuration DSL

== Installation
  gem install config_accessor

== Examples
  require 'config_accessor'

  class Remote
    configurable!

    config_accessor :host, :default => "localhost"
    config_accessor :port, :default => "80", :transform => :to_i
    config_accessor :proxy_host, :proxy_port
  end

  class Local < Remote
    config_accessor :l_port
  end

  Remote.host        # => "localhost"
  Remote.port        # => 80
  Remote.proxy_host  # => nil

  r = Remote.new

  r.port = "81"
  r.port             # => 81
  Remote.port        # => 80
  Remote.port = 82

  # next expressions are equivalent
  r.port             # => 81
  r.config[:port]    # => 81
  r.config["port"]   # => 81
  r.config.port      # => 81

  # It supports inheritance, subclasses cannot change superclasses configurations
  Local.port         # => 80

  # You can do it with +configure+ method
  Local.configure do
    port 81
  end

  # or
  Local.configure do |config|
    config.port 81
  end

## 官网

- 主页: https://github.com/take-five/config_accessor
- RubyGems: https://rubygems.org/gems/config_accessor

## 历史版本号

- 0.0.3 (2011-12-10)
- 0.0.2 (2011-12-10)

## 获取地址

- RubyGems: https://rubygems.org/gems/config_accessor
- gem 安装: `gem install config_accessor`
- Bundler: `gem "config_accessor"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/config_accessor-0.0.3.gem
- 版本锁定: `gem "config_accessor", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
