# capistrano-nobrainer

**Tag**: web, cli, database, networking, filesystem, data

## 简介

["This gem adds the integration for the nobrainer gem in Capistrano.\n\nIt creates the indexes automatically and run the database migration if any (WARNING: You need to use the zedtux's nobrainer fork in order to use migration scripts until it get merged).\n\n| Feature                     | capistrano-nobrainer version  |\n| --------------------------- | ----------------------------- |\n| Nobrainer indexes creation  | 0.2.0                         |\n| Nobrainer migration scripts | 0.3.0                         |\n\nSo if you don't use migration scripts, stick on version 0.2.0.\n\n## Installation\n\nAdd this line to your application's Gemfile:\n\n```ruby\ngem 'capistrano-nobrainer', '~> 0.2', require: false\n```\n\nAnd then execute:\n\n    $ bundle install\n\nOr install it yourself as:\n\n    $ gem install capistrano-nobrainer\n\n## Usage\n\nAdd the following require to your `Capfile`:\n\n```ruby\nrequire 'capistrano/nobrainer'\n```\n\n## Development\n\nAfter checking out the repo, run `bin/setup` to install dependencies. You can also run `bin/console` for an interactive prompt that will allow you to experiment.\n\nTo install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org).\n\n## Contributing\n\nBug reports and pull requests are welcome on GitHub at https://gitlab.com/zedtux/capistrano-nobrainer. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [code of conduct](https://gitlab.com/zedtux/capistrano-nobrainer/blob/master/CODE_OF_CONDUCT.md).\n"]

## 官网

- 主页: https://gitlab.com/zedtux/capistrano-nobrainer
- 更新日志: https://gitlab.com/zedtux/capistrano-nobrainer/-/blob/master/CHANGELOG.md
- RubyGems: https://rubygems.org/gems/capistrano-nobrainer

## 历史版本号

- 0.3.0 (2020-11-02)
- 0.2.0 (2020-10-23)

## 获取地址

- RubyGems: https://rubygems.org/gems/capistrano-nobrainer
- gem 安装: `gem install capistrano-nobrainer`
- Bundler: `gem "capistrano-nobrainer"`
- 最新版本: 0.3.0
- 最新版归档: https://rubygems.org/downloads/capistrano-nobrainer-0.3.0.gem
- 版本锁定: `gem "capistrano-nobrainer", "~> 0.3.0"`
- 中央仓库: https://rubygems.org/
