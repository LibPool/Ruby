# app-ctx

**Tag**: cli, serialization, filesystem

## 简介

For all applications (you are not a mouseclicker, are u?), once in a while you need to supply some configuration values to overrule the built-in defaults. The app-ctx gem does unify and organize built-in constants, config files and commandline option with a clearly defined priority, from low to high:  - procedural: set from your implementation App::Config#set_default_values - YAML default values file loaded from next to the $0 script - user supplied configuration file, eg.: --config=/tmp/foo.yml - command line options and flags: --foo --bar=foo  But for your application it is of no interesst from where the values are coming: command line option: &quot;--port=1234&quot;, a user configuration file or from the applications built-in default values. Therefor +app-ctx+ combines value settings from various sources into a single configuration hash.

## 官网

- 文档: https://www.rubydoc.info/gems/app-ctx/0.1.6
- RubyGems: https://rubygems.org/gems/app-ctx

## 历史版本号

- 0.1.6 (2009-07-25)
- 0.1.4 (2009-07-25)
- 0.1.3 (2009-07-25)
- 0.1.2 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/app-ctx
- gem 安装: `gem install app-ctx`
- Bundler: `gem "app-ctx"`
- 最新版本: 0.1.6
- 最新版归档: https://rubygems.org/downloads/app-ctx-0.1.6.gem
- 版本锁定: `gem "app-ctx", "~> 0.1.6"`
- 中央仓库: https://rubygems.org/
