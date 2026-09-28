# check_tcp_memory

**Tag**: web, cli, testing, networking, filesystem

## 简介

# CheckTCPMemory

This is a simple Nagios/Sensu check that checks that the current TCP memory usage is below the maximum allowed in the Linux kernel.  This will find leaking TCP sockets.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'check_tcp_memory'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install check_tcp_memory

## Usage

```
$ check_tcp_memory -h
Usage: check_tcp_memory -w &lt;warn percent&gt; -c &lt;critical percent&gt;
    -w, --warn-percent PERCENT       Warning when percentage of total TCP memory is over this threashold. Default: 50%
    -c, --crit-percent PERCENT       Critical when percentage of total TCP memory is over this threashold. Default: 60%
    -h, --help                       Show this message
        --version                    Show version
```

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake spec` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/Altiscale/check_tcp_memory. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](contributor-covenant.org) code of conduct.

## 官网

- 主页: https://github.com/Altiscale/check_tcp_memory
- 文档: https://www.rubydoc.info/gems/check_tcp_memory/1.0.2
- RubyGems: https://rubygems.org/gems/check_tcp_memory

## 历史版本号

- 1.0.2 (2016-06-21)
- 1.0.1 (2016-06-14)
- 1.0.0 (2016-06-14)

## 获取地址

- RubyGems: https://rubygems.org/gems/check_tcp_memory
- gem 安装: `gem install check_tcp_memory`
- Bundler: `gem "check_tcp_memory"`
- 最新版本: 1.0.2
- 最新版归档: https://rubygems.org/downloads/check_tcp_memory-1.0.2.gem
- 版本锁定: `gem "check_tcp_memory", "~> 1.0.2"`
- 中央仓库: https://rubygems.org/
