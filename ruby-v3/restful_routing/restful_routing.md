# restful_routing

**Tag**: web, filesystem

## 简介

While developing Rails apps, it is often difficult to remember which prefixes route to which controller#action. That is why it is useful to run `rails routes` and put that output in a file for later reference. This gem does that for you.


    After installing the gem in your Rails project, it is listening for saved changes in your `config/routes.rb`. 
    Every time you make a change to routes.rb and you save it, restful_routing will look for `restful_routing.rb` in your root directory. It will update it if there or make it if not.

    `restful_routing.rb` will contain the output of `rails routes`.

## 官网

- 主页: https://github.com/casey-stinnett/restful_routing
- 文档: https://www.rubydoc.info/gems/restful_routing/1.1.4.1
- RubyGems: https://rubygems.org/gems/restful_routing

## 历史版本号

- 1.1.4.1 (2017-11-29)
- 1.1.4 (2017-11-29)
- 1.1.2 (2017-01-12)
- 1.0.3 (2017-01-10)
- 1.0.2 (2017-01-10)
- 1.0.1 (2017-01-09)
- 1.0 (2017-01-09)
- 0.1.3.4 (2017-01-09)
- 0.1.3.3 (2017-01-09)
- 0.1.3.2 (2017-01-09)
- 0.1.3.1 (2017-01-09)
- 0.1.3 (2017-01-09)
- 0.1.2 (2017-01-09)
- 0.1.1 (2017-01-09)

## 获取地址

- RubyGems: https://rubygems.org/gems/restful_routing
- gem 安装: `gem install restful_routing`
- Bundler: `gem "restful_routing"`
- 最新版本: 1.1.4.1
- 最新版归档: https://rubygems.org/downloads/restful_routing-1.1.4.1.gem
- 版本锁定: `gem "restful_routing", "~> 1.1.4.1"`
- 中央仓库: https://rubygems.org/
