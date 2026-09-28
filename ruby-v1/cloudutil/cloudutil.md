# cloudutil

**Tag**: web, security, networking, devops, filesystem

## 简介

# Cloudutil

A utility library for performing helpful tasks with various cloud platform providers

## Installation

Add this line to your application's Gemfile:

    gem 'cloudutil'

And then execute:

    $ bundle install

Or install it yourself as:

    $ gem install cloudutil

## Usage

For AWS helpers:

    require 'cloudutil/aws'

    aws = Cloudutil::AWS(config: existing_AWS::Config_object) -or-
    aws = Cloudutil::AWS(access_key: your_AWS_access_key, secret_key: your_AWS_secret_key)

    subnet_id  = aws.resolve_subnet_id('my_subnet_name_or_tag')
    sec_grp_id = aws.resolve_subnet_id('my_security_group_name_or_tag')
    ami_id = aws.resolve_subnet_id('my_ami_name_or_tag')

## Contributing

1. Fork it ( https://github.com/mmmorris1975/cloudutil/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## 官网

- 文档: https://www.rubydoc.info/gems/cloudutil/0.2.0
- RubyGems: https://rubygems.org/gems/cloudutil

## 历史版本号

- 0.2.0 (2015-07-06)
- 0.1.0 (2015-01-15)
- 0.0.1 (2014-11-19)

## 获取地址

- RubyGems: https://rubygems.org/gems/cloudutil
- gem 安装: `gem install cloudutil`
- Bundler: `gem "cloudutil"`
- 最新版本: 0.2.0
- 最新版归档: https://rubygems.org/downloads/cloudutil-0.2.0.gem
- 版本锁定: `gem "cloudutil", "~> 0.2.0"`
- 中央仓库: https://rubygems.org/
