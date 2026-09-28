# kaffe

**Tag**: web, template

## 简介

# Kaffe Framework
This is a minimalistic webframework inspired by sinatra and 
rails.

## Basic usage
The idea is to use be able to create modular applications and
forward requests between them.

        class Blog &lt; Kaffe::Base
          use Rack::CommonLogger

          get '/?' do
            "Hello From Blog"            
          end
        end

        class Admin &lt; Kaffe::Base
          get '/login' do
            ... Login logics ...
          end

          error 400..500 do |code, message|
            .. show pretty error message ..
          end
        end

        class MyApp &lt; Kaffe::Base
          route '/blog', Blog
          route '/admin', Admin
        end

        run MyApp

## API overview

## 官网

- 主页: https://github.com/kaffepanna/kaffe
- 文档: https://www.rubydoc.info/gems/kaffe/0.0.4
- RubyGems: https://rubygems.org/gems/kaffe

## 历史版本号

- 0.0.4 (2017-03-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/kaffe
- gem 安装: `gem install kaffe`
- Bundler: `gem "kaffe"`
- 最新版本: 0.0.4
- 最新版归档: https://rubygems.org/downloads/kaffe-0.0.4.gem
- 版本锁定: `gem "kaffe", "~> 0.0.4"`
- 中央仓库: https://rubygems.org/
