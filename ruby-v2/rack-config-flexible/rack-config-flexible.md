# rack-config-flexible

**Tag**: web, serialization, filesystem

## 简介

Rack::Config::Flexible is an alternative to Rack::Config,
  offering much greater flexibility.
  
  Configuration options are stored as key-value pairs in _sections_,
  partitioned by _environments_. For example:
  
    + environment
      + section
        key -> value pairs
  
  A simple DSL is provided and can be used either within a passed
  configuration block (to ::new), or to the #configuration method.
  
  Facilities are also provided to load whole environments, and sections
  from either a single YAML file structured like, or from a directory tree.

  See the README file or RDoc documentation for more info.

## 官网

- 主页: https://github.com/thentenaar/rack-config-flexible
- RubyGems: https://rubygems.org/gems/rack-config-flexible

## 历史版本号

- 0.1.4 (2012-11-19)
- 0.1.3 (2012-11-19)
- 0.1.2 (2012-11-19)
- 0.1.1 (2012-11-17)
- 0.1.0 (2012-11-17)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-config-flexible
- gem 安装: `gem install rack-config-flexible`
- Bundler: `gem "rack-config-flexible"`
- 最新版本: 0.1.4
- 最新版归档: https://rubygems.org/downloads/rack-config-flexible-0.1.4.gem
- 版本锁定: `gem "rack-config-flexible", "~> 0.1.4"`
- 中央仓库: https://rubygems.org/
