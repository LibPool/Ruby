# rjb-loader

**Tag**: web, filesystem

## 简介

When working with multiple gems or several rails initializer files that use Rjb, 
                     you need to make sure that all java dependencies of each implementation 
                     gets set up before running Rjb::load. This is necessary because Rjb can be loaded only once.
                     You can use rjb-loader to change classpath and java options, by adding 'before_load' to your gem or rails initializer.
                     The 'after_load' hook can be used when your code needs an already loaded Rjb. 
                     For instance, when you need to import and use java classes.

## 官网

- 主页: https://github.com/fortesinformatica/rjb-loader
- 文档: https://www.rubydoc.info/gems/rjb-loader/0.0.2
- RubyGems: https://rubygems.org/gems/rjb-loader

## 历史版本号

- 0.0.2 (2013-08-23)
- 0.0.1 (2013-07-05)

## 获取地址

- RubyGems: https://rubygems.org/gems/rjb-loader
- gem 安装: `gem install rjb-loader`
- Bundler: `gem "rjb-loader"`
- 最新版本: 0.0.2
- 最新版归档: https://rubygems.org/downloads/rjb-loader-0.0.2.gem
- 版本锁定: `gem "rjb-loader", "~> 0.0.2"`
- 中央仓库: https://rubygems.org/
