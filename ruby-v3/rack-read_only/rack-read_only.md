# rack-read_only

**Tag**: web, testing, networking, tooling, filesystem

## 简介

# Rack::ReadOnly

This gem allows Rack based APIs to be set to read only. At the most basic
it can be used like this from your `config.ru`:

```ruby
require 'rack/read_only'

use Rack::ReadOnly, {
  active: ENV["READ_ONLY"] == "1",
  response_body: '{ "error": "This API is currently in read only mode." }'
}
run MyApp
```

When in read only mode the API will continue to respond to GET, HEAD, and
OPTIONS requests as normal, but reject POST, PUT, DELETE, and PATCH requests
with the body specified, and a 503 error code.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'rack-read_only'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install rack-read_only

## Development

After checking out the repo, run `bin/setup` to install dependencies.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release` to create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

1. Fork it ( https://github.com/jellybob/rack-read_only/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

Any new builds should pass the tests on [Travis](https://travis-ci.org/jellybob/rack-read_only)

## 官网

- 主页: https://github.com/jellybob/rack-read_only
- 文档: https://www.rubydoc.info/gems/rack-read_only/2.0.0
- RubyGems: https://rubygems.org/gems/rack-read_only

## 历史版本号

- 2.0.0 (2019-09-24)
- 1.0.1 (2015-05-16)
- 1.0.0 (2015-05-16)

## 获取地址

- RubyGems: https://rubygems.org/gems/rack-read_only
- gem 安装: `gem install rack-read_only`
- Bundler: `gem "rack-read_only"`
- 最新版本: 2.0.0
- 最新版归档: https://rubygems.org/downloads/rack-read_only-2.0.0.gem
- 版本锁定: `gem "rack-read_only", "~> 2.0.0"`
- 中央仓库: https://rubygems.org/
