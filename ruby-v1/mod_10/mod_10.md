# mod_10

**Tag**: web, testing, networking, filesystem

## 简介

# Mod10

A simple gem to generate mod_10 check digits and check if integers are mod10
valid.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'mod_10'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install mod_10

## Usage

Include the Mod10 module to make the following two methods available
  - generate_check_digit(value)
    Which returns an integer value for the mod10 check digit of a string or integer.
    Note: If the value is 0, then the argument was already mod10 valid.

  - is_mod10?(value)
    Returns true or false for the tested value is it is or isn't mod10 valid.

## Contributing

1. Fork it ( https://github.com/[my-github-username]/mod_10/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## 官网

- 主页: https://github.com/kryptykfysh/mod_10
- 文档: https://www.rubydoc.info/gems/mod_10/0.0.3
- RubyGems: https://rubygems.org/gems/mod_10

## 历史版本号

- 0.0.3 (2014-10-27)

## 获取地址

- RubyGems: https://rubygems.org/gems/mod_10
- gem 安装: `gem install mod_10`
- Bundler: `gem "mod_10"`
- 最新版本: 0.0.3
- 最新版归档: https://rubygems.org/downloads/mod_10-0.0.3.gem
- 版本锁定: `gem "mod_10", "~> 0.0.3"`
- 中央仓库: https://rubygems.org/
