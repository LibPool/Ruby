# margot

**Tag**: template, data

## 简介

== FEATURES/PROBLEMS:  * The query string, and POST/PUT parameters are available through the +params+ hash * Other request data can be attained through the +request+ method * The Markaby instance is called +mab+ (But you do not need to call it directly.  The +html+ method is an alias to +mab.html+) * Margot keeps an in memory cache of pages and their parameters! * To clear the cache and garbage collect, just send a USR1 signal to the process * The mongrel status information is mounted by default at /status * A directory handler is loaded at /assets to the directory +./assets+ * There is daemonization support but it is borked at the moment * Template and layout handling  == REQUIREMENTS:  Margot requires the following gems * Markaby * Mongrel  == INSTALL:  sudo gem install margot

## 官网

- 主页: http://metacampsite.com/margot/
- RubyGems: https://rubygems.org/gems/margot

## 历史版本号

- 0.5.0 (2009-07-25)

## 获取地址

- RubyGems: https://rubygems.org/gems/margot
- gem 安装: `gem install margot`
- Bundler: `gem "margot"`
- 最新版本: 0.5.0
- 最新版归档: https://rubygems.org/downloads/margot-0.5.0.gem
- 版本锁定: `gem "margot", "~> 0.5.0"`
- 中央仓库: https://rubygems.org/
