# better-initialize

**Tag**: testing, tooling, filesystem

## 简介

# better-initialize

A friendlier, dependency-free initialize method for ruby objects.

## Usage

Gemfile:

    gem 'better-initialize',
      github: 'huned/better-initialize'

Code:

    require 'better_initialize'

    class Pizza
      include BetterInitialize
      attr_accessor :size, :toppings
    end

    # Instantiate with attributes.
    Pizza.new(size: :large, toppings: %i[mushrooms peppers])

    # Instantiate with attributes and a block.
    Pizza.new(size: :large) do |pizza|
      pizza.toppings = %w[mushrooms peppers]
      Oven.bake!(pizza)
    end

## Development Environment (OSX)

    brew install rbenv ruby-build
    git clone git@github.com:huned/better-initialize
    rbenv install -k `cat .ruby-version`
    bundle exec ruby test/run.rb

## 官网

- 主页: https://github.com/huned/better-initialize
- 文档: https://www.rubydoc.info/gems/better-initialize/0.0.1
- RubyGems: https://rubygems.org/gems/better-initialize

## 历史版本号

- 0.0.1 (2015-03-08)

## 获取地址

- RubyGems: https://rubygems.org/gems/better-initialize
- gem 安装: `gem install better-initialize`
- Bundler: `gem "better-initialize"`
- 最新版本: 0.0.1
- 最新版归档: https://rubygems.org/downloads/better-initialize-0.0.1.gem
- 版本锁定: `gem "better-initialize", "~> 0.0.1"`
- 中央仓库: https://rubygems.org/
