# cryptophysh

**Tag**: web, cli, testing, security, networking, tooling, filesystem

## 简介

# Cryptophysh

My attempt to produce a solution to the requirements listed [here](https://github.com/krystal/code-tasks/blob/main/password-generator.md). Essentially, a library/gem you can include in to your own code to add a `::generate_password` class method on a class.

I've pushed the built gem up to RubyGems for completeness' sake.

## Installation

Install the gem and add to the application's Gemfile by executing:

    $ bundle add cryptophysh

If bundler is not being used to manage dependencies, install the gem by executing:

    $ gem install cryptophysh

## Usage

### Extending your own class

`require cryptophysh` and

Add to your class: `extend Cryptophysh`

Your class will now have access to the `::generate_password` class method.

### Using the Cryptophysh::PasswordGenerator Class

See the YARD documentation on the class itself for details.

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake spec` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and the created tag, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/[USERNAME]/cryptophysh. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [code of conduct](https://github.com/kryptykphysh/cryptophysh/blob/master/CODE_OF_CONDUCT.md).

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the Cryptophysh project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/kryptykphysh/cryptophysh/blob/master/CODE_OF_CONDUCT.md).

## 官网

- 主页: https://github.com/kryptykphysh/cryptophysh
- 源码仓库: https://github.com/kryptykphysh/cryptophysh.git
- 更新日志: https://github.com/kryptykphysh/cryptophysh/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/cryptophysh

## 历史版本号

- 1.0.0 (2024-07-11)
- 0.1.0 (2024-07-11)

## 获取地址

- RubyGems: https://rubygems.org/gems/cryptophysh
- gem 安装: `gem install cryptophysh`
- Bundler: `gem "cryptophysh"`
- 最新版本: 1.0.0
- 最新版归档: https://rubygems.org/downloads/cryptophysh-1.0.0.gem
- 版本锁定: `gem "cryptophysh", "~> 1.0.0"`
- 中央仓库: https://rubygems.org/
