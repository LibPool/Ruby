# holepunch

**Tag**: web, database, testing, security, networking, tooling, devops, filesystem, data

## 简介

# holepunch
[![Gem Version](https://badge.fury.io/rb/holepunch.svg)](http://badge.fury.io/rb/holepunch)
[![Build Status](https://travis-ci.org/undeadlabs/holepunch.svg?branch=master)](https://travis-ci.org/undeadlabs/holepunch)

Holepunch manages AWS EC2 security groups in a declarative way through a DSL.

## Requirements

- Ruby 1.9.3 or newer.

## Installation

```bash
gem install holepunch
```

or in your Gemfile

```ruby
gem 'holepunch'
```

## Basic Configuration

You need to provide your AWS security credentials and a region. These can be
provided via the command-line options, or you can use the standard AWS
environment variables:

```bash
export AWS_ACCESS_KEY_ID='...'
export AWS_SECRET_ACCESS_KEY='...'
export AWS_REGION='us-west-2'
```

## The SecurityGroups file

Specify your security groups in a `SecurityGroups` file in your project's root.
Declare security groups that you need and the ingresses you want to expose. You
can add ingresses using `tcp`, `udp`, and `ping`. For each ingress you can list
allowed hosts using group names or CIDR notation.

```ruby
group 'web' do
  desc 'Web servers'

  tcp 80
end

group 'db' do
  desc 'database servers'

  tcp 5432, 'web'
end

group 'log' do
  desc 'log server'

  tcp 9999, 'web', 'db', '10.1.0.0/16'
end
```

An environment can be specified which is available through the `env` variable.
This allows you to have custom security groups per server environment.

```ruby
group "#{env}-web"
group "#{env}-db" do
  tcp 5432, "#{env}-web"
end
```

Your application may depend on security groups defined by other services. Ensure
they exist using the `depends` method.

```ruby
depends 'my-other-service'
group 'my-service' do
  udp 9999, 'my-other-service'
end
```

You may specify port ranges for `tcp` and `udp` using the range operator.

```ruby
group 'my-service' do
  udp 5000..9999, '0.0.0.0/0'
end
```

You can specify ping/icmp rules with `icmp` (alias: `ping`).

```ruby
group 'my-service' do
  ping '10.0.0.0/16'
end
```

It can be useful to describe groups of security groups you plan to launch
instances with by using the `service` declaration.

```ruby
service "#{env}-web" do
  groups %W(
    admin
    #{env}-log-producer
    #{env}-web
  )
end
```

## Usage

Simply navigate to the directory containing your `SecurityGroups` file and run `holepunch`.

```
$ holepunch
```

If you need to specify an environment:

```
$ holepunch -e live
```

You can get a list of security groups for a service using the `service` subcommand.

```
$ holepunch service -e prod prod-web
admin,prod-log-producer,prod-web
```

You can also get a list of all defined services.

```
$ holepunch service --list
```

## Testing

You can run the unit tests by simply running rspec.

```
$ rspec
```

By default the integration tests with EC2 are not run. You may run them with:

```
$ rspec -t integration
```

## Authors

- Ben Scott (gamepoet@gmail.com)
- Pat Wyatt (pat@codeofhonor.com)

## License

Copyright 2014 Undead Labs, LLC.

Licensed under the MIT License: http://opensource.org/licenses/MIT

## 官网

- 主页: https://github.com/undeadlabs/holepunch
- 文档: https://www.rubydoc.info/gems/holepunch/1.3.0
- RubyGems: https://rubygems.org/gems/holepunch

## 历史版本号

- 1.3.0 (2015-01-27)
- 1.2.0 (2014-07-08)
- 1.1.0 (2014-07-01)
- 1.0.1 (2014-06-16)
- 1.0.0 (2014-06-13)

## 获取地址

- RubyGems: https://rubygems.org/gems/holepunch
- gem 安装: `gem install holepunch`
- Bundler: `gem "holepunch"`
- 最新版本: 1.3.0
- 最新版归档: https://rubygems.org/downloads/holepunch-1.3.0.gem
- 版本锁定: `gem "holepunch", "~> 1.3.0"`
- 中央仓库: https://rubygems.org/
