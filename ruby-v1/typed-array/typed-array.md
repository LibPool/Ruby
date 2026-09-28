# typed-array

**Tag**: library

## 简介

All methods that alter the contents of an array that implements this Gem are first checked to
      ensure that the added items are of the types allowed. All methods behave exactly as their Array
      counterparts, including additional forms, block processing, etc.

      Defining a TypedArray Class:

      ```ruby
      class ThingsArray < Array
        extend TypedArray
        restrict_types Thing1, Thing2
      end

      things = ThingsArray.new
      ```

      Generating a single TypedArray
      
      ```ruby
      things = TypedArray(Thing1,Thing2).new

      These classes can be extended, and their accepted-types appended to after their initial definition.

## 官网

- 主页: http://github.com/yaauie/typed-array
- RubyGems: https://rubygems.org/gems/typed-array

## 历史版本号

- 0.1.2 (2011-08-03)
- 0.1.1 (2011-08-03)

## 获取地址

- RubyGems: https://rubygems.org/gems/typed-array
- gem 安装: `gem install typed-array`
- Bundler: `gem "typed-array"`
- 最新版本: 0.1.2
- 最新版归档: https://rubygems.org/downloads/typed-array-0.1.2.gem
- 版本锁定: `gem "typed-array", "~> 0.1.2"`
- 中央仓库: https://rubygems.org/
