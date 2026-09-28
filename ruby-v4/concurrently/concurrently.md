# concurrently

**Tag**: library

## 简介

Concurrently is a concurrency framework for Ruby and mruby based on
fibers. With it code can be evaluated independently in its own execution
context similar to a thread:

    hello = concurrently do
      wait 0.2 # seconds
      "hello"
    end
    
    world = concurrently do
      wait 0.1 # seconds
      "world"
    end
    
    puts "#{hello.await_result} #{world.await_result}"

## 官网

- 主页: https://github.com/christopheraue/m-ruby-concurrently
- 文档: https://www.rubydoc.info/gems/concurrently/1.2.0
- RubyGems: https://rubygems.org/gems/concurrently

## 历史版本号

- 1.2.0 (2017-12-12)
- 1.1.1 (2017-07-15)
- 1.1.0 (2017-07-10)
- 1.0.1 (2017-06-26)

## 获取地址

- RubyGems: https://rubygems.org/gems/concurrently
- gem 安装: `gem install concurrently`
- Bundler: `gem "concurrently"`
- 最新版本: 1.2.0
- 最新版归档: https://rubygems.org/downloads/concurrently-1.2.0.gem
- 版本锁定: `gem "concurrently", "~> 1.2.0"`
- 中央仓库: https://rubygems.org/
